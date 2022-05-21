<template>
  <div>
    <h2>ArticleListView</h2>

    <div>
      <ul>
        <li v-for="article in articles" :key="article.pk">

          <router-link :to="{ name: 'articleDetail', params: {articlePk: article.pk}}">
            {{ article.title }}
          </router-link>

        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ArticleListView',
  computed: {
    ...mapGetters(['articles'])
  },
  methods: {
    ...mapActions(['fetchArticles'])
  },
  created() {
    this.fetchArticles()
  }
}
</script>

<style>

</style>