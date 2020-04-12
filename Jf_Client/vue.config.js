module.exports = {
  devServer: {
    proxy: {
      '/ajax': {
        target: 'http://localhost:5000',
        ws: true,
        changeOrigin: true
      }
    }
  }
}