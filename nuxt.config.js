// https://nuxt.com/docs/api/configuration/nuxt-config

import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  devtools: { enabled: true },
  sourcemap: {
    server: false,
    client: false
  },
  css: ['~/assets/css/main.css'],

  vite: {
    plugins: [tailwindcss()],
    optimizeDeps: {
      include: [
        '@vue/devtools-core',
        '@vue/devtools-kit',
      ]
    }
  },

  modules: ["@nuxt/fonts", "@nuxt/icon", '@nuxt/a11y'],

  app: {
    pageTransition: { name: 'page', mode: 'out-in' },
    layoutTransition: { name: 'page', mode: 'out-in' },
    head: {
      title: 'SIPC',
      charset: 'utf-8',
      meta: [
        { name: 'description', content: 'Sistema Inteligente de Predicción Cardiovascular' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ],
      htmlAttrs: {
        lang: 'es'
      }
    }
  },

  compatibilityDate: '2025-03-17',
})