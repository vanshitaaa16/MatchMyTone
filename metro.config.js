const { getDefaultConfig } = require('expo/metro-config');
const path = require('path');

const config = getDefaultConfig(__dirname);

// Block Metro's resolver AND watcher from accessing the Docker socket
// which causes EACCES permission errors on Windows
const exclusionList = [/.*docker-secrets-engine.*/];

config.resolver.blockList = exclusionList;

// Also exclude from the file watcher to prevent the FallbackWatcher crash
config.watcher = {
  ...config.watcher,
  additionalExclusions: exclusionList,
};

module.exports = config;
