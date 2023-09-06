module.exports = {
  apps : [{
    name   : "app1",
    script : "./build/index.js",
    env_production: {
        NODE_ENV: 'production',
        PORT: 5177 // port the app will be launched on
    }
  }]
}
