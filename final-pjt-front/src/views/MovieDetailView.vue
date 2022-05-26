<template>
  <div class="movie-detail">
    <img class="img-fluid" :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`" alt="">
    <div class="container-lg">
      <div class="movie-detail-info">
        <div class="col-10 col-lg-7">
          <div class="movie-detail-box">
            <div class="mb-3 align-items-end">
              <span class="font-bold">{{ movie.title }}</span><br/>
              <b-form-rating
                variant="warning"
                :value="movieRate"
                no-border inline show-value readonly          
                class="star ml-4"
              ></b-form-rating>
            </div>
            <hr />
            <div class="font-description my-4">
              {{ movie.overview }}
            </div>
            <div class="font-description movie-detail-item">
              <span class="text-small">
                감독&nbsp;
              </span>
              <span>
                {{ movie.director }}
              </span>
            </div>
            <div class="font-description movie-detail-item">
              <span class="text-small">
                장르&nbsp;
              </span>
              <span v-for="genre in movieGenres" :key="genre">
                {{ genre }}&nbsp;
              </span>
            </div>
            <div class="font-description movie-detail-item">
              <span class="text-small">
                개봉일&nbsp;
              </span>
              <span>
                {{ movie.release_date }}
              </span>
            </div>
            <div class="d-flex align-items-center mt-3">
              <span class="text-small">
                내 평점&nbsp;
              </span>
              <div class="star-box">
                <b-form-rating
                  id="rating-lg-no-border rating-inline"
                  v-if="isLoggedIn"
                  @change="onRate()"
                  v-model="value.rate"
                  :value="value.rate"
                  variant="danger"
                  no-border inline show-value show-clear
                  class="star"
                  size="lg"
                ></b-form-rating>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { BFormRating } from 'bootstrap-vue'

export default {
  name: 'MovieDetailView',
  data() {
    return {
      moviePk: this.$route.params.moviePk,
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
    },
    value() {
      return {
        moviePk: this.$route.params.moviePk,
        rate: this.movie.rate?this.movie.rate:null
      }
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
.img-fluid {
  width: 100%;
  opacity: 0.4;
  position: absolute;
  top: 0;
  height: 100%;
  background: #aeaeae;
  /* opacity: 0.5; */
}

.form-control:focus {
  background-color: transparent;
  color: #ffffff;
}

.movie-detail {

}

.movie-detail-box {

}

.movie-detail-info {
  /* z-index: 99; */
  position: absolute;
  bottom: 70px;
}

.movie-detail-item {
  display: inline-block;
  border-bottom: #aaaaaa solid 1px;
  /* border-radius: 50px; */
  padding: 0.5rem 1.6rem;
  margin-right: 2rem;
}

.star-box {
}

.star {
 background-color: transparent;
 color: #ffffff;
}
</style>