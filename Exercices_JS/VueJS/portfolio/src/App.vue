<template>
  <div class="container"
      :style="{background: `#2f7b92 url(${setBg})`}"
      @mousemove="xCoords"
      @touchstart="detectUserTouch"
      >

    <div class="set0"
      :style="{background: `url(${setBg})`, width: navWidth.w0}" >
        <div class="info">
    </div>
    </div>

    <Nav class="set1"
      :style="{width: navWidth.w1}" />

    <NavSec class="set2"
      :class="{ fadeIn: navLevel == 1 || navShow, fadeOut: navLevel >= 2 && !navShow }"
      :style="{width: navWidth.w2}"
      :v-if="navLevel > 0"
      @click="setRouter" />
    <!-- {{ navWidth }} -->

    <!-- Content insert point -->
    <router-view class="insertPoint"
        :style="{left: specs.xPos}" />
        <!-- XPOS: {{ specs.xPos }} - LEVEL {{ navLevel }} - TARGET: {{ target }} - Section: {{ navSection }} -->
    <!-- Content insert point -->
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex';
import Nav from '@/components/Nav.vue';
import NavSec from '@/components/NavSec.vue';

export default {
  name: 'App',
  components: {
    Nav, NavSec
  },
  computed: {
    ...mapState(["USER_TOUCH",'navLevel','navSection','navWidth','navShow','specs','target']),
    ...mapGetters(['setBg']),
  },
  methods: {
    ...mapActions(['detectUserTouch','xCoords','setRouter']),
  }
}
</script>


<style lang="scss" >
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css");

body {
  margin: 0;
  padding: 0;
}

// Transitions //
.fadeIn{
  opacity: 1;
}
.fadeOut {
  opacity: 0;
}

.translateOut {
  transform: translateX(-100px);
  opacity: 0;
}
.translateIn {
  transform: translateX(0px);
  opacity: 1;
}

// Content //
.container {
  display: flex;
  justify-content: flex-start;
  background: no-repeat center fixed;
  background-size: cover;
  height: 100%;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}

a {
  color: white;
  text-decoration: none;
  &:hover {
    color: goldenrod;
  }
  &.router-link-exact-active {
      color: goldenrod;
      font-weight: 800;
    }
}

.set0,
.set1,
.set2 {
  height: 100vh;
  transition: all 1s;
  background: black;
  color: white;
}


.set0 {
  // flex-shrink: 10;
  background-size: cover;
  filter: blur(8px);
  -webkit-filter: blur(3px);
  opacity: 1;
}

.set1 {
  display: flex;
  flex-direction: column;
  z-index: 2;
}

.set2 {
  display: flex;
  background: rgba(0,0,0,.6);
  z-index: 2;
}

.insertPoint {
  flex-shrink: 1;
  position: absolute;
  left: 0px;
  // left: var(--router-x-pos);
  transition: 1s;
  transition-delay: .5s;
  z-index: 0;
}

@media (max-width: 600px) {
  // .container {
  //   flex-direction: column;
  // }
  .set0 { display: none;}
}

</style>
