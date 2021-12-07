<template>
  <div class="production">
    <div class="info" v-if="navLevel > 1 && target.info" >

      <p class="title">{{target.info.title}}</p>
      <p class="description">{{target.info.description}}</p>
      <div class="techTable">
        <span id="title"><i class="fas fa-tools"></i>TECHNOS</span>
        <ul class="technologies">
          <li v-for="tech in target.info.technologies" :key="tech.index">{{tech}} </li>
        </ul>
      </div>
      <div class="documentation" v-if="target.info.documentation">
        <span>{{target.info.documentation.title}}: </span>
        <a :href="target.info.documentation.url" target="blank" >
        <br>  <i class="fas fa-external-link-alt"></i> {{target.info.documentation.url}}</a>

      </div>
    </div>

    <div class="project">
      <div class="screens">
        <a href="#"><i class="fas fa-mobile-alt"></i></a>
        <span>Choose a view mode</span>
        <a href="#"><i class="fas fa-laptop"></i></a>
      </div>
      <div class="iframe">
        <iframe ref="iframe" :src="target.url"
            v-if="target.url != ''"
            frameborder="0" />
        <!-- TARGET: {{ target }}
        MOUSEX: {{ mouseX }} -->
      </div>

    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: "Project",
  data() {
    return {

    }
  },
  computed: {
    ...mapState(['navLevel','target','specs']),
  },
}
</script>

<style lang="scss" scoped>
  .production {
    display: flex;
    width: 90%;
    height: 100vh;
    // border: 3px dashed pink;
  }

  a {
    color: black;
    font-style: italic;
  }
  a:hover {
    color: orangered;
    }


  .info {
    background: rgba(255,255,255,.5);
    color: black;
    text-align: right;
    margin: 0;
    width: 30%;
    // border: 3px dashed pink;
    .title {
      background:goldenrod;
      color: white;
      text-shadow: 2px 2px 5px black;
      margin: 0;
      padding: 20px 10px;
      font-size: 2em;
    }
    .description {
      padding: 10px;
      font-size: 1.5em
      // border-bottom: 1px solid black;
    }
    .techTable {
      background:goldenrod;
      padding: 10px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: "";
      #title {
        text-shadow: 2px 2px 2px black;
        letter-spacing: 1em;
        font-weight: 800;
        color: white;
        // word-wrap:break-word;
      }
      .technologies {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: "";
        list-style: none;
        margin: 0;
        * {
          padding: 2px;
          border-bottom: 1px solid black;
        }
        *:hover {
          background: grey;
          text-shadow: 0 0 3px white;
        }
        // text-decoration: none;
        // border-bottom: 1px solid black;
      }

    }
    .documentation {
      margin: 10px;
      // border-top: 1px solid black;
    }
  }


  .screens {
    margin-top: 20px;
      font-size: 1.5em;
    a {
      font-size: 2em;
      padding: 15px;
      opacity: .5;
    }
    a:hover {
      opacity: 1;
    }
  }


  .project {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1 1 100%;
    width: 70%;
    background: white;
    color: grey;
    // color: black;
    // text-align: center;

    .iframe {
      width: 90%;
      height: 90%;
      resize: both;
      overflow: auto;
      padding: 20px;

      iframe {
        width: 95%;
        height: 95%;
        border-radius: 5%;
      }
    }
  }

  @media(max-width: 850px) {
    .production {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .info {
      width: 100%;
      // margin-right: 5%;
      text-align: left;
    }
    .project {
      width: 100%;
      margin: 5%;
    }
  }
</style>
