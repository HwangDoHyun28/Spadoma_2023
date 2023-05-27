const config = {
  content: [
    "./src/**/*.{html,js,svelte,ts}",
    "./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}",
  ],

  theme: {
    extend: {
      colors: {
        'spadoma1': '#9DCDD1',
        'spadoma2': '#6BB9C0',
        'spadoma3': '#42A0A9',
        'spadoma4': '#0694A2',
        'spadoma5': '#FCD34D',
        'spadoma6': '#D9D9D9',
      }
    },
  },

  plugins: [
    require('flowbite/plugin')
  ],
  darkMode: 'class',
};

module.exports = config;
