/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        teal: {
          dark: '#003333',
          light: '#66CCCC',
        },
        pink: {
          dark: '#993366',
          light: '#FF99CC',
        },
        yellow: {
          dark: '#CCCC33',
          light: '#FFFF99',
        },
        background: {
          dark: '#333333',
          light: '#666666',
        },
        text: {
          light: '#FFFFFF',
          dark: '#CCCCCC',
        },
        button: {
          dark: '#336666',
          light: '#66CCCC',
        },
        card: {
          background: '#333333',
          text: '#FFFFFF',
          border: '#66CCCC',
        },
      },
    },
  },
  plugins: [],
}

