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
        <ul class="navbar-nav col">
          <div>
            <li class="m-3">
              <router-link :to="{ name: 'movieRecommendation' }">오늘 뭐 보지</router-link>
              <!-- <router-link v-else :to="{ name: 'login' }">오늘 뭐 보지</router-link> -->
            </li>
          </div>
          <div>
            <li class="m-3">
              <router-link :to="{ name: 'articleList' }">커뮤니티</router-link>
              <!-- <router-link v-else :to="{ name: 'login' }">커뮤니티</router-link> -->
            </li>
          </div>
          <div class="ms-lg-auto">
            <li class="mx-3 navbar-text dropdown" v-if="isLoggedIn">
              <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                {{ currentUser.username }}님
              </a>
              <ul class="dropdown-menu dropdown-menu-end dropdown-menu-dark" aria-labelledby="navbarDropdownMenuLink">
                <li class="m-3">
                  <router-link class="dropdown-item" :to="{ name: 'profile', params: { username: currentUser.username }}">마이페이지</router-link>
                </li>
                <li class="m-3">
                  <router-link class="dropdown-item" :to="{ name: 'logout' }">로그아웃</router-link>
                </li>
              </ul>
            </li>
            <div class="d-flex" v-else>
              <div class="row">
                <li class="col-12 col-lg-auto m-3">
                  <router-link class="dropdown-item" :to="{ name: 'signup' }">회원가입</router-link> 
                </li>
                <li class="col-12 col-lg-auto m-3">
                  <router-link class="dropdown-item" :to="{ name: 'login' }">로그인</router-link>
                </li>
              </div>
            </div>
          </div>
        </ul>
      </div>
    </nav>
    <router-view :key="$route.path"/>  
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

@font-face {
    font-family: 'IBMPlexSansKR-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/IBMPlexSansKR-Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'SuseongDotum';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2205@1.0/SuseongDotum.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'LeferiPoint-WhiteObliqueA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/LeferiPoint-WhiteObliqueA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

.font-bold {
  font-family: SuseongDotum;
  font-size: 3rem;
}

.font-description {
  font-family: LeferiPoint-WhiteObliqueA;
  font-size: 1.15rem;
}

.text-large {
  font-size: 1.6rem;

}
.text-medium {
  font-size: 1.2rem !important;
}

.text-small {
  font-size: 0.9rem !important;
}

body {
  background-color: #26282B;
  box-sizing: border-box;
}

#app {
  font-family: IBMPlexSansKR-Regular, InfinitySans-RegularA1, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #fff !important;
}

nav {
  padding: 1.2rem !important;
  background-color: transparent;
  z-index: 1;
}

nav a {
  font-size: 1.2rem !important;
  color: #ffffff; 
  text-decoration: none !important;
}

nav a:hover {
  color: #5f85db !important;
}

nav a.router-link-exact-active {
  color: #90b8f8 !important;                     
}

.navbar-text,
.navbar-text a,
.nav-link {
  color: #ffffff;
}

.navbar-toggler {
  color: #ffffff !important;
  border: none;
}

.dropdown-menu[data-bs-popper] {
  right: 0;
}

a { 
  color: #ffffff;
  text-decoration: none;
  cursor: pointer;
}

a:hover {
  color: #90b8f8;
  text-decoration: underline;
}

.logo {
  max-width: 55px;
  margin-right: 1rem;
}

.account {
  flex-direction: column;
}
</style>
