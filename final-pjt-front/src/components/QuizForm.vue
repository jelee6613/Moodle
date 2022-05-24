<template>
  <div>
    <div v-for="quiz in newQuiz" :key="quiz.id">
      <div>
        <label :for="`quiz-${quiz.id}`">{{ quiz.question_content }}</label>
        <select name="`quiz-${quiz.id}`" id="`quiz-${quiz.id}`">{{ quiz.content }}</select>
        {{ quiz }}
      </div>
      <button v-if="quiz.id != last" @onClick.prevent="">다음</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'QuizForm',
    props: {
      newQuiz: Array,
    },
    data() {
      return {
        temp: [],
        last: this.newQuiz.length - 1
      }
    },
    computed: {
      onNext() {
        // 입력 데이터 temp에 저장
        // this.temp.push()
        return 0
      },
      onSubmit() {
        // 입력 데이터 results에 저장
        // findRecommendation
        // this.temp.push()
        this.findRecommendation(this.temp)
        return 0
      }
    },
    methods: {
      ...mapActions('findRecommendation')
    }
}
</script>

<style>

</style>