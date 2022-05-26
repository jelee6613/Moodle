<template>
  <div class="movie-item">
    <div class="card movie-card mx-2 mx-lg-3 my-1">
      <router-link
        :to="{ name: 'movieDetail', params: { moviePk: movie.id }}"
      >
        <img :src="`https://www.themoviedb.org/t/p/original${movie.poster_path}`" alt="movie poster" class="card-img movie-card-img">
      </router-link>
      <div class="card-overlay d-flex justify-content-center align-items-center text-center">
        <div class="card-overlay-text">
          <router-link
            :to="{ name: 'movieDetail', params: { moviePk: movie.id }}"
          >{{ movie.title }}
          </router-link>
        </div>
      </div>
    </div>
  </div>
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
    max-width: 21%;
    scroll-snap-align: start;
  }

  .movie-card {
    position: relative;
    overflow: hidden;
  }

  .movie-card-img {
    max-width: 100%;
  }

  .card-overlay {
    position: absolute;
    width: 100%;
    padding: 1rem;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.7);
    -moz-transition: top 0.3s, right 0.3s, bottom 0.3s, left 0.3s;
    -webkit-transition: top 0.3s, right 0.3s, bottom 0.3s, left 0.3s;
    transition: top 0.3s, right 0.3s, bottom 0.3s, left 0.3s;
    overflow: hidden;
  }

  .card-overlay {
    top: 100%;
  }

  .movie-card:hover .card-overlay {
    top: 0;
  }
  
  .card-overlay-text {
    color: #ffffff;
    font-family: SuseongDotum;
    font-weight: 200;
    font-size: 1rem;
  }
</style>