<template>
  <div class="container">
    <div class="col py-5">
      <div class="row justify-content-center">
        <div class="col-10 col-lg-8">
          <div>
            <div class="mb-5 text-center">
              <h1 class="font-bold mb-3"><i class="fa-solid fa-film"></i> 영화 추천해드려요!</h1>
              <p class="font-description">
                오늘도 무슨 영화를 볼까 고민하는 당신! 우리가 대신 골라드릴게요.<br/>
                문제를 읽고 자신에 해당되는 보기를 고르면,<br/> 
                당신과 가장 닮아있는 감독의 영화 중 취향에 딱 맞는 영화를 추천해드려요!
              </p>
            </div>
            <hr />
            <!-- Quiz Form -->
            <div v-if="isMovieEmpty">
              <quiz-form></quiz-form>
            </div>
            <!-- Recommended List -->
            <div v-else>
              <recommended-list :movie="movie">{{ movie }}</recommended-list>
            </div>
          </div>
        </div>
      </div>
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
    ...mapGetters(['movie', 'isLoggedIn']),
    isMovieEmpty() {
      return _.isEmpty(this.movie)
    }
  },
  methods: {
    ...mapActions(['fetchQuiz']),
  },
  created() {
    if (!this.isLoggedIn) {
      alert('로그인이 필요합니다.')
      this.$router.push({ name: 'login'})
    } else {
      this.fetchQuiz()
    }
  }
}
</script>

<style>

</style>