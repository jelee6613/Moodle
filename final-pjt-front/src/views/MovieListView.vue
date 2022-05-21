<template>
  <div>
    <p>MovieListView</p>

    <div>
      <form @submit="fetchMoviesSearch">
        <label for="keyword">검색어</label>
        <input type="text" v-model="keyword" id="keyword" required>
      </form>
      <!-- <button @click="fetchMoviesUpdate">TMDB API 불러오기</button> -->
    </div>

    <div>
      <h3>현재상영작</h3>
      <movie-list-item
        v-for="nowPlaying in nowPlayings"
        :key="nowPlaying.pk"
        :movie="nowPlaying"
      ></movie-list-item>
    </div>
    <div>
      <h3>인기작</h3>
      <movie-list-item
        v-for="popular in populars"
        :key="popular.pk"
        :movie="popular"
      ></movie-list-item>
    </div>
    <div>
      <h3>상영예정작</h3>
      <movie-list-item
        v-for="upcoming in upcomings"
        :key="upcoming.pk"
        :movie="upcoming"
      ></movie-list-item>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'MovieListView',
  data() {
    return {
      keyword: ''
    }
  },
  components: { MovieListItem },
  computed: {
    ...mapGetters(['nowPlayings', 'upcomings', 'populars'])
  },
  methods: {
    ...mapActions(['fetchMoviesSearch', 'fetchMovies'])
  },
  mounted() {
    this.fetchMovies()
  },
}
</script>

<style>

</style>