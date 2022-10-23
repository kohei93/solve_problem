<template>
    <myHeader />
    <div>
    <h2>過去問題実習</h2>
    <button @click="moveNextScreen">第三種電気主任技術者試験 法規</button>
    </div>
    <myFooter />
</template>

<script>
import myHeader from './myHeader.vue'
import myFooter from './myFooter.vue'
// import { useRouter } from 'vue-router'
export default {
  name: 'home',
  components: {
    myHeader,
    myFooter
  },
  methods: {
    moveNextScreen: function () {
      this.$router.push({ path: '/ap/' })
    }
  }
}
</script>
