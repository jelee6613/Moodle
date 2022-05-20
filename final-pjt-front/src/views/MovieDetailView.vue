<template>
  <div>
    movie detail
    <h1>{{ movie }}</h1>

    <p>
      {{ movie }}
    </p>

  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name: 'MovieDetailView',
    date() {
      return {
        moviePk: this.$route.params.moviePk
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