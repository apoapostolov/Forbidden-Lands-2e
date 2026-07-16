import { expect, test, type Page } from '@playwright/test'
import { mkdirSync, writeFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

interface OverflowFinding {
  page: number
  region: string
  segmentId: string
  segmentType: string
  axis: 'bottom' | 'left' | 'right'
  overflowPx: number
  excerpt: string
}

const testDirectory = dirname(fileURLToPath(import.meta.url))
const reportPath = resolve(testDirectory, '../../test-results/layout-overflow.json')
// One CSS pixel becomes fractional after the reader's spread scale transform;
// allow two rendered pixels for rounding while still catching visible overlap.
const verticalTolerancePx = 2
// Decorative blockquote rails intentionally bleed five pixels beyond their
// text column. Larger horizontal excursions indicate real margin overflow.
const horizontalTolerancePx = 6

async function inspectVisiblePage(page: Page, pageNumber: number) {
  return page.locator(`[data-book-page="${pageNumber}"]`).evaluate(
    (pageElement, tolerances) => {
      const round = (value: number) => Math.round(value * 100) / 100
      const footer = pageElement.querySelector<HTMLElement>('[data-page-footer]')
      const flowRoot = pageElement.querySelector<HTMLElement>('[data-flow-root]')
      if (!footer || !flowRoot) {
        throw new Error(`Page ${pageElement.getAttribute('data-book-page')} lacks audit markers`)
      }

      const footerTop = footer.getBoundingClientRect().top
      const rootRect = flowRoot.getBoundingClientRect()
      const findings: OverflowFinding[] = []

      for (const segment of flowRoot.querySelectorAll<HTMLElement>('[data-segment-id]')) {
        const region = segment.closest<HTMLElement>('[data-flow-region]')
        if (!region) continue

        const regionRect = region.getBoundingClientRect()
        const rectangles = [segment, ...segment.querySelectorAll<HTMLElement>('*')]
          .map((element) => element.getBoundingClientRect())
          .filter((rect) => rect.width > 0 && rect.height > 0)

        const maxBottom = Math.max(...rectangles.map((rect) => rect.bottom))
        const minLeft = Math.min(...rectangles.map((rect) => rect.left))
        const maxRight = Math.max(...rectangles.map((rect) => rect.right))
        const excerpt = (segment.textContent ?? '').replace(/\s+/gu, ' ').trim().slice(0, 100)
        const base = {
          page: Number(pageElement.getAttribute('data-book-page')),
          region: region.dataset.flowRegion ?? 'unknown',
          segmentId: segment.dataset.segmentId ?? 'unknown',
          segmentType: segment.dataset.segmentType ?? 'unknown',
          excerpt,
        }

        if (maxBottom > footerTop + tolerances.vertical) {
          findings.push({
            ...base,
            axis: 'bottom',
            overflowPx: round(maxBottom - footerTop),
          })
        }

        const legalLeft = regionRect.left - tolerances.horizontal
        const legalRight = regionRect.right + tolerances.horizontal
        if (
          minLeft < legalLeft &&
          minLeft < rootRect.left - tolerances.horizontal
        ) {
          findings.push({
            ...base,
            axis: 'left',
            overflowPx: round(Math.min(regionRect.left, rootRect.left) - minLeft),
          })
        }
        if (
          maxRight > legalRight &&
          maxRight > rootRect.right + tolerances.horizontal
        ) {
          findings.push({
            ...base,
            axis: 'right',
            overflowPx: round(maxRight - Math.max(regionRect.right, rootRect.right)),
          })
        }
      }

      return findings
    },
    { vertical: verticalTolerancePx, horizontal: horizontalTolerancePx },
  )
}

test('all columns and tables remain inside the printable page area', async ({ page }) => {
  await page.goto('/#page/1')
  await expect(page.locator('[data-book-page="1"]')).toBeVisible()
  await page.evaluate(() => document.fonts.ready)

  const totalPages = Number(
    (await page.locator('#page-jump + span').textContent())?.replace(/\D+/gu, ''),
  )
  expect(totalPages).toBeGreaterThan(0)

  const findings: OverflowFinding[] = []
  const jumpInput = page.locator('#page-jump')

  for (let firstPage = 1; firstPage <= totalPages; firstPage += 2) {
    if (firstPage !== 1) {
      await jumpInput.fill(String(firstPage))
      await jumpInput.press('Enter')
      await expect(page.locator(`[data-book-page="${firstPage}"]`)).toBeVisible()
    }

    findings.push(...(await inspectVisiblePage(page, firstPage)))
    if (firstPage + 1 <= totalPages) {
      findings.push(...(await inspectVisiblePage(page, firstPage + 1)))
    }
  }

  mkdirSync(dirname(reportPath), { recursive: true })
  writeFileSync(reportPath, `${JSON.stringify({ totalPages, findings }, null, 2)}\n`)

  const formatted = findings
    .map(
      (finding) =>
        `page ${finding.page}, ${finding.region}, ${finding.segmentType} ${finding.segmentId}: ` +
        `${finding.axis} overflow ${finding.overflowPx}px — ${finding.excerpt}`,
    )
    .join('\n')

  expect(findings, formatted).toEqual([])
})
