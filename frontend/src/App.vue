<template>
  <div>
    <nav class="navbar navbar-inverse navbar-inverse-fixed-top navbar-home fixedmenu">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand img-responsive" href="/" style="padding:0px;">
            <img src="./assets/img/deaths-dancing-ico.png"  style="height:100%;">
          </a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <li>
              <a>
                <router-link :to="'/'">
                    Home
                </router-link>
              </a>
            </li>
            <li>
              <a>
                <router-link :to="'profile'"
                  v-if="authenticated">
                    Profile
                </router-link>
              </a>
            </li>
            <li>
              <a>
                <router-link :to="'schedule'"
                  v-if="authenticated">
                    Schedule
                </router-link>
              </a>
            </li>
            <li>
              <a v-if="!authenticated"
                @click="login()">
                  Log In
              </a>
            </li>
            <li>
              <a v-if="authenticated"
                @click="logout()">
                  Log Out
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container">
      <router-view 
        :auth="auth" 
        :authenticated="authenticated">
      </router-view>
    </div>
  </div>
</template>

<script>
import AuthService from './auth/AuthService'

const auth = new AuthService()

const { login, logout, authenticated, authNotifier } = auth

export default {
  name: 'app',
  data () {
    authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })
    return {
      auth,
      authenticated
    }
  },
  methods: {
    login,
    logout
  }
}
</script>


