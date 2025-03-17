// https://nuxt.com/docs/api/configuration/nuxt-config

import { fileURLToPath } from 'url'

export default defineNuxtConfig({
  devtools: { enabled: true },
  srcDir: 'src/',

  alias: {
    '@': fileURLToPath(new URL('./src/', import.meta.url)),
  },

  css: ['@/assets/css/main.css'],

  modules: [
    '@nuxtjs/tailwindcss',
    "@nuxt/fonts", 
    "@nuxt/icon",

  ],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  app: {
    pageTransition: { name: 'page', mode: 'out-in' },
    layoutTransition: { name: 'page', mode: 'out-in' },
    head: {
      title: 'SIPC',
      charset: 'utf-8',
      meta: [
        { name: 'description', content: 'Sistema Inteligente de Predicción Cardiovascular' }
      ],
      link: [{ rel: 'icon', type: 'image/png', href: '/favicon-32x32.png' }]
    }
  },

  compatibilityDate: '2025-03-17',
})