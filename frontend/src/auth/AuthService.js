import Vue from 'vue'
import Auth0Lock from 'auth0-lock'
import EventEmitter from 'EventEmitter'
import { AUTH_CONFIG, API_CONFIG } from '../config'
import store from '../store'

const USER_INFO_URL = API_CONFIG.url + 'base/me/'

export default class AuthService {
  authenticated = this.isAuthenticated()
  authNotifier = new EventEmitter()
  userProfile;

  constructor () {
    this.login = this.login.bind(this)
    this.setSession = this.setSession.bind(this)
    this.logout = this.logout.bind(this)
    this.isAuthenticated = this.isAuthenticated.bind(this)
  }

  auth0 = new Auth0Lock(AUTH_CONFIG.clientId, AUTH_CONFIG.domain, {
    auth: {
      redirectUrl: AUTH_CONFIG.callbackUrl,
      responseType: 'code',
      params: { api: true }
    },
    additionalSignUpFields: [
      {
        name: 'given_name',
        placeholder: 'Enter your given name'
      },
      {
        name: 'family_name',
        placeholder: 'Enter your family name'
      }
    ],
    theme: {
      logo: './static/deaths-dancing-ico.png',
      primaryColor: '#97bcdc'
    }
  })

  login () {
    this.auth0.show()
  }

  handleAuthentication () {
    let authResult = {}
    if (Vue.cookie.get('auth_token')) {
      authResult.accessToken = Vue.cookie.get('auth_token')
      authResult.expiresAt = Vue.cookie.get('expiration_time')
      authResult.prefixToken = Vue.cookie.get('auth_prefix')
    }

    if (authResult && authResult.accessToken) {
      this.setSession(authResult)
      return this.setUser()
    } else {
      return false
    }
  }

  setSession (authResult) {
    let expiresAt = JSON.stringify(
      authResult.expiresAt * 1000 + new Date().getTime()
    )

    localStorage.setItem('access_token', authResult.accessToken)
    localStorage.setItem('prefix_token', authResult.prefixToken)
    localStorage.setItem('expires_at', expiresAt)
    this.authNotifier.emit('authChange', { authenticated: true })
  }

  logout () {
    // Clear access token and ID token from local storage
    localStorage.removeItem('access_token')
    localStorage.removeItem('expires_at')
    this.userProfile = null
    store.commit('CLEAR_ALL_DATA')
    this.authNotifier.emit('authChange', false)
    this.$router.push({ name: 'Home' })
  }

  isAuthenticated () {
    // Check whether the current time is past the
    // access token's expiry time
    let expiresAt = JSON.parse(localStorage.getItem('expires_at'))
    return new Date().getTime() < expiresAt
  }

  setAccessToken () {
    let accessToken = localStorage.getItem('access_token')
    let prefixToken = localStorage.getItem('prefix_token')
    if (!accessToken) {
      throw new Error('No access token found')
    }
    localStorage.removeItem('prefix_token')
    localStorage.setItem('access_token', prefixToken + ' ' + accessToken)
  }

  setUser () {
    this.setAccessToken()
    Vue.http.headers.common['Authorization'] = localStorage.getItem('access_token')
    Vue.http.get(USER_INFO_URL)
      .then((result) => {
        let user = {}
        user.id = result.body.data.id
        user.name = result.body.data.attributes.full_name
        user.email = result.body.data.attributes.email
        user.picture = result.body.data.attributes.picture
        store.commit('UPDATE_USER', user)
        return true
      })
  }
}
