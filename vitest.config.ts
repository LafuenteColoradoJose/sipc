import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    environment: 'happy-dom',
    globals: true,
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      include: ['app/components/**/*.vue']
    },
  },
  resolve: {
    alias: {
      '~': new URL('./app/', import.meta.url).pathname,
      '#app': new URL('./tests/mocks/app.ts', import.meta.url).pathname
    }
  }
})
