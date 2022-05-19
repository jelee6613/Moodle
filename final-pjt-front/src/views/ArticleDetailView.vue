<template>
  <div>
    <comment-list>
      <comment-list-item></comment-list-item>
      <comment-form></comment-form>
    </comment-list>
  </div>
</template>

<script>
import CommentList from '../components/CommentList.vue'
import CommentListItem from '../components/CommentListItem.vue'
import CommentForm from '../components/CommentForm.vue'


export default {
    name: 'ArticleDetailView',
    components: {
      CommentList,
      CommentListItem,
      CommentForm,
    },
}
</script>

<style>

</style>