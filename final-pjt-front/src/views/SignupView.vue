<template>
  <div class="container d-flex align-items-center">
    <div class="col py-5">
      <div class="row justify-content-center">
        <div class="col-md-8 col-lg-6">
          <div>
            <!-- Text -->
            <div class="mb-5 text-center">
              <h3 class="my-2">회원가입</h3>
              <p>회원가입 후 다양한 서비스를 즐겨보세요</p>
            </div>
            <!-- Signup Form -->
            <!-- <account-error v-if="authError"></account-error> -->
            <form @submit.prevent="signup(credentials)">
              <div>
                <label class="form-label" for="username">아이디 </label>
                <input 
                  class="form-control form-control-lg" 
                  v-model="credentials.username" 
                  type="text" 
                  id="username" 
                  placeholder="username"
                  required />
                  <div v-if="authError">
                    <account-error v-if="'username' in this.authError" :errors="authError.username"></account-error>
                  </div>
              </div>
              <div class="my-4">
                <label class="form-label" for="password1">비밀번호 </label>
                <input 
                  class="form-control form-control-lg"
                  v-model="credentials.password1" 
                  type="password" 
                  id="password1" 
                  placeholder="********"
                  required />
                  <div v-if="authError">
                    <account-error v-if="'password1' in this.authError" :errors="authError.password1"></account-error>
                  </div>
              </div>
              <div class="my-4">
                <label class="form-label" for="password2">비밀번호 확인 </label>
                <input 
                  class="form-control form-control-lg"
                  v-model="credentials.password2" 
                  type="password" 
                  id="password2" 
                  placeholder="********"
                  required />
                  <div v-if="authError">
                    <account-error v-if="'password2' in this.authError" :errors="authError.password2"></account-error>
                  </div>
              </div>
              <div v-if="authError">
                <div v-for="(errors, field) in authError" :key="field">
                    <account-error v-if="!(['username', 'password1', 'password2'].includes(field))" :errors="errors"></account-error>
                </div>
              </div>
              <div class="d-grid mt-5">
                <button class="btn btn-outline-primary btn-lg mb-3">가입하기</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import AccountError from '@/components/AccountError.vue'

export default {
  name: 'SignupView',
  components: { AccountError },
  data() {
    return {
      credentials : {
        username: '',
        password1: '',
        password2: ''
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup', 'removeToken'])
  },
  created() {
    this.removeToken()
  }
}
</script>

<style>

</style>