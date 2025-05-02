<script setup lang="ts">
defineProps<{
  value: number;
}>();
</script>

<template>
  <div class="flex flex-col w-xs justify-center">
    <h1 class="text-4xl text-center">{{ value }}</h1>
    <h3 class="text-base text-center mt-2 uppercase">
      <slot name="title"></slot>
    </h3>
  </div>
</template>

<style scoped></style>
