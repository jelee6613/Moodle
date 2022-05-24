<template>
  <div>
    Movie Recommendation
    {{ newQuizzes }}
    <quiz-form
      v-for="newQuiz in newQuizzes"
      :key="newQuiz.id"
      :newQuiz="newQuiz"
    ></quiz-form>
    <recommended-list :movie="movie"></recommended-list>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'

import QuizForm from '@/components/QuizForm.vue'
import RecommendedList from '@/components/RecommendedList.vue'

export default {
  name: 'MovieRecommendationView',
  components: { QuizForm, RecommendedList },
  data() {
    return {
      step: 3,
    }
  },
  computed: {
    ...mapGetters(['quizzes', 'movie']),
    newQuizzes() {
      return _.chunk(this.quizzes, this.step)
    },
  },
  methods: {
    ...mapActions(['fetchQuiz', 'findRecommendation']),
  },
  create() {
    this.fetchQuiz()
  }
}
</script>

<style>

</style>