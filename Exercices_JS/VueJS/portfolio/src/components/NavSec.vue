<template>
  <div class="navSec">
    <div class="info">
    </div>

      <ul :class="{translateIn: navLevel >= 1, translateOut: navLevel < 1}">
        <li v-for="entry in navData[navSection]"
            :key="entry.index"
            @click="activateNav({ level: 2, section: navSection }),
            setTarget(entry)"  >
          <!-- // TODO: selected section set to yellow/bold -->
          <router-link :class="{active: entry.name == target.name}"
        :to="navSection">
          {{ entry.name }}
          </router-link>
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
      "target"
    ]),
  },
  methods: {
    ...mapActions(['activateNav','setTarget']),
  },
};
</script>

<style lang="scss" scoped>
.navSec {
  ul {
    list-style: none;
    padding: 0;
    margin: 0;
    width: 100%;
    transition: all .5s;
    transition-delay: .5s;

    // &.fadeIn {
    //   transition: .5s;
    //   transition-delay: 3s;
    // }

    li {
      padding: 20px;
      margin: 0 auto;
      font-size: 1.2em;
      font-weight: 400;

      &:hover {
        cursor: pointer;
        background: rgba(0, 0, 0, 0.5);
      }
    }
  }
}
</style>