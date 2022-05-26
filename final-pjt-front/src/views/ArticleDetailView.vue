<template>
  <div class="container d-flex align-items-center">
    <div class="col py-5">
      <div class="row justify-content-center">
        <div class="col-md-10 col-lg-8">
          <!-- Back Button -->
          <div class="mb-4">
            <router-link :to="{ name: 'articleList' }">
              <button class="btn btn-outline-light btn-sm">
                <i class="fa-solid fa-chevron-left"></i>&nbsp;&nbsp;글 목록
              </button>
            </router-link>
          </div>
          <!-- Article -->
          <div>
            <div class="article-title my-4">
              <h2>{{ article.title }}</h2>
            </div>
            <div class="article-info mb-5 d-flex justify-content-between">
              <div>
                <router-link :to="{ name: 'profile', params: { username: article.user.username }}">
                  {{ article.user.username }}
                </router-link>&nbsp;|&nbsp;
                {{ article.created_at | date }} 작성&nbsp;|&nbsp;
                {{ article.updated_at | date }} 수정&nbsp;|&nbsp;
                <i class="fa-regular fa-thumbs-up"></i> {{ article.like_count }}&nbsp;
                <i class="fa-regular fa-message"></i> {{ article.comment_set.length }}
              </div>
              <div>
                <router-link v-if="isAuthor" :to="{ name: 'articleEdit', params: { articlePk }}">
                  <i class="fa-regular fa-pen-to-square"></i> 수정
                </router-link>&nbsp;
                <a v-if="isAuthor" class="delete-btn">
                  <button @click="deleteArticle(articlePk)">
                    <i class="fa-regular fa-trash-can"></i> 삭제 
                  </button>
                </a>
              </div>
            </div>
            <div class="article-content">
              <p>{{ article.content }}</p>
            </div>
          </div>

          <!-- Article Like -->
          <div class="article-like">
            <button v-if="article.like_users.find((user) => user.pk === currentUser.pk)" class="like-btn" @click="likeArticle(articlePk)">
              <!-- <i class="fa-solid fa-heart"></i>  -->
              <i class="fa-solid fa-thumbs-up"></i> <span>좋아요 취소</span>
            </button>
            <button v-else class="like-btn" @click="likeArticle(articlePk)">
              <!-- <i class="fa-regular fa-heart"></i>  -->
              <i class="fa-regular fa-thumbs-up"></i> <span>좋아요</span>
            </button>
          </div>
          <hr />
          <!-- Comments -->
          <comment-list :comments="article.comment_set"></comment-list>
        </div>
      </div>
    </div>




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
  .article-title {

  }

  .article-info {
    color: #cdcdcd;
    font-size: 0.9rem;
  }

  .delete-btn button {
    color: #ffffff;
    background: none;
    border: none;
  }

  .delete-btn button:hover {
    color: #90b8f8;
    text-decoration: underline;
  }

  .article-content {
    white-space: pre-wrap;
  }

  .article-like button {
    color: #ffffff;
    background: none;
    border: none;
  }
</style>