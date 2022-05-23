<template>
  <div>
    <ul>
      <comment-list-item
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
      ></comment-list-item>
    </ul>

    <comment-form></comment-form>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentForm from '@/components/CommentForm.vue'

export default {
    name: 'CommentList',
    components: { CommentListItem, CommentForm },
    props: {
      comments: Array
    }
}
</script>

<style>

</style>