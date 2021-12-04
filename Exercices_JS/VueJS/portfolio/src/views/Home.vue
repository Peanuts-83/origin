<template>
  <div class="home">
    HOME
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  data() {
    return {
      // sayHello: ''
    }
  },
  components: {
    // HelloWorld
  },
  computed: {
    ...mapState({
      sayHello: 'sayHello',
    })
  }
}
</script>
