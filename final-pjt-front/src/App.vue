<template>
  <div id="app">
    <router-link :to="{ name: 'signup' }">Signup</router-link> | 
    <router-link :to="{ name: 'login' }">Login</router-link> | 
    <router-link :to="{ name: 'logout' }">Logout</router-link> | 
    <router-link :to="{ name: 'articleList' }">Community</router-link>

    <p>반갑습니다. {{ user.username }}님!</p>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['currentUser']),
    user() {
      return JSON.parse(this.currentUser)
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
