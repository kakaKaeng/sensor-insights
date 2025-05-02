import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import ECharts from 'vue-echarts';
import router from './router';
import { i18n } from '@/translates.ts';
import { use } from 'echarts/core';
import { LineChart } from 'echarts/charts';
import { CanvasRenderer } from 'echarts/renderers';
import {
  GridComponent,
  LegendComponent,
  TitleComponent,
  TooltipComponent,
  VisualMapComponent,
  MarkLineComponent,
  DataZoomComponent,
  ToolboxComponent,
  DataZoomInsideComponent,
  DataZoomSliderComponent,
} from 'echarts/components';

use([
  CanvasRenderer,
  LineChart,
  TitleComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent,
  VisualMapComponent,
  MarkLineComponent,
  DataZoomComponent,
  ToolboxComponent,
  DataZoomInsideComponent,
  DataZoomSliderComponent,
]);

const app = createApp(App);

app.use(i18n);
app.use(router);
app.component('v-chart', ECharts);

app.mount('#app');
