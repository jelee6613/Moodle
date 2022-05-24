<template>
  <div class="movie-item">
    <div class="card mx-2 mx-lg-3 my-1">
      <router-link
        :to="{ name: 'movieDetail', params: { moviePk: movie.id }}"
      >
      <img :src="`https://www.themoviedb.org/t/p/original${movie.poster_path}`" alt="movie poster" class="card-img">
      </router-link>
      
    </div>
  </div>
  <!-- <router-link
    :to="{ name: 'movieDetail', params: { moviePk: movie.id }}"
  >{{ movie.title }}</router-link>
  <img :src="`https://www.themoviedb.org/t/p/w300${movie.poster_path}`" alt=""> -->
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object
  },
  methods: {
  },
}
</script>

<style>
  .movie-item {
    min-width: 21%;
    scroll-snap-align: start;
  }

</style>