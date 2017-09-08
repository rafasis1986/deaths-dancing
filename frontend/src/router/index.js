import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
import Home from '@/components/Home'
import Profile from '@/components/User'
import Callback from '@/components/Callback'
import AuthService from './../auth/AuthService'

Vue.use(Router)
Vue.use(VueResource)

const auth = new AuthService()

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/callback',
      name: 'Callback',
      component: Callback
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      beforeEnter: (to, from, next) => {
        console.log('profile')
        if (!auth.isAuthenticated()) {
          next(false)
        } else {
          next()
        }
      }
    }
  ]
})
