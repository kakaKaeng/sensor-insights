<script setup lang="ts">
import { useDarkMode } from '@/shared/composables/useDarkMode.ts';

const { isDark } = useDarkMode();
</script>

<template>
  <label class="inline-flex items-center cursor-pointer">
    <input type="checkbox" value="" class="sr-only peer" v-model="isDark" />
    <div
      class="relative w-11 h-6 bg-gray-700 dark:bg-gray-100 peer-focus:outline-none peer-focus:ring-4 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:border-gray-600 peer-checked:white dark:white after:bg-white dark:after:bg-gray-700"
    ></div>
  </label>
</template>

<style scoped></style>
