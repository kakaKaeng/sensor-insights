<script setup lang="ts">
import type { SensorAggregatedColumn } from '@/features/sensors/interfaces/SensorAggregated.ts';
import AggregateData from '@/features/sensors/components/AggregateData.vue';
import ProcessedChart from '@/features/sensors/components/ProcessedChart.vue';
import type { SensorProcessedColumn } from '@/features/sensors/interfaces/SensorProcessed.ts';

defineProps<{
  sensorAggregateColumn?: SensorAggregatedColumn;
  sensorProcessedColumn?: SensorProcessedColumn;
  loading: boolean;
}>();
</script>

<template>
  <div class="p-6 bg-white dark:bg-gray-700 dark:text-white rounded-lg shadow-md lg:w-full sm:w-2xl w-100 transition duration-300">
    <h1 class="text-xl">
      <slot name="title"></slot>
    </h1>

    <ProcessedChart :sensor-processed-column="sensorProcessedColumn" :loading="loading" />

    <div class="mt-6 grid lg:grid-cols-4 sm:grid-cols-2 grid-cols-1 gap-y-4 pb-2">
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
