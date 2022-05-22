<template>
  <div>
    <form @submit.prevent="onSubmit">
      <label for="comment">댓글: </label>
      <input type="text" v-model="content" id="comment" required />
      <button>작성</button>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'CommentForm',
    data(){
      return {
        content: ''
      }
    },
    computed: {
      ...mapGetters(['article']),
    },
    methods: {
      ...mapActions(['createComment']),
      onSubmit() {
        this.createComment({ articlePk: this.article.pk, content: this.content })
        this.content = ''
      }
    }
}
</script>

<style>

</style>