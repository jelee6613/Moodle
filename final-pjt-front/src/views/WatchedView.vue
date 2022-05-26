<template>
  <div class="container">
    <div class="col">
      <div class="row">
        <h3>{{ profile.username }}님이 관람한 영화</h3>
        <div class="col-4"></div>
          <movie-list-item
            v-for="watchedMovie in profile.movies"
            :key="watchedMovie.pk"
            :movie="watchedMovie"
          >
          </movie-list-item>
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

</style>