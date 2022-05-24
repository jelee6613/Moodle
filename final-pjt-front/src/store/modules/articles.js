import drf from '@/api/drf'
import router from '@/router'
import axios from 'axios'
import _ from 'lodash'

export default {
  state: {
    articles: [],
    article: {},
  },
  getters: {
    articles: state => state.articles,
    article: state => state.article,
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle: state => !_.isEmpty(state.article),
  },
  mutations: {
    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state, comments) => { state.article.comment_set = comments }
  },
  actions: {
    fetchArticles({ commit, getters }) {
      // GET articles articles
      axios({
        url: drf.articles.articles(),
        method: 'get',
        headers: getters.authHeader
      })
        .then( res => commit('SET_ARTICLES', res.data) )
        .catch( err => console.error(err) )
    },
    fetchArticle({ commit, getters }, articlePk) {
      // GET articles article
      axios({
        url: drf.articles.article(articlePk),
        method: 'get',
        headers: getters.authHeader
      })
        .then( res => commit('SET_ARTICLE', res.data) )
        .catch( err => {
          console.error(err)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound' })
          }
        })
    },
    createArticle({ commit, getters }, article) {
      // POST articles articles
      axios({
        url: drf.articles.articles(),
        method: 'post',
        data: article,
        headers: getters.authHeader
      })
        .then( res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'articleDetail',
            params: { articlePk: getters.article.id }
          })
        })
        .catch( err => console.error(err) )
    },
    updateArticle({ commit, getters }, { pk, title, content }) {
      // PUT articles article
      axios({
        url: drf.articles.article(pk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader
      })
        .then( res => {
          console.log(res)
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'articleDetail',
            params: { articlePk: getters.article.id }
          })
        })
        .catch( err => console.error(err) )
    },
    deleteArticle({commit, getters }, articlePk) {
      // DELETE articles article
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.article(articlePk),
          method: 'delete',
          headers: getters.authHeader
        })
          .then( () => {
            commit('SET_ARTICLE', {})
            router.push({ name: 'articleList' })
          })
          .catch( err => console.error(err) )
      }
    },
    likeArticle({ commit, getters }, articlePk) {
      // POST articles likeArticle
      axios({
        url: drf.articles.likeArticle(articlePk),
        method: 'post',
        headers: getters.authHeader
      })
        .then( res => {
          commit('SET_ARTICLE', res.data )
        })
        .catch( err => console.error(err) )
    },
    createComment({ commit, getters }, { articlePk, content }) {
      // POST articles comments
      const comment = { content }

      axios({
        url: drf.articles.comments(articlePk),
        method: 'post',
        data: comment,
        headers: getters.authHeader
      })
        .then( res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch( err => console.error(err) )
    },
    updateComment({ commit, getters }, { articlePk, commentPk, content }) {
      // PUT articles comment
      const comment = ({ content })

      axios({
        url: drf.articles.comment(articlePk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader
      })
        .then( res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch( err => console.error(err) )
    },
    deleteComment({ commit, getters }, { articlePk, commentPk }) {
      // DELETE articles comment
      axios({
        url: drf.articles.comment(articlePk, commentPk),
        method: 'delete',
        data: {},
        headers: getters.authHeader
      })
        .then( res => {
          alert('정상적으로 삭제되었습니다.')
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch( err => console.error(err) )
    }
  },
}
  