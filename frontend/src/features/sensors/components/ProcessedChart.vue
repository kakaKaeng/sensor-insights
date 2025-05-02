<script setup lang="ts">
import { ref, watch } from 'vue';
import type { SensorProcessedColumn } from '@/features/sensors/interfaces/SensorProcessed.ts';

const props = defineProps<{
  sensorProcessedColumn?: SensorProcessedColumn;
  loading: boolean;
}>();


const data = ref<number[]>([]);

const lineChartOptions = ref({
  tooltip: {
    trigger: 'axis',
  },
  xAxis: {
    type: 'category',
    data: [],
    show: false,
  },
  yAxis: {
    type: 'value',
    show: true,
  },
  series: [
    {
      type: 'line',
      data: data,
      smooth: true,
    },
  ],
});

watch(
  () => props.sensorProcessedColumn,
  (newVal) => {
    data.value = newVal?.value ?? [];
  },
  { immediate: true },
);
</script>

<template>
  <div v-if="loading" class="animate-pulse">
    <div class="h-60 bg-gray-300 rounded-md w-full my-5"></div>
  </div>
  <div v-else-if="data.length === 0" class="h-60 w-full flex">
    <h1 class="text-center content-center m-auto text-xl">{{$t('commons.data_not_found')}}</h1>
  </div>
  <v-chart v-else :option="lineChartOptions" autoresize style="width: 100%; height: 300px" />
</template>

<style scoped></style>
