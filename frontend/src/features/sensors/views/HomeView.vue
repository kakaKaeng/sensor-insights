<script setup lang="ts">
import AggregateGroup from '@/features/sensors/components/AggregateGroup.vue';
import type { SensorAggregateColumn } from '@/features/sensors/interfaces/SensorAggregated.ts';
import { IntervalOptions } from '@/features/sensors/services/SensorApiService.ts';

const mockData: SensorAggregateColumn = {
  mean: 10.05,
  median: 20.11,
  min: 10.99,
  max: 20.91,
};

const intervalOptions = IntervalOptions.ALL_TIME;


</script>

<template>
  <div class="container m-auto flex flex-col items-center">
    <AggregateGroup :sensor-aggregate-column="mockData" class="my-5">
      <template #title>{{ $t('sensors.temperature') }}</template>
    </AggregateGroup>
    <AggregateGroup :sensor-aggregate-column="mockData" class="my-5">
      <template #title>{{ $t('sensors.humidity') }}</template>
    </AggregateGroup>
    <AggregateGroup :sensor-aggregate-column="mockData" class="my-5">
      <template #title>{{ $t('sensors.air_quality') }}</template>
    </AggregateGroup>
  </div>
</template>

<style scoped></style>
