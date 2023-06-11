#!/usr/bin/env node

const { spawnSync } = require('child_process');

function main() {
  const djangoSettingsModule = 'core.settings';
  const managePath = './manage.py';

  process.env.DJANGO_SETTINGS_MODULE = djangoSettingsModule;

  try {
    const result = spawnSync('python', [managePath, ...process.argv.slice(2)], { stdio: 'inherit' });

    if (result.error) {
      console.error('Failed to execute Django management command:', result.error.message);
      process.exit(1);
    }
  } catch (error) {
    console.error('An error occurred while executing the Django management command:', error);
    process.exit(1);
  }
}

main();
