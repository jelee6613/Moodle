import drf from "@/api/drf"
import router from "@/router"
import axios from "axios"

export default ({
  state: {
    movies: [],
    movie: {},
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie
  },
  actions: {
    fetchMoviesUpdate({ commit, getters }) {
      // 관리자 권한만 TMDB API 통신 요청하기
      // POST: movies movies URL
      // 성공하면 응답으로 받은 영화 리스트를 state.movies에 저장
      // 실패하면 에러 메세지 표시
      // state.movies 초기화 후 axios 통신
      commit('SET_MOVIES', [])

      axios({
          url: drf.movies.getMovies(),
          method: 'post',
          headers: getters.authHeader
      })
        .then( res => {
          commit('SET_MOVIES', res.data)
        })
        .catch( err => console.error(err))
    },
    fetchMovies({ commit }) {
      // 영화 목록 페이지 받아오기
      // GET: movies movies URL
      // 성공하면 응답으로 받은 영화 리스트를 state.movies에 저장
      // 실패하면 에러 메세지 표시
      commit('SET_MOVIES', [])
      
      axios({
        url: drf.movies.movies(),
        method: 'get',
      })
        .then( res => {
          commit('SET_MOVIES', res.data)
        })
        .catch( err => console.error(err))
    },
    fetchMovie({ commit }, moviePk) {
      // 영화 디테일 페이지 받아오기
      // GET: movies movie URL
      // 성공하면 응답으로 받은 영화 객체를 state.movie에 저장
      // 실패하면 단순 에러일 때는 에러 메세지 표시, 404 에러일 때는 NotFound404로 이동
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get'
      })
        .then( res => {
          commit('SET_MOVIE', res.data)
        })
        .catch( err => {
          if (err.response.data === 404) {
            router.push({ name: 'NotFound'})
          } else {
            console.error(err)
          }
        })
    },
  },
})
  