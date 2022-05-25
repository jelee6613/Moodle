import drf from "@/api/drf"
import router from "@/router"
import axios from "axios"

export default {
  state: {
    token: '',
    currentUser: {},
    profile: {},
    authError: null,
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`})
  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_CURRENT_USER: (state, user) => state.currentUser = user
  },
  actions: {
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },
    removeToken({ commit }) {
      commit('SET_TOKEN', '')
      commit('SET_AUTH_ERROR', null)
      localStorage.removeItem('vuex')
      localStorage.setItem('token', '')
    },
    signup({ commit, dispatch }, credentials) {
      // 회원가입
      // POST: accounts signup
      // 성공하면 응답 토큰 저장, 현재 사용자 정보 받고 메인 페이지 이동
      // 실패하면 에러 메세지 표시
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials,
      })
        .then( res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'movieList' })
        })
        .catch( err => {
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },
    login({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials,
      })
        .then( res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'movieList' })
        })
        .catch( err => {
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },
    logout({ commit, getters, dispatch }) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        headers: getters.authHeader
      })
        .then( () => {
          dispatch('removeToken')
          commit('SET_CURRENT_USER', {})
          alert('로그아웃 되었습니다.')
          router.push({ name: 'movieList' })
        })
        .catch( err => {
          console.error(err.response.data)
        })
    },
    fetchCurrentUser({ commit, getters, dispatch }) {
      // GET accounts currentUserInfo
      // 성공하면 state.currentUser에 저장
      // 실패하면 기존 토큰 삭제, LoginView 이동
      if (getters.isLoggedIn){
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader
        })
          .then( res => {
            // const user = JSON.stringify(res.data)
            commit('SET_CURRENT_USER', res.data)
          })
          .catch( err => {
            if (err.response.data === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },
    fetchProfile({ commit, getters, dispatch }, username) {
      // 프로필페이지
      // GET accounts profile
      if (getters.isLoggedIn){
        axios({
          url: drf.accounts.profile(username),
          method: 'get',
          headers: getters.authHeader
        })
          .then( res => {
            commit('SET_PROFILE', res.data)
          })
          .catch( err => {
            if (err.response.data === 401) {
              dispatch('removieToken')
              router.push({ name: 'login' })
            }
          })
      }
    },
    follow({ commit, getters }, username) {
      // POST accounts follow
      axios({
        url: drf.accounts.follow(username),
        method: 'post',
        headers: getters.authHeader
      })
        .then( res => {
          commit('SET_PROFILE', res.data)
        })
        .catch( err => console.error(err) )
    }
  },
}
  