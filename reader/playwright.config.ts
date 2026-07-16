import { defineConfig } from '@playwright/test'

const port = 4174

export default defineConfig({
  testDir: './tests/layout',
  fullyParallel: false,
  timeout: 180_000,
  expect: { timeout: 10_000 },
  reporter: [['line']],
  use: {
    baseURL: `http://127.0.0.1:${port}`,
    browserName: 'chromium',
    headless: true,
    viewport: { width: 1600, height: 1000 },
  },
  webServer: {
    command: `npm exec vite -- --host 127.0.0.1 --port ${port} --strictPort`,
    url: `http://127.0.0.1:${port}`,
    reuseExistingServer: false,
    timeout: 120_000,
  },
})
