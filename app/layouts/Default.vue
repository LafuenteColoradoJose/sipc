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
  isolation: isolate;
  /* Creates a new stacking context */
}

/* Pseudo-element for the background image */
main::before {
  content: "";
  position: absolute;
  inset: 0;
  /* Shorthand for top/left/right/bottom: 0 */
  background-image: url('/img/bg.svg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  /* Visible in light mode */
  z-index: -1;
  /* Behind content */
  pointer-events: none;
  transition: opacity 0.3s ease;
}


/* Ensure content sits above the background */
main>* {
  position: relative;
  z-index: 1;
}
</style>
