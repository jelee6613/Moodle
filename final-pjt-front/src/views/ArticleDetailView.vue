<template>
  <div>
    <h1>{{ article.title }}</h1>

    <p>
      작성자: {{ article.user.username }} | 
      작성일: {{ article.created_at | date }} |
      최종수정일: {{ article.updated_at | date }}
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
      <button v-if="article.like_users.find((user) => user.pk === currentUser.pk)" class="like-btn" @click="likeArticle(articlePk)">
        <i class="fa-solid fa-heart"></i> 
      </button>
      <button v-else class="like-btn" @click="likeArticle(articlePk)">
        <i class="fa-regular fa-heart"></i> 
      </button>
      <span>좋아요 {{ article.like_count }}개</span>
    </div>

    <hr />

    <!-- Comments -->
    <comment-list :comments="article.comment_set"></comment-list>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import CommentList from '../components/CommentList.vue'
import moment from 'moment'

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
      ...mapGetters(['article', 'isAuthor', 'currentUser']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions(['fetchArticle', 'deleteArticle', 'likeArticle']),
    },
    filters: {
      date(dateField) {
        return moment(String(dateField)).format('YYYY/MM/DD HH:mm')
      }
    },
    created() {
      this.fetchArticle(this.articlePk)
    }
}
</script>

<style>
  .like-btn {
    color: red;
    background: none;
    border: none;
  }
</style>