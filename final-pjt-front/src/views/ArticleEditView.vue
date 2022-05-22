<template>
  <div>
    <h1>Edit Article</h1>
    <article-form v-if="isArticle" :article="article" action="update"></article-form>
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