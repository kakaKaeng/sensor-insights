<script setup lang="ts">
const langs = {
  en: 'English',
  th: 'Thai',
};
</script>

<template>
  <select
    id="langs"
    class="bg-gray-10 border border-gray-200 text-gray-900 text-sm rounded-md"
    v-model="$i18n.locale"
  >
    <option v-for="(lang, locale) in langs" :key="`locale-${locale}`" :value="locale">
      {{ lang }}
    </option>
  </select>
</template>
