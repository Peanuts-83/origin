<template>
  <div class="navPrim">
    <div>
      <!--// INFO: Title -->
      <router-link
        to="/"
        class="title"
        @click="activateNav({ level: 0, section: 'Home' })"
        :class="{ fadeIn: navLevel < 2, fadeOut: navLevel >= 2 }"
      >
        <div>Thomas RANQUE <br>Front-end Developer <br> <hr> Vue.js Dedicated Framework</div>
      </router-link>

      <!--// INFO: Socials -->
      <div
        class="link"
        :class="{ fadeIn: navLevel < 2, fadeOut: navLevel >= 2 }"
      >
        <a
          href="https://github.com/Peanuts-83/origin"
          target="blank"
          alt="GitHub"
          @mouseenter="textLink = 'My GitHub'"
          @mouseleave="textLink = ''"
          ><i class="fab fa-github"></i
        ></a>
        <a
          href="https://peanuts-team.atlassian.net/wiki/spaces/CF/overview"
          target="blank"
          alt="Confluence"
          @mouseenter="textLink = 'My Confluence'"
          @mouseleave="textLink = ''"
          ><i class="fab fa-confluence"></i
        ></a>
        <a
          href="#"
          target="blank"
          alt="Linkedin"
          @mouseenter="textLink = 'My Linkedin'"
          @mouseleave="textLink = ''"
          ><i class="fab fa-linkedin"></i
        ></a>
        <a
          href="#"
          alt="email"
          @mouseenter="textLink = 'tranque@free.fr'"
          @mouseclick="textLink = 'tranque@free.fr'"
          @mouseleave="textLink = ''"
          ><i class="fas fa-at"></i
        ></a>
        <a
          href="#"
          alt="phone"
          @mouseenter="textLink = '06.21.35.39.32'"
          @mouseclick="textLink = '06.21.35.39.32'"
          @mouseleave="textLink = ''"
          ><i class="fas fa-mobile-alt"></i
        ></a>
        <!-- legend text for icons -->
        <span
          class="textLink"
          :class="{ translateIn: textLink != '', translateOut: textLink == '' }"
          >{{ textLink }}</span
        >
      </div>
    </div>

    <!-- // INFO: Nav section -->
    <div class="nav" :class="{ fadeIn: navLevel < 2, fadeOut: navLevel >= 2 }">
      <a href="#" :class="{active: navSection == 'Production'}"
        @click.prevent="activateNav({ level: 1, section: 'Production' })"
      >
        Production
      </a>
      <router-link
        to="/skills" :class="{active: navSection == 'Skills'}"
        @click="activateNav({ level: 1, section: 'Skills' })"
      >
        Skills
      </router-link>
      <router-link to="/cv" :class="{active: navSection == 'CV'}"     @click="activateNav({ level: 3, section: 'CV' })">
        CV
      </router-link>
    </div>

    <!-- // INFO: Vertical title & menu icon  -->
    <div
    class="miniNav" :class="{ slide: navLevel >= 2 }">
       <!-- menu ONLY if touchScreen -->
        <!-- // TODO: fixed vertical nav! -->
      <a class="menu"
        v-if="USER_TOUCH"
        @click="toggleNavSec" >
        <i class="fas fa-bars"></i>
      </a>
      <!-- end -->
      <router-link
        to="/"
        @click="activateNav({ level: 0, section: 'Home' }), setTarget('')"
        class="vertical"
      >
        <span v-if="navSection != 'Home'">{{ navSection }}</span>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from "vuex";

export default {
  name: "Nav",
  data() {
    return {
      textLink: "",
    };
  },
  computed: {
    ...mapState(["USER_TOUCH","backgrounds", "navWidth", "navLevel", "navSection"]),
    ...mapGetters(["setBg"]),
  },
  methods: {
    ...mapActions(["activateNav", "setTarget","toggleNavSec"]),
  },
};
</script>

<style lang="scss">
.navPrim {
  display: flex;
  flex-direction: column;
  height: 100%;
  text-align: center;
  color: white;
}

.title {
  font-size: 1.2em;
  font-weight: 400;
  hr {

    margin: 5px 20px;
  }
  &.router-link-exact-active {
    color: white;
  }
  &.fadeIn {
    transition: opacity 1s;
    transition-delay: 0.5s;
  }
  div {
    padding: 20vh 0 20px 0;
  }
}

.link {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  transition: 0.2s;
  &.fadeIn {
    transition: all 1s;
    transition-delay: 0.5s;
  }
  // &:hover *{
  //   cursor: pointer;
  // }
  a {
    padding: 5%;
    // margin: 5px;
    // border: 1px dashed red;
  }
  .textLink {
    transition: all 0.3s;
    width: 100%;
    height: 1em;
    color: goldenrod;
    padding: 10px 0;
  }
}

.nav {
  display: flex;
  flex-direction: column;
  margin: 5vh 0;
  transition: all .2s;
  font-size: 1.5em;;

  &.fadeIn {
    transition: all 1s;
    transition-delay: 0.5s;
  }

  * {
    padding: 20px 0;
    &:hover {
      cursor: pointer;
      background: rgba($color: white, $alpha: 0.2);
    }
  }
}

// Vertical title navLevel 2/3
.miniNav {
  position: absolute;
  top: -150px;
  width: 50px;
  height: 1vh;
  transition: all 0.5s;
  opacity: 0;
  // border: 3px dashed pink;

  .menu  {
    font-size: 1.8em;
    padding: 15px;
    margin-top: 15px;
    // border: 1px dashed green;
  }

  .vertical {
    writing-mode: vertical-rl;
    font-weight: 100;
    font-size: 3em;
    * {
      overflow: hidden;
    }
    overflow: hidden;
    left: -5px;
    position: absolute;
    margin-top: 40px;
    height: 100%;
    text-align: right;
    transform: rotate(180deg);
  }

  &.slide {
    display: block;
    height: 100%;
    transform: translateY(150px) ;
    opacity: 1;
    cursor: pointer;
  }
}


@media (max-width: 600px) {
}
</style>
