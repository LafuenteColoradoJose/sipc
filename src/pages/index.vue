<template>
  <html :data-theme="theme">
  <main :class="{ 'theme-dark': theme === 'dark', 'theme-light': theme === 'light' }" class="p-2 flex flex-col gap-2">
    <header class="flex flex-row justify-between items-center">
     
        <svg xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 48 48">
          <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" d="m24 41.824l16.23-19.05A10.13 10.13 0 1 0 24 10.694" />
          <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" d="M14 21.114h5l3-6l4 12l3-6h5" />
          <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" d="M24 41.824L7.77 22.774A10.13 10.13 0 1 1 24 10.693" />
        </svg>
  
        <label class="swap swap-rotate">
  
          <!-- this hidden checkbox controls the state -->
          <input type="checkbox" class="theme-controller" @change="toggleTheme" value="dark" />
  
          <!-- sun icon -->
          <svg class="swap-off fill-current w-10 h-10" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path
              d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z" />
          </svg>
  
          <!-- moon icon -->
          <svg class="swap-on fill-current w-10 h-10" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path
              d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z" />
          </svg>
  
        </label>

    </header>
    <div class="flex flex-col items-center">
      <h1 class="text-6xl font-semibold">S.I.P.C.</h1>
      <h2 class="text-2xl font-light text-center">Sistema Inteligente de Predicción Cardiovascular</h2>
    </div>
    <Form />
  </main>

  </html>
</template>

<script setup>
// Supports weights 100-900
import '@fontsource-variable/onest';
import Form from '@/components/Form.vue';
import { ref, provide } from 'vue';

const theme = ref('light');
provide('theme', theme);

function toggleTheme() {
  theme.value = theme.value === 'light' ? 'dark' : 'light';
}

</script>

<style scoped>
main {
  font-family: 'Onest Variable', sans-serif;
  overflow: hidden;
  background-image: url('/img/bg.svg');
  /* background-image: linear-gradient(white 10% , white 50%, black 90%); */
  /* background-image: repeating-radial-gradient(red, yellow 10%, green 20%); */
  /* background-color: rgba(255, 255, 255, 0.9); */
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-repeat: no-repeat,
}

.theme-dark {
  color: #b1e0e7;
  /* Color de texto para tema oscuro */

}

.theme-light {
  color: #007ea8;
  /* Color de texto para tema claro */
}
</style>
