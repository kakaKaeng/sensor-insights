<script setup lang="ts">
import { RouterView } from 'vue-router';
import CoreNavbar from '@/shared/components/CoreNavbar.vue';
</script>

<template>
  <div class="bg-gray-100 dark:bg-gray-600 transition duration-300">
    <CoreNavbar />
    <RouterView />
  </div>
</template>

<style scoped></style>
