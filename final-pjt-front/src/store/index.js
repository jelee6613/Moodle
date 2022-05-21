import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

import accounts from './modules/accounts'
import movies from './modules/movies'
import articles from './modules/articles'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  modules: {
    accounts,
    movies,
    articles
  }
})
