<template>
  <div class="container">
    {{ profileUsername }}의 <h2>ProfileView</h2>

    <!-- Follow -->
    <div v-if="profile.pk != currentUser.pk">
      <button v-if="profile.followers.find((user) => user.pk === currentUser.pk)" @click="follow(username)">
        <!-- <i class="fa-solid fa-heart"></i> -->
        팔로우취소
      </button>
      <button v-else @click="follow(username)">
        팔로우
        <!-- <i class="fa-regular fa-heart"></i>  -->
      </button>
    </div>
    <div>
      팔로잉 : {{ profile.followings }}  |
      팔로우 : {{ profile.followers }}
    </div>
    <router-link :to="{ name: 'watched', params: { username: profile.username }}">
      관람한 영화
    </router-link>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'ProfileView',
  data() {
    return {
      username: this.$route.params.username
    }
  },
  computed: {
    ...mapGetters(['profile', 'currentUser']),
    profileUsername() {
      return this.profile.username
    }
  },
  methods: {
    ...mapActions(['fetchProfile', 'follow'])
  },
  created() {
    this.fetchProfile(this.username)
  }
}
</script>

<style>

</style>