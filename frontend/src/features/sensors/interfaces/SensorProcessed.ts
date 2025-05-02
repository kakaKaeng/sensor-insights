export interface SensorProcessedColumn {
  value: number[];
  iqr_lower: number | null;
  iqr_upper: number | null;
}

export interface SensorProcessed {
  count: number;
  temperature: SensorProcessedColumn;
  humidity: SensorProcessedColumn;
  air_quality: SensorProcessedColumn;
}
