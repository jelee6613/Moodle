import drf from '@/api/drf'
import router from '@/router'
import axios from 'axios'
import _ from 'lodash'

export default ({
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
    SET_ARTICLE_COMMENTS: (state, comments) => { state.article.comments = comments }
  },
  actions: {
    fetchArticles({ commit, getters }) {
      // GET articles articles
      axios({
        url: drf.articles.articles,
        method: 'get',
        headers: getters.authHeader
      })
        .then( res => commit('SET_ARTICLES', res.data) )
        .catch( err => console.error(err) )
    },
    fetchArticle({ commit, getters }) {
      // GET articles article
      axios({
        url: drf.articles.article,
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
  },
})
  