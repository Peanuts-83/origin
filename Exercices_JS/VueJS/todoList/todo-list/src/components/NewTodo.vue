<template>
  <div class="container">
    <input
      type="text"
      id="text"
      placeholder="Add new task..."
      @keyup.enter="addTodo"
      v-model="todo.text"
    />
  </div>
</template>

<script>
export default {
  name: "NewTodo",
  data() {
    return {
      todo: { text: "", isDone: false, date: new Date().toLocaleDateString() },
    };
  },
  methods: {
    addTodo() {
      this.$emit("add-todo", this.todo);
      this.todo = {
        text: "",
        isDone: false,
        date: new Date().toLocaleDateString(),
      };
    },
  },
};
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  font-weight: bold;

  input {
    padding-left: 15px;
    padding: 5px 5px;
    height: 100%;
    width: 100%;
    font-size: 1em;
    font-weight: bold;
    color: lightblue;
    background: #002f36;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    border: none;
  }
}
</style>