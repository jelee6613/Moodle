<template>
  <div>
    <h2>movie detail</h2>
    <h1>{{ movie.title }}</h1>

    <p>
      {{ movie }}
    </p>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieDetailView',
  data() {
    return {
      movieTitle: this.$route.params.movieTitle
    }
  },
  computed: {
    ...mapGetters(['movie'])
  },
  methods: {
    ...mapActions(['fetchMovie'])
  },
  created() {
    this.fetchMovie(this.movieTitle)
  }
}
</script>

<style>

</style>