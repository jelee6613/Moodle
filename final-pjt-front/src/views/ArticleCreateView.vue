<template>
  <div class="container d-flex align-items-center">
    <div class="col py-5">
      <div class="row justify-content-center">
        <div class="col-md-8 col-lg-6">
          <div class="mb-5 text-center">
            <h3 class="my-1">
              게시글 작성
            </h3>
          </div>
          <article-form :article="article" action="create"></article-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'

export default {
    name: 'ArticleCreateView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          pk: null,
          title: '',
          content: ''
        }
      }
    }
}
</script>

<style>

</style>