import { describe, expect, it } from 'vitest'
import { isEditableTarget } from './keyboard'

describe('isEditableTarget', () => {
  it('recognizes form controls and contenteditable descendants', () => {
    const input = document.createElement('input')
    const editor = document.createElement('div')
    const child = document.createElement('span')
    editor.setAttribute('contenteditable', 'true')
    editor.appendChild(child)

    expect(isEditableTarget(input)).toBe(true)
    expect(isEditableTarget(child)).toBe(true)
    expect(isEditableTarget(document.createElement('p'))).toBe(false)
  })
})
