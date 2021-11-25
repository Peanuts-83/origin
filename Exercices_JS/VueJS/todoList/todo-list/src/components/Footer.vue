<template>
  <div class="container">
    <span class="left">{{ itemsLeft }} items left</span>
    <div class="select">
      <span :class="{ selected: selection == 'All' }" @click="show('All')"
        >All</span
      >
      <span :class="{ selected: selection == 'Active' }" @click="show('Active')"
        >Active</span
      >
      <span
        :class="{ selected: selection == 'Completed' }"
        @click="show('Completed')"
      >
        Completed
      </span>
    </div>
    <div>
      <span class="clear" v-show="completedLeft.length" @click="clearCompleted"
        >Clear completed</span
      >
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selection: "All",
    };
  },
  props: ["itemsLeft", "todos"],
  computed: {
    completedLeft() {
      return this.todos.filter((item) => item.isDone);
    },
  },
  methods: {
    show(sel) {
      this.$emit("show", { selection: sel });
      this.selection = sel;
    },
    clearCompleted() {
      if (this.selection == "Completed") {
        this.selection = "All";
      }
      this.$emit("clear-completed");
    },
  },
};
</script>

<style lang="scss" scoped>
.container {
  display: flex;

  font-size: 0.8em;
  font-weight: bold;

  * {
    margin: 3px 5px;
    // border: 1px dashed red;
    flex: 1;
  }

  .left {
    text-align: left;
    flex-basis: 15px;
  }

  .select *{
    padding: 2px;
  }

  .select *.selected {
    border: 1px solid #002f36;
  }

  .select *:hover {
    cursor: pointer;
    border: 1px solid #002f36;
  }

  .clear {
    justify-content: flex-end;
    text-align: right;
  }

  .clear:hover {
    cursor: pointer;
    color: red;
  }
}
</style>