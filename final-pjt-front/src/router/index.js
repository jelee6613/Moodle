import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import SignupView from '../views/SignupView.vue'
import ProfileView from '../views/ProfileView.vue'
import WatchedView from '../views/WatchedView.vue'
import MovieListView from '../views/MovieListView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import MovieRecommendationView from '../views/MovieRecommendationView.vue'
import ArticleListView from '../views/ArticleListView.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'
import ArticleEditView from '../views/ArticleEditView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import NotFoundView from '../views/NotFoundView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/accounts/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/accounts/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/accounts/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/accounts/:username/watched',
    name: 'watched',
    component: WatchedView
  },
  {
    path: '/',
    name: 'movieList',
    component: MovieListView
  },
  {
    path: '/movies/recommendations',
    name: 'movieRecommendation',
    component: MovieRecommendationView
  },
  {
    path: '/movies/:moviePk',
    name: 'movieDetail',
    component: MovieDetailView
  },
  {
    path: '/community',
    name: 'articleList',
    component: ArticleListView
  },
  {
    path: '/community/create',
    name: 'articleCreate',
    component: ArticleCreateView
  },
  {
    path: '/community/:articlePk',
    name: 'articleDetail',
    component: ArticleDetailView
  },
  {
    path: '/community/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/404',
    name: 'NotFound',
    component: NotFoundView
  },
  {
    path: '*',
    redirect: '/404',
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
