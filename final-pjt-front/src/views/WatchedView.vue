<template>
  <div class="container">
    <div class="d-flex watched-list">
      <h3>{{ profile.username }}님이 관람한 영화</h3>
      <div class="d-flex">
        <div class="row watch-list-item">
          <movie-list-item
            class="col-3 mb-5"
            v-for="watchedMovie in profile.movies"
            :key="watchedMovie.pk"
            :movie="watchedMovie"
          >
          </movie-list-item>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'WatchedView',
  components: { MovieListItem },
  computed: {
    ...mapGetters(['profile'])
  }
}
</script>

<style>
.watched-list {
  flex-direction: column;
  margin: 5rem 0 ;
}

.watched-list-item {
  overflow: auto;
  scroll-snap-type: y mandatory;
}
</style>