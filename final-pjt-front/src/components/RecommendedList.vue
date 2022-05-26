<template>
  <div class="recommend-container">
    <div class="recommend-header text-center">
      <span>당신과 가장 비슷한 성향의 감독은 <br/>
      <strong class="text-medium">{{ movie.director }}</strong> 입니다!</span>
    </div>
    <div class="card recommnd-body">
      <img class="card-img" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="">
      <div class="recommend-overlay">
        <div class="recommend-title">
          {{ movie.title }}
        </div>
        <div class="mb-2">
          <b-form-rating
            variant="warning"
            :value="movie.average_vote"
            no-border inline show-value readonly          
            class="star"
            style="color: #000000;"
          ></b-form-rating>
        </div>
        <div class="recommend-info">
          <span v-for="genre in movieGenres" :key="genre">
            {{ genre }}
          </span> |
          <span>
            {{ movie.release_date }} 개봉
          </span>
        </div>
        <div class="recomment-text">
            {{ movie.overview }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
    name: 'RecommendedList',
    props: {
      movie: Object
    },
    computed: {
      movieGenres() {
        return JSON.parse(this.movie.genre)
      }
    }
}
</script>

<style>
.recommend-container {
  
}

.recommend-header {
  font-family: LeferiPoint-WhiteObliqueA;
  font-size: 1.6rem;
  margin: 2rem 0;
}

.recommnd-body {
  background-color: #272727;
  color: #ffffff;
  border-radius: 30px;
}

.recommend-overlay {
  position: absolute;
  bottom: calc(-15%);
  padding: 2rem;
  color: #000000;
  border-bottom-left-radius: calc(0.375rem - 1px);
  border-bottom-right-radius: calc(0.375rem - 1px);
  /* From https://css.glass */
  background: rgba(255, 255, 255, 0.4);
  border-top-left-radius: 40px;
  border-top-right-radius: 40px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.22);
}

.recommend-title {
  font-family: SuseongDotum;
  font-size: 1.8rem;
  margin-bottom: 0.2rem;
}

.recommend-info {
  font-family: LeferiPoint-WhiteObliqueA;
  font-size: 1rem;
  margin-bottom: 1rem;
}

.recomment-text {
  font-family: LeferiPoint-WhiteObliqueA;
  font-size: 1.2rem;
}
</style>