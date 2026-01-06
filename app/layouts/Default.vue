<template>

  <main class="p-4 flex flex-col justify-between min-h-screen relative">
    <NavBar @toggle-theme="toggleTheme" />
    <Title />
    <Form />
    <Advise />
    <Footer />
    <NuxtPage />
  </main>


</template>

<script setup>
import { provide } from 'vue';
import NavBar from '~/components/NavBar.vue';
import Title from '~/components/Title.vue';
import Footer from '~/components/Footer.vue';
import Advise from '~/components/Advise.vue';
import Form from '~/components/Form.vue';

// Theme management is now handled in Header.vue via useAppTheme composable
</script>

<style scoped>
main {
  font-family: 'Onest Variable', sans-serif;
}

/* Pseudo-element for the background image to add opacity/blending */
main::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('/img/bg.svg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0.1;
  /* Reduced opacity to make it look decent */
  z-index: 0;
  pointer-events: none;
}

/* Ensure content sits above the background */
main>* {
  position: relative;
  z-index: 1;
}
</style>
