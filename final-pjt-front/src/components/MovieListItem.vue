<template>
  <div>
    <router-link
      :to="{ name: 'movieDetail', params: { moviePk: movie.id }}"
    >{{ movie.title }}</router-link>
    {{ movie.poster_path }}
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

</style>