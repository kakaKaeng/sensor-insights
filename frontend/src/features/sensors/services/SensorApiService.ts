import { BaseApiService } from '@/shared';
import type { SensorProcessed } from '@/features/sensors/interfaces/SensorProcessed.ts';
import type { SensorAggregated } from '@/features/sensors/interfaces/SensorAggregated.ts';

export class SensorApiService extends BaseApiService {
  getSensorProcessed() {
    return this.get<SensorProcessed>('sensors/processed');
  }

  getSensorAggregated() {
    return this.get<SensorAggregated>('sensors/aggregated');
  }
}
