<script setup lang="ts">
import AggregateGroup from '@/features/sensors/components/AggregateGroup.vue';
import type { SensorAggregated } from '@/features/sensors/interfaces/SensorAggregated.ts';
import { IntervalOptions, sensorApiService } from '@/features/sensors/services/SensorApiService.ts';
import { onMounted, ref, watch } from 'vue';
import IntervalOptionSelect from '@/features/sensors/components/IntervalOptionSelect.vue';
import { useDebounceFn } from '@vueuse/core';

const aggregatedData = ref<SensorAggregated | null>(null);
const loading = ref(true);

const selectedInterval = ref<IntervalOptions>(IntervalOptions.ALL_TIME);

onMounted(async () => {
  await loadSensorAggregated();
});

watch(
  selectedInterval,
  useDebounceFn(() => {
    loadSensorAggregated();
  }, 300),
);

const loadSensorAggregated = async () => {
  try {
    loading.value = true;
    const response = await sensorApiService.getSensorAggregated(selectedInterval.value);
    aggregatedData.value = response.data;
  } catch (err) {
    console.error('Failed to load sensor data', err);
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
      :loading="loading"
      class="my-5"
    >
      <template #title>{{ $t('sensors.temperature') }}</template>
    </AggregateGroup>
    <AggregateGroup
      :sensor-aggregate-column="aggregatedData?.humidity"
      :loading="loading"
      class="my-5"
    >
      <template #title>{{ $t('sensors.humidity') }}</template>
    </AggregateGroup>
    <AggregateGroup
      :sensor-aggregate-column="aggregatedData?.air_quality"
      :loading="loading"
      class="my-5"
    >
      <template #title>{{ $t('sensors.air_quality') }}</template>
    </AggregateGroup>
  </div>
</template>

<style scoped></style>
