<template>
  <div>
    <form>
      <div v-for="idx in stepList" :key="idx" class="quiz-box">
        <div class="question-container text-center font-description mb-2">
          {{ newQuizzes[quizIndex][idx].id }}. {{ newQuizzes[quizIndex][idx].content }}
        </div>
        <div class="options-container font-description row justify-content-center">
          <input 
            type="radio" 
            class="btn-check"
            v-model="options[idx]" 
            :name="`q${idx}`" 
            :id="`q${idx}-0`" 
            :value="newQuizzes[quizIndex][idx].value_set[0].id"
            autocomplete="off" 
          />
          <label class="btn option-btn col-12 col-lg-5 align-items-center" :for="`q${idx}-0`">
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
          <label class="btn option-btn col-12 col-lg-5 align-items-center" :for="`q${idx}-1`">
            {{ newQuizzes[quizIndex][idx].value_set[1].content }}
          </label>
        </div>
      </div>
      <div class="col-8 d-grid mx-auto py-3">
        <button class="btn btn-outline-light btn-lg" v-if="quizIndex === newQuizzes.length - 1" @click.prevent="onSubmit()">결과보기</button>
        <button class="btn btn-outline-light btn-lg" v-else @click.prevent="onNext()">다음</button>
      </div>
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
      ...mapGetters(['quizzes']),
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
.quiz-box {
  margin-top: 1.5rem;
  margin-bottom: 1.5rem;
  padding: 1rem;
  /* From https://css.glass */
  /* background: rgba(229, 229, 229, 0.2);
  border-radius: 16px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(40px);
  -webkit-backdrop-filter: blur(40px);
  border: 1px solid rgba(174, 174, 174, 0.22); */
}

.question-container {

}

.options-container {

}

.option-btn {
  margin: 1rem;
  padding: 1.5rem;
  color: #ffffff;
  text-align: center;
  border-radius: 30px;
  background: #363636;
  box-shadow:  5px 5px 10px #262626,
              -5px -5px 10px #464646;
}
</style>