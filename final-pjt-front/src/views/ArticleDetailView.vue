<template>
  <div>
    <h1>{{ article.title }}</h1>

    <p>
      작성자: {{ article.user }} | 
      작성일: {{ article.created_at }} |
      최종수정일: {{ article.updated_at }}
    </p>

    <p>{{ article.content }}</p>

    <!-- Article Edit/Delete -->
    <div v-if="isAuthor">
      <router-link :to="{ name: 'articleEdit', params: { articlePk }}">
        <button>수정</button>
      </router-link>
      |
      <button @click="deleteArticle(articlePk)">삭제</button>
    </div>

    <!-- Article Like -->
    <div>
      좋아요: {{ article.like_count }}
      <button @click="likeArticle(articlePk)">좋아요</button>
    </div>

    <hr />

    <!-- Comments -->
    <comment-list :comments="article.comments"></comment-list>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import CommentList from '../components/CommentList.vue'

export default {
    name: 'ArticleDetailView',
    components: {
      CommentList,
    },
    data() {
      return {
        articlePk: this.$route.params.articlePk
      }
    },
    computed: {
      ...mapGetters(['article', 'isAuthor']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions(['fetchArticle', 'deleteArticle', 'likeArticle']),
    },
    created() {
      this.fetchArticle(this.articlePk)
    }
}
</script>

<style>

</style>