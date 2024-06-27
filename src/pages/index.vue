<template>
  

    <html :data-theme="theme">
  
    <div id="prueba"  :class="{ 'theme-dark': theme === 'dark', 'theme-light': theme === 'light' }" />

    </html>


</template>

<script setup>
// Supports weights 100-900
import '@fontsource-variable/onest';
import Form from '@/components/Form.vue';
import { ref, provide } from 'vue';

useHead({
  title: 'S.I.P.C.',
  meta: [
    {
      name: 'description',
      content: 'Sistema Inteligente de Predicción Cardiovascular',
    },
  ],
  script: [
    {
      src: "https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js",
    },
  ],
});

const theme = ref('light');
provide('theme', theme);




</script>

<style scoped>

.theme-dark {
  color: #b1e0e7;
  /* Color de texto para tema oscuro */

}

.theme-light {
  color: #007ea8;
  /* Color de texto para tema claro */
}
</style>
