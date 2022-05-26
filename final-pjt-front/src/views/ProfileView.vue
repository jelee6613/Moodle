<template>
  <div class="container">
    <span class="font-bold">{{ profileUsername }}</span><br/>
    <!-- Follow -->
    <div class="my-2" v-if="profile.pk != currentUser.pk">
      <button class="btn btn-outline-light btn-sm" v-if="profile.followers.find((user) => user.pk === currentUser.pk)" @click="follow(username)">
        팔로우취소
        <i class="fa-solid fa-user-group"></i>
      </button>
      <button class="btn btn-outline-light btn-sm" v-else @click="follow(username)">
        팔로우
        <i class="fa-solid fa-user-group"></i>
      </button>
    </div>

    <div class="movie-detail-item">
      <span class="font-bold-semi-semi">
        팔로워&nbsp;
      </span>
      <span class="font-bold-semi-semi">
        {{ profile.followers.length }}
      </span>
    </div>

    <div class="movie-detail-item">
      <span class="font-bold-semi-semi">
        팔로잉&nbsp;
      </span>
      <span class="font-bold-semi-semi">
        {{ profile.followings.length }}
      </span>
    </div>

    <div class="d-flex movie-list">
      <h3 class="font-bold-semi">영화 보관함</h3>
      <div class="d-flex movie-list-item">
        <movie-list-item
          v-for="movie in profile.movies"
          :key="movie.pk"
          :movie="movie"
        ></movie-list-item>
      </div>
    </div>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'ProfileView',
  data() {
    return {
      username: this.$route.params.username
    }
  },
  components: { MovieListItem },
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

.font-bold-semi {
  font-family: Happiness-Sans-Bold;
  font-size: 2rem;
  font-weight: 100;
}

.font-bold-semi-semi {
  font-family: Happiness-Sans-Bold;
  font-size: 1.5rem;
  font-weight: 100;
}

.movie-detail-item {
  display: inline-block;
  border-bottom: #aaaaaa solid 1px;
  /* border-radius: 50px; */
  padding: 0.5rem 1.6rem;
  margin-right: 2rem;
}

.movie-list {
  flex-direction: column;
  margin: 5rem 0 ;
}

.movie-list-item {
  overflow: auto;
  scroll-snap-type: x mandatory;
}

.movie-list-item::-webkit-scrollbar {
  width: 10px;
}

.movie-list-item::-webkit-scrollbar-thumb {
  height: 30%;
  background: #ffffff;
  border-radius: 50px;
  background-clip: padding-box;
  border: 2px solid transparent;
}

.movie-list-item::-webkit-scrollbar-track {
  background: #353941; 
  border-radius: 50px;
}
</style>