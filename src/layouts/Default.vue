<template>

  <main class="p-4 flex flex-col justify-between h-dvh">
    <NavBar />
    <Title />
    <Form />
    <Advise />
    <Footer />
  </main>

</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
import Title from '@/components/Title.vue';
import Footer from '@/components/Footer.vue';
import Advise from '~/components/Advise.vue';
import Form from '~/components/Form.vue';





</script>

<style scoped>
main{
  font-family: 'Onest Variable', sans-serif;
  /* overflow: hidden; */

  background-image: url('/img/bg.svg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-repeat: no-repeat,
  

}
</style>
