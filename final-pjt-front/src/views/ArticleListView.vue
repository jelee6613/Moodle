<template>
  <div class="container">
    <h2>커뮤니티</h2>
    
    <div class="d-flex flex-row-reverse">
      <button type="button" class="btn btn-dark">
        <router-link class="text-decoration-none text-white" :to="{ name: 'articleCreate' }">글쓰기</router-link>
      </button>
    </div>

    <table class="table table-dark table-striped table-hover">
      <thead>
        <tr class="text-center">
          <th scope="col">No</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">추천</th>
          <th scope="col">등록일</th>
        </tr>
      </thead>

      <tbody v-for="article in orderedArticles" :key="article.id">
        <tr scope="row">
          <th class="col-1 text-center">{{ article.id }}</th>
          <td class="col-7">
            <router-link class="text-decoration-none text-white" :to="{ name: 'articleDetail', params: { articlePk: article.id }}">
              {{ article.title }} [{{ article.comment_count }}]
            </router-link>
          </td>
          <td class="col-1 text-center">
            <router-link class="text-decoration-none text-white" :to="{ name: 'profile', params: { username: article.user.username }}">
              {{ article.user.username }}
            </router-link>
          </td>
          <td class="col-1 text-center">{{ article.like_count }}</td>
          <td class="col-2 text-center">{{ article.created_at | date }}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'
import moment from 'moment'

export default {
  name: 'ArticleListView',
  computed: {
    ...mapGetters(['articles']),
    orderedArticles() {
      return _.orderBy(this.articles, 'id', 'desc')
    }
  },
  methods: {
    ...mapActions(['fetchArticles'])
  },
  filters: {
    date(dateField) {
      return moment(String(dateField)).format('YYYY/MM/DD HH:mm')
    }
  },
  created() {
    this.fetchArticles()
  }
}
</script>

<style>
router-link {
  font-size: 1.2rem;
  color: #ffffff;
  text-decoration: none;
}
</style>