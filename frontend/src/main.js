import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store'
import router from '@/router'

// order is important
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.productionTip = false

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
