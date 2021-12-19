<template>
  <div class="container"
      :style="{'--bg-img': bgImg}"
      @mousemove="xCoords"
      @touchstart="detectUserTouch"
      >

    <div class="set0"
      :style="{width: navWidth.w0}" >
        <div class="info">
    </div>
    </div>

    <Nav class="set1"
      :style="{width: navWidth.w1}" />

    <NavSec class="set2"
      :class="{ translateIn: navLevel == 1 || navShow, translateOut: navLevel >= 2 && !navShow }"
      :style="{width: navWidth.w2}"
      :v-if="navLevel > 0"
      @click="setRouter" />
    <!-- {{ navWidth }} -->

    <!-- Content insert point -->
    <router-view class="insertPoint"
        :style="{left: specs.xPos}"
        />
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
  data() {
    return {
      // bg: 'url("../assets/images/bgds/pexels-miguel-lights.jpg")',
    }
  },
  mounted() {
    // scan img folder to fill backgrounds Array and set bgImg
    console.log('CREATED FIRED!');
    this.setBg;
  },
  computed: {
    ...mapState(['USER_TOUCH','bgImg','navLevel','navSection','navWidth','navShow','specs','target']),
    ...mapGetters(['setBg']),
  },
  methods: {
    ...mapActions(['detectUserTouch','xCoords','setRouter']),
  },
}
</script>


<style lang="scss" >
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css");
@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,400;0,700;0,900;1,100;1,400;1,700;1,900&display=swap');

html {
  height: 100%;
}
body {
  margin: 0;
  padding: 0;
  min-height: 100%;
  // border: 5px dotted red;
}

// Transitions //
.fadeIn{
  opacity: 1;
}
.fadeOut {
  opacity: 0;
}

.translateOut {
  transform: translateX(-200px);
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
  align-items: stretch;
  background: var(--bg-img);
  background-size: cover;
  background-repeat: no-repeat;
  // background-position: center center;
  height: 100vh;
  font-family: Lato;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  // border: 3px dashed pink;
}

a {
  color: white;
  text-decoration: none;
  &:hover {
    color: goldenrod;
  }
}

.active {
  color: goldenrod;
  font-weight: bold;
}

.set0,
.set1,
.set2 {
  height: 100vh;
  transition: all .7s;
  background: black;
  color: white;
}


.set0 {
  background: var(--bg-img);
  background-size: cover;
  background-repeat: no-repeat;
  filter: blur(8px);
  -webkit-filter: blur(3px);
  opacity: 1;
}

.set1 {
  display: flex;
  flex-direction: column;
  z-index: 2;
  // border: 3px dotted green;
}

.set2 {
  display: flex;
  background: rgba(0,0,0,.85);
  z-index: 1;
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

@media (max-width: 850px) {
  // .container {
  //   flex-direction: column;
  // }
  .set0 {
    display: none;
    opacity: 0;
  }
}

</style>
