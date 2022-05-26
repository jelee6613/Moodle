<template>
  <div class="comment-item mb-4">
    <div class="comment-item-header d-flex justify-content-between mb-3">
      <div>
        <router-link :to="{ name: 'profile', params: { username: comment.user.username }}">
          <strong>{{ comment.user.username }}</strong>
        </router-link>&nbsp;&nbsp;
        <span class="comment-info">{{ comment.created_at | date }} 작성 | {{ comment.updated_at | date}} 수정</span>
      </div>

      <div v-if="currentUser.username === comment.user.username && !isEditing">
        <button @click.prevent="switchIsEditing">
          <i class="fa-regular fa-pen-to-square"></i>수정
        </button>
        <button @click="deleteComment(payload)">
          <i class="fa-regular fa-trash-can"></i>삭제
        </button>
      </div>
    </div>

    <div class="comment-item-body">
      <span v-if="isEditing">
        <input class="form-control" type="text" v-model="payload.content">
        <button @click.prevent="onUpdate">완료</button>
        <button @click="switchIsEditing">취소</button>
      </span>
      <div v-else class="comment-item-content">
        <span>{{ comment.content }}</span>
      </div>
    
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import moment from 'moment'

export default {
    name: 'CommentListItem',
    props: {
      comment: Object,
    },
    data() {
      return {
        isEditing: false,
        payload: {
          articlePk: this.comment.article,
          commentPk: this.comment.id,
          content: this.comment.content
        }
      }
    },
    computed: {
      ...mapGetters(['currentUser']),
      // user() {
      //   return JSON.parse(JSON.stringify(this.currentUser))
      // }
    },
    methods: {
      ...mapActions(['updateComment', 'createComment', 'deleteComment']),
      switchIsEditing() {
        this.isEditing = !this.isEditing
      },
      onUpdate() {
        this.updateComment(this.payload)
        this.isEditing = false
      }
    },
    filters: {
      date(dateField) {
        return moment(String(dateField)).format('YYYY/MM/DD HH:mm')
      }
    },

}
</script>

<style>
  .comment-item {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 0.8rem 1rem;
    border-radius: 7px;
  }

  .comment-item button {
    color: #ffffff;
    background: none;
    border: none;
    font-size: 0.85rem;
  }

  .comment-item button:hover {
    color: #90b8f8;
    text-decoration: underline;
  }
  
  .comment-item-header {

  }

  .comment-info {
    color: #cdcdcd;
    font-size: 0.9rem;
  }

  .comment-item-body {
    word-wrap: break-word;
  }
</style>