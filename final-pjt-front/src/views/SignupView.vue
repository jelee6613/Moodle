<template>
  <div>
    <h1>회원가입</h1>

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">Username: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>
      <div>
        <label for="password1">password: </label>
        <input v-model="credentials.password1" type="password" id="password1" required />
      </div>
      <div>
        <label for="password2">password check: </label>
        <input v-model="credentials.password2" type="password" id="password2" required />
      </div>
      <div>
        <button>가입하기</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'SignupView',
    data() {
      return {
        credentials : {
          username: '',
          password1: '',
          password2: ''
        }
      }
    },
    methods: {
      ...mapActions(['signup',])
    }

}
</script>

<style>

</style>