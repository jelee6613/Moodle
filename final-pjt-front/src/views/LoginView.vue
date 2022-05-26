<template>
  <div class="container d-flex align-items-center">
    <div class="col py-5">
      <div class="row justify-content-center">
        <div class="col-md-8 col-lg-6">
          <div>
            <!-- Text -->
            <div class="mb-5 text-center">
              <h3 class="my-2">로그인</h3>
              <p>로그인 후 다양한 서비스를 즐겨보세요</p>
            </div>
            <!-- Login Form -->
            <form @submit.prevent="login(credentials)">
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
                <label class="form-label" for="password">비밀번호 </label>
                <input 
                  class="form-control form-control-lg"
                  v-model="credentials.password" 
                  type="password" 
                  id="password" 
                  placeholder="********"
                  required />
                  <div v-if="authError">
                    <account-error v-if="'password' in this.authError" :errors="authError.password"></account-error>
                  </div>
              </div>
              <div v-if="authError">
                <div v-for="(errors, field) in authError" :key="field">
                    <account-error v-if="!(['username', 'password'].includes(field))" :errors="errors"></account-error>
                </div>
              </div>
              <div class="d-grid mt-5 text-center">
                <button class="btn btn-outline-primary btn-lg mb-3">로그인</button>
                <span class="text-small">
                  처음이신가요? <router-link class="link" :to="{ name: 'signup' }">회원가입</router-link>
                </span>
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
    name: 'LoginView',
    components: { AccountError },
    data() {
      return {
        credentials : {
          username: '',
          password: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login', 'removeToken'])
    },
    created() {
      this.removeToken()
    }
}
</script>

<style>
.text-small > .link {
  margin-left: 0.4rem;
  text-decoration: underline;
}

.text-small > .link:hover {
  color: #90b8f8;
}
</style>