/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,jinja2}",
    "./static/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#6366f1',
        'primary-dark': '#4f46e5',
        secondary: '#10b981',
        dark: '#1e293b',
        light: '#f8fafc',
        gray: '#64748b',
      },
    },
  },
  plugins: [],
}
