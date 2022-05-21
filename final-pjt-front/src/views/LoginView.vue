<template>
  <div>
    <h1>로그인</h1>

    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">Username: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>
      <div>
        <label for="password">password: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>
      <div>
        <button>로그인</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'LoginView',
        data() {
      return {
        credentials : {
          username: '',
          password: '',
        }
      }
    },
    methods: {
      ...mapActions(['login',])
    }
}
</script>

<style>

</style>