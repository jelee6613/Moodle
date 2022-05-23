<template>
  <div class="invalid-feedback d-block">
    <span v-for="(error, idx) in errors" :key="idx">
      {{ error }}
    </span>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'AccountError',
  props: {
    errors: Array
  },
  computed: {
    ...mapGetters(['authError',])
  },
}
</script>

<style>

</style>