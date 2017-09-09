<template>
  <div class="panel panel-default profile-area">
    <div class="panel-heading  header-center">
      <h3>User Profile</h3>
    </div>
    <div class="panel-body">
      <div class="container">
        <div class="row">
          <div class="col-md-3">
            <img :src="$store.state.user.picture" class="avatar" alt="avatar">
          </div>
          <div class="col-md-9">
            <div>
              <label><i class="glyphicon glyphicon-user"></i> Name</label>
              <h3 class="nickname">{{ $store.state.user.name }}</h3>
            </div>
            <div>
              <label><i class="glyphicon glyphicon-envelope"></i> Email</label>
              <h3 class="email">{{ $store.state.user.email }}</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: ['auth'],
  data () {
    if (this.auth.userProfile) {
      this.$nextTick(() => {
        this.profile = this.auth.userProfile
      })
    }
    return {
      profile: {}
    }
  }
}
</script>

<style>
  .profile-area img {
    max-width: 150px;
    margin-bottom: 20px;
  }

  .panel-body h3 {
    margin-top: 0;
  }
</style>
