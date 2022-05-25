<template>
  <div>
    <h2>movie detail</h2>

    <div>
      <h1>{{ movie.title }}</h1>
    </div>
    <div>
      {{ movie.overview }}
    </div>
    <div>
      {{ movie.poster_path }}
    </div>
    <div>
      {{ movie.backdrop_path }}
    </div>
    <div>
      {{ movie.director }}
    </div>
    <div>
      {{ movie.average_vote }}
    </div>
      {{ movieGenres }}
    <div>
      {{ movie.release_date }}
    </div>
    <div>
      평점
    </div>
    <star-rating
      @click="test()"
      v-model="movieRate"
      v-bind:increment="0.5"
      v-bind:star-size="30"
      v-bind:rounded-corners="true"
      v-bind:clearable="true"
      v-bind:rount-start-rating="true"
    ></star-rating>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import StarRating from 'vue-star-rating'

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
    },
    movieRate() {
      return this.movie.rate
    }
  },
  components: {
    StarRating
  },
  methods: {
    ...mapActions(['fetchMovie']),
    test() {
      console.log(1)
    }
  },
  created() {
    this.fetchMovie(this.moviePk)
  }
}
</script>

<style>

</style>