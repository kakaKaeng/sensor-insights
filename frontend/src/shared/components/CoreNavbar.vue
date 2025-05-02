<script setup lang="ts">
import LanguageSwitch from '@/shared/components/LanguageSwitch.vue';
import DartModeSwitch from '@/shared/components/DartModeSwitch.vue';
</script>

<template>
  <nav class="w-full bg-white dark:bg-gray-800 shadow-md p-4 transition duration-300">
    <div class="flex justify-between">
      <h3 class="text-base content-center font-medium tracking-tight inline text-gray-700 dark:text-white">
        Sensor Insights
      </h3>

      <div class="flex content-center">
        <DartModeSwitch class="mx-5" />
        <LanguageSwitch />
      </div>
    </div>
  </nav>
</template>

<style scoped></style>
