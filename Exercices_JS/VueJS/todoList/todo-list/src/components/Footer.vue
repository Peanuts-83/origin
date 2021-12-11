<template>
  <div class="container">
    <div class="left">{{ itemsLeft }} items left</div>

    <div class="select">
      <div :class="{ selected: selection == 'All' }" @click="show('All')"
        >All</div
      >
      <div :class="{ selected: selection == 'Active' }" @click="show('Active')"
        >Active</div
      >
      <div
        :class="{ selected: selection == 'Completed' }"
        @click="show('Completed')"
      >
        Completed
      </div>
    </div>

    <div class="clear">
        <span v-show="completedLeft" @click="clearCompleted">Clear completed</span>
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
      return this.todos.filter((item) => item.isDone).length;
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
    // completedLeft() {
    //   const completed = this.todos.filter((item) => item.isDone).length;
    //   console.log(completed)
    //   if (!completed) {
    //     this.clearText = "";
    //   } else {
    //     this.clearText = "Clear completed"
    //   }
    // },
  },
};
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  font-size: .9em;
  font-weight: 800;
  margin: 5px;

  // * {
  //   border: 1px dashed red;
  // }


  .left {
    // margin: 3px 5px;
    text-align: left;
    flex: 1 1 20%;
    display: flex;
    align-items: center;
  }

  .select {
    // margin: 3px 5px;
    // width: 600px;
    flex: 1 1 60%;
    display: flex;
    justify-content: center;

    * {
      padding: 5px;
          margin: 3px;
        }

    *.selected {
      border: 1px solid #002f36;
    }
    *:hover {
      cursor: pointer;
      border: 1px solid #002f36;
    }
  }

  .clear {
    // margin: 3px 5px;
    flex: 1 1 20%;
    display: flex;
    text-align: right;
    // justify-content: flex-end;
    // align-items: center;
    span {
      width: 100%;
      text-align: right;
      align-self: center;
    }
  }

  .clear:hover {
    cursor: pointer;
    color: red;
  }
}

@media (max-width: 500px) {
  .container{
    flex-direction: column;
  }
  .left {
    justify-content: center;
    text-align: center;
    margin: 5px 0;
  }
  .clear {
    justify-content: center;
    margin: 3px auto;
  }
}
</style>