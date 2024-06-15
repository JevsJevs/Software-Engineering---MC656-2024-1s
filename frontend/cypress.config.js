const { defineConfig } = require("cypress");

module.exports = defineConfig({
  projectId: '4r47xo',
  e2e: {
    supportFile:'cypress/e2e/create_news_spec.js',
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
