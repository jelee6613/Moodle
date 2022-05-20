<template>
  <div>
    movie detail
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
        moviePk: this.$route.params.moviePk
      }
    },
    computed: {
      ...mapGetters(['movie'])
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