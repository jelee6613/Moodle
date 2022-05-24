<template>
  <div>
    <form action="">
      <div v-for="idx in stepList" :key="idx">
        <div class="quizBox">
          <div class="questionContainer">
            퀴즈 문항
            {{ newQuizzes[quizIndex][idx].content }}
          </div>
          <div class="optionsContainer">
            퀴즈 보기
            <input 
              type="radio" 
              class="btn-check"
              v-model="options[idx]" 
              :name="`q${idx}`" 
              :id="`q${idx}-0`" 
              :value="newQuizzes[quizIndex][idx].value_set[0].id"
              autocomplete="off" 
            />
            <label class="btn btn-outline-primary" :for="`q${idx}-0`">
              {{ newQuizzes[quizIndex][idx].value_set[0].content }}
            </label>
            <input 
              type="radio" 
              class="btn-check" 
              v-model="options[idx]" 
              :name="`q${idx}`" 
              :id="`q${idx}-1`" 
              :value="newQuizzes[quizIndex][idx].value_set[1].id"
              autocomplete="off" 
            />
            <label class="btn btn-outline-primary" :for="`q${idx}-1`">
              {{ newQuizzes[quizIndex][idx].value_set[1].content }}
            </label>
          </div>
        </div>
      </div>
      <button v-if="quizIndex === newQuizzes.length - 1" @click.prevent="onSubmit()">결과보기</button>
      <button v-else @click.prevent="onNext()">다음</button>
    </form>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'QuizForm',
    props: {
    },
    data() {
      return {
        step: 3,
        quizIndex: 0,
        temp: [],
        options: ['', '', '']
      }
    },
    computed: {
      ...mapGetters(['quizzes', 'results']),
      newQuizzes() {
        return _.chunk(this.quizzes, this.step)
      },
      start() {
        return this.quizIndex * this.step 
      },
      end() { 
        return this.start + this.step
      },
      stepList() {
        return _.range(this.step)
      }
    },
    methods: {
      ...mapActions(['findRecommendation']),
      onNext() {
        this.temp.push(...this.options)
        this.quizIndex += 1
      },
      onSubmit() {
        this.temp.push(...this.options)
        this.findRecommendation(this.temp)
      }
    }
}
</script>

<style>

</style>