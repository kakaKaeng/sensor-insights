export interface SensorAggregateColumn {
  mean: number;
  median: number;
  min: number;
  max: number;
}

export interface SensorAggregated {
  count: number;
  temperature: SensorAggregateColumn;
  humidity: SensorAggregateColumn;
  air_quality: SensorAggregateColumn;
}
