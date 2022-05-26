<template>
  <div class="container d-flex align-items-center">
    <div class="col py-5">
      <div class="row justify-content-center">
        <div class="col-md-8 col-lg-6">
          <div class="mb-5 text-center">  
            <h3 class="my-1">
              게시글 수정
            </h3>
          </div>
          <article-form v-if="isArticle" :article="article" action="update"></article-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import ArticleForm from '../components/ArticleForm.vue'

export default {
    name: 'ArticleEditView',
    components: { ArticleForm },
    computed: {
      ...mapGetters(['article', 'isArticle'])
    },
    methods: {
      ...mapActions(['fetchArticle'])
    },
    created() {
      this.fetchArticle(this.$route.params.articlePk)
    }
}
</script>

<style>

</style>