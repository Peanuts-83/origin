<template>
  <div class="navSec">
    <div class="info">
    </div>

      <ul :class="{ fadeIn: navLevel >= 1, fadeOut: navLevel < 1}">
        <li v-for="entry in navData[navSection]"
            :key="entry.index"
            @click="activateNav({ level: 2, section: navSection }),
            setTarget(entry)"  >

          {{ entry.name }}

        </li>
      </ul>

  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "NavSec",
  props: ["show"],
  computed: {
    ...mapState([
      "navLevel",
      "navSection",
      "navData",
    ]),
  },
  methods: {
    ...mapActions(['activateNav','setTarget']),
  },
};
</script>

<style lang="scss" >
ul {
  list-style: none;
  padding: 0;
  width: 100%;
  transition: all 1s;
  transition-delay: .2s;

  &.fadeIn {
    transition: .5s;
    transition-delay: 1s;
  }

  li {
    padding: 20px;
    margin: 0 auto;

    &:hover {
      cursor: pointer;
      background: rgba(0, 0, 0, 0.5);
    }
  }
}
</style>