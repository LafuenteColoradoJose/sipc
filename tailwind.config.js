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
        mytheme: {
          "primary": "#007ea8",
          "secondary": "#00a4d6",
          "accent": "#84d2f6",
          "neutral": "#c9dff2",
          "base-100": "#b1e0e7",
          "info": "#0000ff",
          "success": "#00ff00",
          "warning": "#00ff00",
          "error": "#ff0000",
        },
      },
    ],
  },
  plugins: [
    require('daisyui'),
  ],
}