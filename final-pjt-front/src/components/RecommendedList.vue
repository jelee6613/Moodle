<template>
  <div>
    Recommended Movie
    <div>
      {{ movie }}
    </div>
  </div>
</template>

<script>

export default {
    name: 'RecommendedList',
    props: {
      movie: Object
    },
}
</script>

<style>

</style>