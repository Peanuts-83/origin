<template>
  <div class="production" @load="info = setInfo">
    <div class="info" v-if="navLevel > 1"
          :style="{width: specs.info}" >
    {{target}}Hello
    </div>



    <div class="project"
        :style="{width: specs.iframeWidth, height: specs.iframeHeight}">
      <div>{{ target.name }} {{ specs.routerWidth }}</div>

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

<style lang="scss">
  .production {
    display: flex;
    width: 90%;
    height: 100vh;
    // border: 3px dashed pink;
  }

  .info {
    background: rgba(255,255,255,.5);
    color: black;
    border: 3px dashed pink;
  }

  .project {
    display: flex;
    flex-direction: column;
    flex: 1 1 100%;
    background: white;
    text-align: center;

    .iframe {
      width: 90%;
      height: 90%;
      resize: both;
      overflow: auto;
      padding: 20px;

      iframe {
        width: 95%;
        height: 95%;
      }
    }
  }
</style>
