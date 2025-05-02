<script setup lang="ts">
defineProps<{
  value?: number;
  loading: boolean;
}>();
</script>

<template>
  <div class="flex flex-col w-xs justify-center">
    <div v-if="loading" class="animate-pulse">
      <div class="h-10 bg-gray-300 rounded-full max-w-xs"></div>
    </div>
    <h1 v-else class="text-4xl text-center">{{ value ? value.toFixed(2) : 0 }}</h1>
    <h3 class="text-base text-center mt-2 uppercase">
      <slot name="title"></slot>
    </h3>
  </div>
</template>

<style scoped></style>
