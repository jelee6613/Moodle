<template>
  <div>
    <router-link :to="{ name: 'RecommendedList'}">Recommended List</router-link>
    <quiz-form></quiz-form>
  </div>
</template>

<script>
import QuizForm from '@/components/QuizForm.vue'

export default {
  name: 'MovieRecommendationView',
  components: { QuizForm }
}
</script>

<style>

</style>