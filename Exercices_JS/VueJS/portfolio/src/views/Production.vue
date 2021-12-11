<template>
  <div :class="{ fadeIn: navLevel >= 2, fadeOut: navLevel < 2 , production: true}">
    <div class="info" v-if="navLevel > 1 && target.info" >

      <p class="title">
        {{target.info.title}}
        <br>
        <a :href="target.url" target="blank">
          <i class="fas fa-external-link-alt"></i>
        </a>
        </p>
      <p class="description">{{target.info.description}}</p>
      <div class="techTable">
        <span id="title"><i class="fas fa-tools"></i>TECHNOS</span>
        <ul class="technologies">
          <li v-for="tech in target.info.technologies" :key="tech.index">{{tech}} </li>
        </ul>
      </div>
      <div class="documentation" v-if="target.info.documentation">
        <span id="title">{{target.info.documentation.title}}: </span>
        <a :href="target.info.documentation.url" target="blank" >
        <br> <i class="fas fa-external-link-alt"></i> {{target.info.documentation.url}}</a>

      </div>
    </div>

    <div class="project">
      {{mouseX}} - {{navLevel}} - {{navWidth.w2}} - {{target.name}}
      <div class="screens">
        <a href="#" @click.prevent="setIFrame({width: '375px', height: '812px'})"><i class="fas fa-mobile-alt"></i></a>
        <span>Choose view mode</span>
        <a href="#" @click.prevent="setIFrame({width: '95%', height: '95%'})"><i class="fas fa-laptop"></i></a>
      </div>
      <div class="iframe">
        <iframe ref="iframe" loading="lazy" :src="target.url"
            :style="{width: specs.iframeWidth, height: specs.iframeHeight}"
            v-if="target.url != ''"
            frameborder="0" />
        <!-- TARGET: {{ target }}
        MOUSEX: {{ mouseX }} -->
      </div>

    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: "Project",
  computed: {
    ...mapState(['navLevel','target','specs', 'mouseX', 'navWidth']),
  },
  methods: {
    ...mapActions(['setIFrame'])
    // lazyloading for iframes using data-src in place of src
    // iframeUrl() {
    //   if ('loading' in HTMLIFrameElement.prototype) {
    //     console.log('iFrame lazyloading ok!');
    //     const iframes = document.querySelectorAll('iframe[loading="lazy"]');
    //     iframes.forEach(iframe => {
    //       iframe.src = iframe.dataset.src;
    //     })
    //   } else {
    //     // Dynamic import LazySizes librairy
    //     console.log('iFrame loading with LAZYSIZES script import...');
    //     const script = document.createElement('script');
    //     script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.2.2/lazysizes.min.js';
    //     document.body.appendChild(script);
    //   }
    // }
  }
}
</script>

<style lang="scss" scoped>
  .production {
    display: flex;
    width: 90%;
    height: 120vh;
    // opacity: 0;
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

    .title {
      background:goldenrod;
      color: white;
      text-shadow: 2px 2px 3px black;
      font-weight: 800;
      font-size: 2em;
      margin: 0;
      padding: 20px 10px;
      i {
        font-size: 1em;
      }
    }

    .description {
      padding: 10px;
      font-size: 1.1em;
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
      }
      .technologies {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: "";
        list-style: none;
        * {
          padding: 2px 5px;
          border-bottom: 1px solid black;
        }
        *:hover {
          background: grey;
          text-shadow: 0 0 4px white;
        }
      }
    }

    .documentation {
      margin: 10px;
      #title {
        font-weight: bold;
      }
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
      // resize: both;
      overflow: auto;
      padding: 10px 3%;

      iframe {
        // width: 95%;
        // height: 95%;
        transition: 1s;
        border-radius: 30px;
        border: 1px dashed grey;
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
      // margin: 5%;
    }
  }
</style>
