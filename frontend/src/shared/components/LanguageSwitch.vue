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
    <option v-for="locale in $i18n.availableLocales" :key="`locale-${locale}`" :value="locale">
      {{ langs[locale] }}
    </option>
  </select>
</template>
