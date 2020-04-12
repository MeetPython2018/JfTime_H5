import Vue from 'vue'
import App from './App.vue'
import store from './store'
import '@/assets/jquery-3.2.1.js'
import '@/assets/flexible.min.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import ElementUI from 'element-ui'
import axios from 'axios'
import qs from 'qs'
import 'element-ui/lib/theme-chalk/index.css'
import 'aplayer/dist/APlayer.min.css'
import 'aplayer/dist/APlayer.min.js'

Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.prototype.$axios = axios    //全局注册，使用方法为:this.$axios
Vue.prototype.qs = qs    //全局注册，使用方法为:this.$axios

import router from './router'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
