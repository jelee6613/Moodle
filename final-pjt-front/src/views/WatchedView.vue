<template>
  <div>
    <h2>WatchedView</h2>
    <h3>관람한 영화</h3>
    <movie-list-item
      v-for="watchedMovie in profile.movies"
      :key="watchedMovie.pk"
      :movie="watchedMovie"
    >
    </movie-list-item>
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