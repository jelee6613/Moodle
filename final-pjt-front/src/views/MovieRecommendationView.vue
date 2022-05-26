<template>
  <div class="container">
    <span>Movie Recommendation</span>
    <div v-if="isMovieEmpty">
      <quiz-form></quiz-form>
    </div>
    <div v-else>
      <recommended-list :movie="movie">{{ movie }}</recommended-list>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'

import QuizForm from '@/components/QuizForm.vue'
import RecommendedList from '@/components/RecommendedList.vue'

export default {
  name: 'MovieRecommendationView',
  components: { QuizForm, RecommendedList },
  computed: {
    ...mapGetters(['movie']),
    isMovieEmpty() {
      return _.isEmpty(this.movie)
    }
  },
  methods: {
    ...mapActions(['fetchQuiz']),
  },
  created() {
    this.fetchQuiz()
  }
}
</script>

<style>

</style>