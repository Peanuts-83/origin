<template>
  <div class="container" >
    <div class="set0" ></div>
    <div class="set1" >
      SET 1
      <div>
        <div class="title">
          Thomas RANQUE Développeur Front-end Spécialisé Vue.js
        </div>
        <div class="links">
          <span alt="GitHub"><i class="fab fa-github"></i></span>
          <span alt="Confluence"><i class="fab fa-confluence"></i></span>
          <span alt="Linkedin"><i class="fab fa-linkedin"></i></span>
          <span alt="Facebook"><i class="fab fa-facebook-square"></i></span>
          <span alt="email"><i class="fas fa-at"></i></span>
          <span alt="phone"><i class="fas fa-mobile-alt"></i></span>
        </div>
      </div>
      <div class="nav">
        <span>
          production
        </span>
        <span>
          connaissances
        </span>
        <span>
          cv
        </span>
      </div>
    </div>
    <div class="set2">SET 2</div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { mapState } from 'vuex';

export default {
  name: "Home",
  components: {
  },
  computed: {
    ...mapState({
      bgds: 'bgds',
      background: 'background',
      colorRed: 'colorRed',
    }),
    setBackground() {
      let index = Math.round(Math.random() * this.bgds.length);
      // let backgroundImg = this.bgds[index];
      console.log(index, this.bgds[index].url, `url('${this.bgds[index].url}')`);
      return this.bgds[index].url;
    },
  }
};
</script>

<style lang="scss" >
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css");


.container {
  display: flex;
  // flex-direction: column;
  justify-content: flex-start;
  // background:  url(v-bind(background)) no-repeat center fixed;
  background-size: cover;
  height: 100%;
}

.set0,
.set1,
.set2 {
  // flex: 1 1 10px;
  width: 200px;
  height: 100vh;
  transition: all 1s;
  background: black;
  color: white;
}


.set0 {
  // background:  url("../assets/images/ours.jpg") no-repeat center fixed;
  background-size: cover;
  filter: blur(8px);
  -webkit-filter: blur(5px);
  opacity: 1;
  width: 35%;
}

.set1 {
  display: flex;
  flex-direction: column;
  z-index: 2;
  // justify-content: space-around;


  .title {
    padding-top: 100px;
    color: v-bind(colorRed)
  }
  .links {
    display: flex;
    justify-content: space-evenly;
    margin: 10px 5px;
  }
  .nav {
    display: flex;
    flex-direction: column;
    margin-top: 60px;

    * {
      padding: 20px;
      text-align: center;
      // border: 1px dashed red;
    }
    *:hover {
      cursor: pointer;
      background: rgba($color: white, $alpha: .2);
    }

  }
}

.set2 {
  opacity: 0.3;
}

</style>
