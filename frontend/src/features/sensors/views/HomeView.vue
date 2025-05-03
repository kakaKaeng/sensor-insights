<script setup lang="ts">
import AggregateGroup from '@/features/sensors/components/AggregateGroup.vue';
import type { SensorAggregated } from '@/features/sensors/interfaces/SensorAggregated.ts';
import { IntervalOptions, sensorApiService } from '@/features/sensors/services/SensorApiService.ts';
import { onMounted, onUnmounted, ref, watch } from 'vue';
import IntervalOptionSelect from '@/features/sensors/components/IntervalOptionSelect.vue';
import { useDebounceFn } from '@vueuse/core';
import type { SensorProcessed } from '@/features/sensors/interfaces/SensorProcessed.ts';

const aggregatedData = ref<SensorAggregated | null>(null);
const processedData = ref<SensorProcessed | null>(null);
const loading = ref(true);

const selectedInterval = ref<IntervalOptions>(IntervalOptions.LAST_5_MINUTES);
let intervalId: number;

onMounted(async () => {
  await loadSensorData(true).then(() => {
    intervalId = setInterval(loadSensorData, 5000);
  });
});

onUnmounted(() => {
  clearInterval(intervalId);
});

watch(
  selectedInterval,
  useDebounceFn(() => {
    loadSensorData(true);
  }, 300),
);

const loadSensorData = async (setLoading: boolean = false) => {
  try {
    if (setLoading) {
      loading.value = true;
    }
    const [processed, aggregated] = await Promise.all([
      sensorApiService.getSensorProcessed(selectedInterval.value),
      sensorApiService.getSensorAggregated(selectedInterval.value),
    ]);
    processedData.value = processed.data;
    aggregatedData.value = aggregated.data;
  } catch (err) {
    console.error('API call failed', err);
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="container m-auto flex flex-col items-center">
    <div class="mt-4">
      <IntervalOptionSelect v-model="selectedInterval"></IntervalOptionSelect>
    </div>

    <AggregateGroup
      :sensor-aggregate-column="aggregatedData?.temperature"
      :sensor-processed-column="processedData?.temperature"
      :timestamp="processedData?.timestamp"
      :loading="loading"
      class="my-5"
    >
      <template #title>{{ $t('sensors.temperature') }}</template>
    </AggregateGroup>
    <AggregateGroup
      :sensor-aggregate-column="aggregatedData?.humidity"
      :sensor-processed-column="processedData?.humidity"
      :timestamp="processedData?.timestamp"
      :loading="loading"
      class="my-5"
    >
      <template #title>{{ $t('sensors.humidity') }}</template>
    </AggregateGroup>
    <AggregateGroup
      :sensor-aggregate-column="aggregatedData?.air_quality"
      :sensor-processed-column="processedData?.air_quality"
      :timestamp="processedData?.timestamp"
      :loading="loading"
      class="my-5"
    >
      <template #title>{{ $t('sensors.air_quality') }}</template>
    </AggregateGroup>
  </div>
</template>

<style scoped></style>
