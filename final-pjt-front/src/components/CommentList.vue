<template>
  <div>
    <!-- <div class="col">
      <div class="row p-3"> -->
        <comment-list-item
          v-for="comment in comments"
          :key="comment.id"
          :comment="comment"
        ></comment-list-item>
        <comment-form></comment-form>
      <!-- </div> -->
    <!-- </div> -->
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