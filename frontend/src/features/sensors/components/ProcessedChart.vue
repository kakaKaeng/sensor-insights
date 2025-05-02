<script setup lang="ts">
import { ref, watch } from 'vue';
import type { SensorProcessedColumn } from '@/features/sensors/interfaces/SensorProcessed.ts';

const props = defineProps<{
  sensorProcessedColumn?: SensorProcessedColumn;
  loading: boolean;
}>();

const data = ref<number[]>([]);
const lowerBound = ref<number>(0);
const upperBound = ref<number>(0);

const getVisualMap = () => {
  return {
    type: 'piecewise',
    seriesIndex: 0,
    pieces: [
      { max: lowerBound.value, color: 'red'},
      { min: lowerBound.value, max: upperBound.value },
      { min: upperBound.value, color: 'red' },
    ],
    textStyle: { color: ['red', 'blue', 'red']},
    top: 'center',
    right: 10,
  };
};

const getMarkLine = () => {
  return [
    {
      yAxis: lowerBound.value,
    },
    {
      yAxis: upperBound.value,
    },
  ];
};

const lineChartOptions = ref({
  visualMap: getVisualMap(),
  tooltip: {
    trigger: 'axis',
  },
  grid: {
    left: '0',
  },
  xAxis: {
    type: 'category',
    show: false,
  },
  yAxis: {
    type: 'value',
    show: true,
    scale: true,
  },
  toolbox: {
    feature: {
      dataZoom: {
        yAxisIndex: 'none',
      },
      restore: {},
    },
  },
  dataZoom: [
    {
      type: 'inside',
    },
    {
      type: 'slider',
      show: true,
    },
  ],
  series: {
    type: 'line',
    data: data,
    smooth: true,
    showSymbol: false,
    markLine: {
      silent: true,
      lineStyle: {
        color: '#5470c6',
        type: 'solid',
      },
      data: getMarkLine(),
    },
  },
});

watch(
  () => props.sensorProcessedColumn,
  (newVal) => {
    data.value = newVal?.value ?? [];
    lowerBound.value = newVal?.iqr_lower ?? 0;
    upperBound.value = newVal?.iqr_upper ?? 0;
    lineChartOptions.value.visualMap = getVisualMap();
    lineChartOptions.value.series.markLine.data = getMarkLine();
  },
  { immediate: true },
);
</script>

<template>
  <div v-if="loading" class="animate-pulse">
    <div class="h-60 bg-gray-300 rounded-md w-full my-5"></div>
  </div>
  <div v-else-if="data.length === 0" class="h-60 w-full flex">
    <h1 class="text-center content-center m-auto text-xl">{{ $t('commons.data_not_found') }}</h1>
  </div>
  <v-chart v-else :option="lineChartOptions" autoresize style="width: 100%; height: 300px" />
</template>

<style scoped></style>
