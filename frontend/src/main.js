// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueCookie from 'vue-cookie'
import vueEventCalendar from 'vue-event-calendar'

import App from './App'
import router from './router'
import store from './store'

import 'bootstrap/dist/css/bootstrap.css'
import 'vue-event-calendar/dist/style.css'

Vue.config.productionTip = false
Vue.use(VueCookie)
Vue.use(vueEventCalendar,
  {
    locale: 'en',
    color: '#97bcdc',
    weekStartOn: 1
  })

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
