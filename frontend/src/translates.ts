import { createI18n } from 'vue-i18n';

export const i18n = createI18n({
  locale: 'en',
  fallbackLocale: 'en',
  messages: {
    en: {
      sensors: {
        sensor: 'Sensor',
        temperature: 'Temperature',
        humidity: 'Humidity',
        air_quality: 'Air Quality',
        mean: 'Mean',
        median: 'Median',
        min: 'Min',
        max: 'Max',
        last_1_minute: 'Last 1 minute',
        last_5_minutes: 'Last 5 minutes',
        last_10_minutes: 'Last 10 minutes',
        last_1_hour: 'Last 1 hour',
        last_24_hours: 'Last 24 hours',
        all_time: 'All time',
      },
    },
    th: {
      sensors: {
        sensor: 'Sensor',
        temperature: 'อุณหภูมิ',
        humidity: 'ความชื้น',
        air_quality: 'คุณภาพอากาศ',
        mean: 'ค่าเฉลี่ย',
        median: 'ค่ามัธยฐาน',
        min: 'ค่าต่ำสุด',
        max: 'ค่าสูงสุด',
        last_1_minute: '1 นาทีสุดท้าย',
        last_5_minutes: '5 นาทีสุดท้าย',
        last_10_minutes: '10 นาทีสุดท้าย',
        last_1_hour: '1 ชั่วโมงสุดท้าย',
        last_24_hours: '24 ชั่วโมงล่าสุด',
        all_time: 'ตลอดเวลา',
      },
    },
  },
});
