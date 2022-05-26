<template>
  <div class="container">
    <div class="mt-3 mb-5" v-if="currentUser.is_superuser">
      <form @submit.prevent="onSubmit" class="row justify-content-center">
        <div class="col-11 col-md-8 col-lg-6">
          <label class="visually-hidden" for="keyword"></label>
          <div class="input-group">
            <div @click.prevent="onSubmit" class="input-group-text"><i class="fa-solid fa-magnifying-glass"></i></div>
            <input type="text" class="form-control form-control-lg" v-model="keyword" id="keyword" placeholder="검색어로 영화를 추가하세요." autocomplete="off" required>
          </div>
        </div>
      </form>
      <!-- <button @click="fetchMoviesUpdate">TMDB API 불러오기</button> -->
    </div>

    <div class="d-flex movie-list">
      <h3>현재상영작</h3>
      <div class="d-flex movie-list-item mt-3">
        <movie-list-item
          v-for="nowPlaying in nowPlayings"
          :key="nowPlaying.id"
          :movie="nowPlaying"
        ></movie-list-item>
      </div>
    </div>
    <div class="d-flex movie-list">
      <h3>인기작</h3>
      <div class="d-flex movie-list-item mt-3">
        <movie-list-item
          v-for="popular in populars"
          :key="popular.id"
          :movie="popular"
        ></movie-list-item>
      </div>
    </div>
    <div class="d-flex movie-list">
      <h3>상영예정작</h3>
      <div class="d-flex movie-list-item mt-3">
        <movie-list-item
          v-for="upcoming in upcomings"
          :key="upcoming.id"
          :movie="upcoming"
        ></movie-list-item>
      </div>
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
    ...mapGetters(['currentUser', 'nowPlayings', 'upcomings', 'populars'])
  },
  methods: {
    ...mapActions(['fetchMoviesSearch', 'fetchMovies']),
    onSubmit() {
      this.fetchMoviesSearch(this.keyword)
      this.keyword = ''
    }
  },
  created() {
    this.fetchMovies()
  },
}
</script>

<style>
.input-group {
  border: 1px solid #ced4da;
  border-radius: 0.375rem;
}
.input-group > .input-group-text {
  background-color: transparent !important;
  color: #ffffff;
  border: none;
  cursor: pointer;
}
.input-group > .form-control {
  border: none;
}
textarea.form-control,
textarea.form-control:-webkit-autofill,
textarea.form-control:-webkit-autofill:hover,
textarea.form-control:-webkit-autofill:focus,
textarea.form-control:-webkit-autofill:active,
input.form-control,
input.form-control:-webkit-autofill,
input.form-control:-webkit-autofill:hover,
input.form-control:-webkit-autofill:focus,
input.form-control:-webkit-autofill:active {
  background-image: none !important;
  background-color: #26282B !important;
  color: #ffffff !important;
}

.movie-list {
  flex-direction: column;
  margin: 5rem 0 ;
}

.movie-list h3 {
  font-family: IBMPlexSansKR-Bold;
  font-size: 2rem;
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