<script setup lang="ts">
import type { SensorAggregateColumn } from '@/features/sensors/interfaces/SensorAggregated.ts';
import AggregateData from '@/features/sensors/components/AggregateData.vue';

defineProps<{
  sensorAggregateColumn?: SensorAggregateColumn;
  loading: boolean;
}>();
</script>

<template>
  <div class="p-6 bg-white rounded-lg shadow-md lg:w-full sm:w-2xl w-100">
    <h1 class="underline text-base">
      <slot name="title"></slot>
    </h1>

    <div class="mt-4 grid lg:grid-cols-4 sm:grid-cols-2 grid-cols-1 gap-y-4">
      <AggregateData :value="sensorAggregateColumn?.mean" :loading="loading">
        <template #title>{{ $t('sensors.mean') }}</template>
      </AggregateData>
      <AggregateData :value="sensorAggregateColumn?.median" :loading="loading">
        <template #title>{{ $t('sensors.median') }}</template>
      </AggregateData>
      <AggregateData :value="sensorAggregateColumn?.min" :loading="loading">
        <template #title>{{ $t('sensors.min') }}</template>
      </AggregateData>
      <AggregateData :value="sensorAggregateColumn?.max" :loading="loading">
        <template #title>{{ $t('sensors.max') }}</template>
      </AggregateData>
    </div>
  </div>
</template>

<style scoped></style>
