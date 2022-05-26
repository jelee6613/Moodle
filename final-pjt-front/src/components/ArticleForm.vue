<template>
  <div>
    <form @submit.prevent="onSubmit" enctype="multipart/form-data">
      <div class="my-4">
        <label class="form-label" for="title">글 제목</label>
        <input 
          class="form-control form-control-lg"
          v-model="newArticle.title" 
          type="text" 
          id="title" 
          required />
      </div>
      <div class="my-4">
        <label class="form-label" for="content">글 내용</label>
        <textarea 
          class="form-control form-control-lg"
          v-model="newArticle.content" 
          type="text" 
          id="content"
          required />
      </div>
      <div class="d-grid mt-4">
        <button class="btn btn-outline-primary btn-lg mb-3">작성완료</button>
      </div>
    </form>

  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ArticleForm',
  props: {
    article: Object,
    action: String,
  },
  data() {
    return {
      newArticle: {
        title: this.article.title,
        content: this.article.content,
      }
    }
  },
  methods: {
    ...mapActions(['createArticle', 'updateArticle']),
    onSubmit() {
      if (this.action === 'create') {
        this.createArticle(this.newArticle)
      } else if (this.action === 'update') {
        const payload = {
          pk: this.article.id,
          ...this.newArticle          
        }
        this.updateArticle(payload)
      }
    }
  }
}
</script>

<style>
textarea.form-control {
  min-height: calc(1.5rem + 15rem + 2px) !important;
}
</style>