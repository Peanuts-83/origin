<template>
  <div class="production">
    <div class="info" v-if="navLevel > 1"
          :style="{width: specs.info}" >explications projet {{ specs.info }}</div>
    <div class="project"
        :style="{width: specs.iframeWidth, height: specs.iframeHeight}">
      <div>{{ target.name }} {{ specs.routerWidth }}</div>

      <div class="iframe">
      <iframe ref="iframe" :src="target.url"
          v-if="target.url != ''"
          frameborder="0" />
      <!-- TARGET: {{ target }} -->
      <!-- MOUSEX: {{ mouseX }} -->
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
      // specsWidth: 0,
    }
  },
  // props: ['target'],
  computed: {
    ...mapState(['mouseX','navLevel','navWidth','target','specs']),
    specsWidth() {
      return (parseInt(this.navWidth.w2) * window.innerWidth /100) +'px';
    },
    // cssVars() {
    //   const width = (parseInt(this.navWidth.w2) * window.innerWidth /100);
    //   return {
    //     '--specs-width': width +'px',
    //     '--project-width': (window.innerWidth - (width + 150)) +'px',
    //     '--iframe-width': ((window.innerWidth - width) * .75) +'px',
    //     '--height': window.innerHeight +'px',
    //   }
    // }
  },
}
</script>

<style lang="scss">
  .production {
    display: flex;
    width: 90%;
    // border: 3px dashed pink;
  }

  // .specs {
  //   // width: var(--specs-width);
  // }

  .project {
    display: flex;
    flex-direction: column;
    flex: 1 1 100%;
    // width: var(--project-width);
    // height: var(--height);
    background: white;
    text-align: center;

    .iframe {
      width: 100%;
      height: 100%;
      resize: both;
      overflow: auto;
      // border: 2px solid;
      padding: 20px;

      iframe {
        width: 100%;
        height: 100%;
      }
    }
  }
</style>
