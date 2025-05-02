import { BaseApiService } from '@/shared';
import type { SensorProcessed } from '@/features/sensors/interfaces/SensorProcessed.ts';
import type { SensorAggregated } from '@/features/sensors/interfaces/SensorAggregated.ts';

export enum IntervalOptions {
  LAST_1_MINUTE = 'last_1_minute',
  LAST_5_MINUTES = 'last_5_minutes',
  LAST_10_MINUTES = 'last_10_minutes',
  LAST_1_HOUR = 'last_1_hour',
  LAST_24_HOURS = 'last_24_hours',
  ALL_TIME = 'all_time',
}

export class SensorApiService extends BaseApiService {
  getSensorProcessed(intervalOption: IntervalOptions) {
    return this.get<SensorProcessed>('sensors/processed', {
      params: {
        interval_options: intervalOption
      }
    });
  }

  getSensorAggregated(intervalOption: IntervalOptions) {
    return this.get<SensorAggregated>('sensors/aggregated', {
      params: {
        interval_options: intervalOption
      }
    });
  }
}
