<template>
  <div>
    <h2>movie detail</h2>
    <h1>{{ movie.title }}</h1>

    <p>
      {{ movie }}
      {{ movieGenres }}
    </p>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieDetailView',
  data() {
    return {
      moviePk: this.$route.params.moviePk
    }
  },
  computed: {
    ...mapGetters(['movie']),
    movieGenres() {
      return JSON.parse(this.movie.genre)
    }
  },
  methods: {
    ...mapActions(['fetchMovie'])
  },
  created() {
    this.fetchMovie(this.moviePk)
  }
}
</script>

<style>

</style>