<template>
  <div>
    <p>MovieListView</p>
    
    <button @click="fetchMoviesUpdate">TMDB API 불러오기</button>

    <movie-list-item
      v-for="movie in movies"
      :key="movie.pk"
      :movie="movie"
    ></movie-list-item>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'MovieListView',
  components: { MovieListItem },
  computed: {
    ...mapGetters(['movies'])
  },
  methods: {
    ...mapActions(['fetchMoviesUpdate', 'fetchMovies'])
  },
  created() {
    this.fetchMovies()
  },
}
</script>

<style>

</style>