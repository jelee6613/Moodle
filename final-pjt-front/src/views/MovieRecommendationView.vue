<template>
  <div>
    <quiz-form></quiz-form>
    <recommended-list></recommended-list>
  </div>
</template>

<script>
import QuizForm from '@/components/QuizForm.vue'
import RecommendedList from '@/components/RecommendedList.vue'

export default {
  name: 'MovieRecommendationView',
  components: { QuizForm, RecommendedList }
}
</script>

<style>

</style>