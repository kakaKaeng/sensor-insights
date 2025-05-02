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
      },
    },
  },
});
