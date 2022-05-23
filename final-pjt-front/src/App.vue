<template>
  <div class="main" id="app">
    <router-link :to="{ name: 'movieList' }">Home</router-link>
    <router-link :to="{ name: 'logout' }" v-if="isLoggedIn">Logout</router-link>
    <div class="d-inline" v-else>
      <router-link :to="{ name: 'signup' }">Signup</router-link> 
      <router-link :to="{ name: 'login' }">Login</router-link>
    </div>
    <router-link :to="{ name: 'articleList' }">Community</router-link>

    <p v-if="isLoggedIn">반갑습니다. {{ currentUser.username }}님!</p>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['currentUser', 'isLoggedIn']),
    // user() {
    //   return this.currentUser
    // },
  }
}
</script>
<style>
@font-face {
    font-family: 'InfinitySans-RegularA1';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/InfinitySans-RegularA1.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'IBMPlexSansKR-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/IBMPlexSansKR-Light.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

#app {
  font-family: IBMPlexSansKR-Regular, InfinitySans-RegularA1, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
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
