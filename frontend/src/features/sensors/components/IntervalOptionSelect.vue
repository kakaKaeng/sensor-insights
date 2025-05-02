<script setup lang="ts">
import { ref, watch } from 'vue';
import { IntervalOptions } from '@/features/sensors/services/SensorApiService.ts';

const props = defineProps<{
  modelValue: IntervalOptions;
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: IntervalOptions): void;
}>();

const selected = ref(props.modelValue);

watch(selected, (val) => {
  emit('update:modelValue', val);
});
</script>

<template>
  <form class="max-w-sm mx-auto">
    <select
      id="langs"
      class="bg-gray-10 dark:bg-gray-700 dark:text-white border border-gray-200 dark:border-gray-500 text-gray-900 text-sm rounded-md"
      v-model="selected"
    >
      <option v-for="option in IntervalOptions" :key="`locale-${option}`" :value="option">
        {{ $t(`sensors.${option}`) }}
      </option>
    </select>
  </form>
</template>

<style scoped></style>
