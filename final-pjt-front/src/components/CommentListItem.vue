<template>
  <div>
    <li>
      <router-link :to="{ name: 'profile', params: { username: comment.user.username }}">
        {{ comment.user.username }}
      </router-link>

      <span v-if="isEditing">{{ payload.content }}</span>

      <span v-if="isEditing">
        <input type="text" v-model="payload.content">
        <button @click="onUpdate">수정</button>
        <button @click="switchIsEditing">취소</button>
      </span>

      <span v-if="currentUser.username === comment.user.username && !isEditing">
        <button @click="switchIsEditing">수정</button>
        <button @click="deleteComment(payload)">삭제</button>
      </span>
    </li>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

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
          commentPk: this.comment.pk,
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
      ...mapActions(['updateComment', 'createComment']),
      switchIsEditing() {
        this.isEditing = !this.isEditing
      },
      onUpdate() {
        this.updateComment(this.payload)
        this.isEditing = false
      }
    }
}
</script>

<style>

</style>