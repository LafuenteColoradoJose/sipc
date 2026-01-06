<template>
  <header class="flex flex-row justify-between items-center mb-4">

    <svg xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 48 48"
      class="text-[var(--primary)] transition-colors duration-300">
      <path fill="none" stroke-width="3" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
        d="m24 41.824l16.23-19.05A10.13 10.13 0 1 0 24 10.694" />
      <path fill="none" stroke-width="2" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
        d="M14 21.114h5l3-6l4 12l3-6h5" />
      <path fill="none" stroke-width="3" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
        d="M24 41.824L7.77 22.774A10.13 10.13 0 1 1 24 10.693" />
    </svg>

    <h1 class="text-6xl font-semibold ">S.I.P.C.</h1>

    <button @click="toggleTheme"
      class="flex flex-col justify-center items-center cursor-pointer p-2 rounded-full hover:bg-black/10 dark:hover:bg-white/10 transition-colors focus:outline-none"
      aria-label="Cambiar tema">
      <Icon v-if="isDark" name="mdi:weather-sunny" size="3rem" class="text-gray-800 dark:text-gray-200" />
      <Icon v-else name="mdi:weather-night" size="3rem" class="text-gray-800 dark:text-gray-200" />
    </button>
  </header>
</template>

<script setup lang="ts">
import { ref, watchEffect, onMounted } from 'vue';
import { useAppTheme } from '~/composables/useAppTheme';

const appTheme = useAppTheme();
const isDark = ref(appTheme.value === 'dark');

const toggleTheme = () => {
  const newTheme = appTheme.value === 'dark' ? 'light' : 'dark';
  appTheme.value = newTheme;
  if (!import.meta.env.SSR) {
    localStorage.setItem('theme', newTheme);
  }
};

onMounted(() => {
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  console.log("🎨 Sistema prefiere dark:", prefersDark);

  if (localStorage.getItem('theme')) {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark' || savedTheme === 'light') {
      console.log("📦 Usando tema guardado:", savedTheme);
      appTheme.value = savedTheme;
    }
  } else {
    const detectedTheme = prefersDark ? 'dark' : 'light';
    console.log("🔍 Detectado tema del sistema:", detectedTheme);
    appTheme.value = detectedTheme;
    localStorage.setItem('theme', appTheme.value);
  }
});

watchEffect(() => {
  isDark.value = appTheme.value === 'dark';

  if (!import.meta.env.SSR) {
    if (appTheme.value === 'dark') {
      document.documentElement.classList.add('dark');
      document.documentElement.classList.remove('light');
    } else {
      document.documentElement.classList.remove('dark');
      document.documentElement.classList.add('light');
    }
  }
});
</script>

<style scoped></style>
