<template>
  <div>
    <img class="img-fluid" :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`" alt="">
    <div class="container movie-detail">
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
        <b-form-rating
          variant="warning"
          :value="movieRate"
          no-border inline show-value readonly          
          class="star"
        ></b-form-rating>
        <!-- {{ movie.average_vote }} -->
      </div>
        {{ movieGenres }}
      <div>
        {{ movie.release_date }}
      </div>
      <div>
        평점
        <b-form-rating
          id="rating-lg-no-border rating-inline"
          v-if="isLoggedIn"
          @change="onRate()"
          v-model="value.rate"
          variant="danger"
          class="star mb-2"
          no-border inline show-value
          size="lg"
        ></b-form-rating>
        {{ value }}
      </div>
    </div>

    <!-- <star-rating
      @click="test()"
      v-model="movieRate"
      v-bind:increment="0.5"
      v-bind:star-size="30"
      v-bind:rounded-corners="true" 
      v-bind:clearable="true"
      v-bind:round-start-rating="true"
    ></star-rating> -->

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { BFormRating } from 'bootstrap-vue'
// import StarRating from 'vue-star-rating'

export default {
  name: 'MovieDetailView',
  data() {
    return {
      moviePk: this.$route.params.moviePk,
      value: {
        moviePk: this.$route.params.moviePk,
        rate: 0,
      }
      // watchedRate: this.movie.rate,
    }
  },
  computed: {
    ...mapGetters(['movie', 'isLoggedIn']),
    movieGenres() {
      return JSON.parse(this.movie.genre)
    },
    isWatched() {
      return 'rate' in this.movie
    },
    movieRate() { // average_vote
      return this.movie.average_vote
    }
  },
  components: {
    BFormRating
  },
  methods: {
    ...mapActions(['fetchMovie', 'rateMovie']),
    onRate() {
      console.log(this.value)
      this.rateMovie(this.value)
    }
  },
  created() {
    this.fetchMovie(this.moviePk)
  }
}
</script>

<style>
/* .img-fluid {
  width: 100%;
} */
.form-control:focus {
  background-color: transparent;
  color: #ffffff;
}

.movie-detail {

}

.star {
 background-color: transparent;
 color: #ffffff
}
</style>