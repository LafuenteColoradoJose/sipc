<template>

    <main class="p-4 flex flex-col justify-between md:h-lvh" :data-theme="theme" :v-model="textColor">
      <NavBar @toggle-theme="toggleTheme"/>
      <Title />
      <Form />
      <Advise />
      <Footer />
      <NuxtPage />
    </main>


</template>

<script setup>
import { ref } from 'vue';
import NavBar from '@/components/NavBar.vue';
import Title from '@/components/Title.vue';
import Footer from '@/components/Footer.vue';
import Advise from '~/components/Advise.vue';
import Form from '~/components/Form.vue';

const theme = ref('light');
const textColor = ref('#1d3461')

function toggleTheme() {
  theme.value = theme.value === 'light' ? 'dark' : 'light';
  localStorage.setItem('theme', theme.value);
  console.log(theme.value);

  if (theme.value === 'light') {
    textColor.value = '#1d3461';
  } else {
    textColor.value = '#E9FFFF';
  }
}
</script>

<style scoped>
main {
  font-family: 'Onest Variable', sans-serif;
  color: v-bind(textColor);
  /* overflow: hidden; */

  background-image: url('/img/bg.svg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-repeat: no-repeat,
  
}
</style>
