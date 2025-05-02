import { ref, watchEffect } from 'vue';

const isDark = ref<boolean>(false);

export function useDarkMode() {
  watchEffect(() => {
    const html = document.documentElement;
    html.setAttribute('data-theme', isDark.value ? 'dark' : 'light');
  });

  return {
    isDark,
    toggle: () => (isDark.value = !isDark.value),
  };
}
