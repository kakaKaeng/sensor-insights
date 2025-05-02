<script setup lang="ts">
const langs = {
  en: 'English',
  th: 'Thai',
};
</script>

<template>
  <select
    id="langs"
    class="bg-gray-10 dark:bg-gray-700 dark:text-gray-100 border border-gray-200 dark:border-gray-600 text-gray-900 text-sm rounded-md"
    v-model="$i18n.locale"
  >
    <option v-for="(lang, locale) in langs" :key="`locale-${locale}`" :value="locale">
      {{ $t(`commons.${locale}`) }}
    </option>
  </select>
</template>
