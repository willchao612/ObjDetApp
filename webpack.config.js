const path = require('path');

module.exports = {
  entry: './app.js',
  output: {
    filename: './app.bundle.js',
    path: path.resolve(__dirname, 'build'),
  },
  mode: 'development',
  devServer: {
    port: 5512,
    static: {
      directory: __dirname,
    },
  },
};
