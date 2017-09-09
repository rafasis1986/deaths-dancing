// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueCookie from 'vue-cookie'
import App from './App'
import router from './router'
import store from './store'
import vueEventCalendar from 'vue-event-calendar'
import datePicker from 'vue-bootstrap-datetimepicker'
import 'bootstrap/dist/css/bootstrap.css'
import 'vue-event-calendar/dist/style.css'
import 'eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css'
// import './assets/style/custom.css'

Vue.use(datePicker)
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
