export interface SensorAggregatedColumn {
  mean: number;
  median: number;
  min: number;
  max: number;
}

export interface SensorAggregated {
  count: number;
  temperature: SensorAggregatedColumn;
  humidity: SensorAggregatedColumn;
  air_quality: SensorAggregatedColumn;
}
