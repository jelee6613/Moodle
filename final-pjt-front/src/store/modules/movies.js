import drf from "@/api/drf"
import router from "@/router"
import axios from "axios"

export default {
  state: {
    nowPlayings: [],
    upcomings: [],
    populars: [],
    movies: [],
    movie: {},
    quizzes: [],
  },
  getters: {
    nowPlayings: state => state.nowPlayings,
    upcomings: state => state.upcomings,
    populars: state => state.populars,
    movies: state => state.movies,
    movie: state => state.movie,
    quizzes: state => state.quizzes,
  },
  mutations: {
    SET_NOW_PLAYINGS: (state, movies) => state.nowPlayings = movies,
    SET_UPCOMINGS: (state, movies) => state.upcomings = movies,
    SET_POPULARS: (state, movies) => state.populars = movies,
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_QUIZZES: (state, quizzes) => state.quizzes = quizzes,
  },
  actions: {
    fetchMoviesSearch({ getters }, keyword) {
      // 관리자 권한만 TMDB API 통신 요청하기
      // POST: movies movies URL
      // 성공하면 응답으로 받은 영화 리스트를 state.movies에 저장
      // 실패하면 에러 메세지 표시

      axios({
          url: drf.movies.getMovies(),
          method: 'post',
          data: keyword,
          headers: getters.authHeader
      })
        .then( res => {
          if (res.status === 201) {
            alert('영화가 추가되었습니다.')
          }
        })
        .catch( err => {
          console.error(err)
        })
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
          commit('SET_NOW_PLAYINGS', res.data.now_playing)
          commit('SET_UPCOMINGS', res.data.upcoming)
          commit('SET_POPULARS', res.data.popular)

        })
        .catch( err => console.error(err))
    },
    fetchMovie({ commit, getters }, moviePk) {
      // 영화 디테일 페이지 받아오기
      // GET: movies movie URL
      // 성공하면 응답으로 받은 영화 객체를 state.movie에 저장
      // 실패하면 단순 에러일 때는 에러 메세지 표시, 404 에러일 때는 NotFound404로 이동
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.isLoggedIn?getters.authHeader:''
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
    fetchQuiz({ getters, commit }) {
      // 퀴즈 내용 받아오기
      // GET movies movieRecommendation URL
      // 성공하면 응답으로 받은 퀴즈 문항을 state.quizzes에 저장
      // 실패하면 에러 메세지 표시 
      commit('SET_MOVIE', {})

      axios({
        url: drf.movies.movieRecommendation(),
        method: 'get',
        headers: getters.authHeader
      })
        .then( res => {
          commit('SET_QUIZZES', res.data)
        })
        .catch( err => console.error(err) )
    },
    findRecommendation({ getters, commit }, results) {
      // 추천 영화 받아오기
      // POST movies movieRecommendation URL
      // 성공하면 응답으로 받은 영화를 state.movie에 저장
      // 실패하면 에러 메세지 표시
      axios({
        url: drf.movies.movieRecommendation(),
        method: 'post',
        data: results,
        headers: getters.authHeader
      })
        .then( res => {
          commit('SET_MOVIE', res.data)
        })
        .catch( err => console.error(err) )
    },
    rateMovie({ getters, commit }, { moviePk, rate }) {
      // 내가 본 영화 추가 및 별점 저장하기
      // POST movies movieRate
      axios({
        url: drf.movies.movieRate(moviePk),
        method: 'post',
        data: { rate },
        headers: getters.authHeader
      })
        .then( res => {
          commit('SET_MOVIE', res.data)
        })
        .catch( err => console.error(err) )
    }
  },
}
  