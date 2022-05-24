<template>
  <div class="main" id="app">
    <nav class="navbar navbar-expand-lg bg-none">
      <router-link :to="{ name: 'movieList' }">
        <img class="logo mr-4" src="https://lab.ssafy.com/uploads/-/system/appearance/header_logo/1/ssafy_logo.png" alt="">
      </router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar" aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation">
        <i class="fa-solid fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbar">
        <ul class="navbar-nav me-auto">
          <li class="m-3">
            <router-link :to="{ name: 'movieRecommendation' }">오늘 뭐 보지</router-link>
          </li>
          <li class="m-3">
            <router-link :to="{ name: 'articleList' }">커뮤니티</router-link>
          </li>
        </ul>
        <div class="d-flex">
          <router-link class="m-3" :to="{ name: 'logout' }" v-if="isLoggedIn">로그아웃</router-link>
          <router-link class="m-3" :to="{ name: 'signup' }" v-if="!isLoggedIn">회원가입</router-link> 
          <router-link class="m-3" :to="{ name: 'login' }" v-if="!isLoggedIn">로그인</router-link>
        </div>
      </div>
    </nav>
    <div class="container">
      <div class="text-center">
        <p v-if="isLoggedIn">반갑습니다. {{ currentUser.username }}님!</p>
      </div>
      <router-view/>  
    </div>
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

body {
  background-color: #26282B;
}

#app {
  font-family: IBMPlexSansKR-Regular, InfinitySans-RegularA1, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #fff !important;
}

nav {
  padding: 1.2rem !important;
}

nav a {
  font-size: 1.2rem;
  color: #ffffff;
  text-decoration: none;
}

nav a:hover {
  color: #5f85db;
}

nav a.router-link-exact-active {
  color: #90b8f8;
}

.navbar-toggler {
  color: #ffffff !important;
  border: none;
}

.logo {
  max-width: 55px;
  margin-right: 1rem;
}

.account {
  flex-direction: column;
}
</style>
