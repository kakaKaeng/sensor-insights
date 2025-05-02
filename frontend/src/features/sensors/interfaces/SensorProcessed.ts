export interface SensorColumn {
  value: number[];
  iqr_lower: number | null;
  iqr_upper: number | null;
}

export interface SensorProcessed {
  count: number;
  temperature: SensorColumn;
  humidity: SensorColumn;
  air_quality: SensorColumn;
}
