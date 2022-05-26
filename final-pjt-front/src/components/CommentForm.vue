<template>
  <div>
    <label class="form-label" for="comment"></label>
    <form class="input-group" @submit.prevent="onSubmit">
      <textarea class="form-control form-control-lg" type="text" v-model="content" id="comment" required />
      <button class="btn btn-outline-light comment-btn">작성</button>
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
        this.createComment({ articlePk: this.article.id, content: this.content })
        this.content = ''
      }
    }
}
</script>

<style>

.input-group > .form-control {
  min-height: calc(1.5rem + 2rem + 2px) !important;
}

.comment-btn {
  border-top: none;
  border-bottom: none;
  border-right: none;
  border-left: #ced4da solid 1px;
}
</style>