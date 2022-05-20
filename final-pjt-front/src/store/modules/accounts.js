export default ({
  state: {
    currentUser: {},
    profile: {},
    authError: null,
  },
  getters: {
    isSuperUser: state => state.currentUser.is_superuser,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError
  },
  mutations: {},
  actions: {},
})
  