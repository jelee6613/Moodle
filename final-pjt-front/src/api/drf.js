const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMUNITY = 'community/'

export default {
    accounts: {
        login: () => HOST + ACCOUNTS + 'login/',
        logout: () => HOST + ACCOUNTS + 'logout/',
        signup: () => HOST + ACCOUNTS + 'signup/',
        currentUserInfo: () => HOST + ACCOUNTS + 'user/',
        profile: username => HOST + ACCOUNTS + 'profile/' + username,
        follow: username => HOST + ACCOUNTS + 'profile/' + username + '/follow/',
        watchedMovie: username => HOST + ACCOUNTS + username + '/watched/'
    },
    movies: {
        movies: () => HOST,
        movie: moviePk => HOST + MOVIES + moviePk,
        movieRecommendation: () => HOST + MOVIES + 'recommendations/',
        watchedMovie: (username, moviePk) => HOST + MOVIES + username + '/watched/' + moviePk,
        movieRate: (username, moviePk) => HOST + MOVIES + username + '/watched/' + moviePk + '/rate/'
    },
    articles: {
        articles: () => HOST + COMMUNITY,
        article: articlePk => HOST + COMMUNITY + articlePk,
        comments: articlePk => HOST + COMMUNITY + articlePk + '/comment/',
        comment: (articlePk, commentPk) => HOST + COMMUNITY + `${articlePk}/` + 'comment/' + commentPk,
        likeArticle: articlePk => HOST + COMMUNITY + articlePk + '/like/'
    }
}