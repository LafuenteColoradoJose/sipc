/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/**/*.{vue,js,ts,jsx,tsx,html}",
    "./src/assets/css/*.css"
  ],
  daisyui: {
    themes: [
      "dark", // Corregido: Se debe especificar como un string si es un tema predefinido
      "light", // Corregido: Se debe especificar como un string si es un tema predefinido
      {
        
      },
    ],
  },
  plugins: [
    require('daisyui'),
  ],
}