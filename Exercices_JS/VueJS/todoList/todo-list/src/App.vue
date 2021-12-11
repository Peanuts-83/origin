<template>
  <div id="app">
    <div class="title">{{ title }}</div>
    <div class="container">
      <div class="box">
        <NewTodo @add-todo="addToList" />
        <ul class="todoList">
          <Todo :todos="showTodos || todos"
                class="todos"
                @destroy-todo="destroyTodo"
                 />
        </ul>
        <div class="footer">
          <Footer @show="show"
                  @clearCompleted="clearCompleted"
                  :itemsLeft="itemsLeft"
                  :todos="showTodos || todos" />
        </div>
      </div>
    </div>
    <div class="copyright">{{ copyright }}</div>
  </div>
</template>

<script>
import Todo from "./components/Todo.vue";
import NewTodo from "./components/NewTodo.vue";
import Footer from "./components/Footer.vue";

export default {
  name: "App",
  components: {
    Todo,
    NewTodo,
    Footer,
  },
  data() {
    return {
      title: "Todos!",
      todos:  JSON.parse(localStorage.getItem('todos')) || [
        { text: "Todo app reminds important things to do...",
          isDone: false,
          date: this.newDate(3) },
        { text: "Default tasks are displayed if local storage is empty, but any modification stores tasks in local storage to enable persistent data.",
          isDone: false,
          date: this.newDate(5) },
        { text: "Existing tasks can be edited by double-click, saved with 'ENTER' or 'blur', unchanged with 'ESC'.",
          isDone: false,
          date: this.newDate(12) },
        { text: "Exemple of done task.",
        isDone: true,
        date: this.newDate(12) },
      ],
      showTodos: this.todos,
      selection: 'All',
    };
  },
  watch: {
    todos: {
      deep: true,
      handler(newValue) {
        localStorage.setItem('todos', JSON.stringify(newValue));
      }
    }
  },
  computed: {
    copyright() {
      const date = new Date().getFullYear();
      return `Copyright © ${date}`;
    },
    itemsLeft() {
      return this.todos.filter(item => item.isDone == false).length;
    }
  },
  methods: {
    addToList(obj) {
      const newTodo = obj;
      this.todos.unshift(newTodo);
    },
    newDate(daysOff) {
      const date = Date.now();
      const millisecOff = daysOff * 24 * 3600 * 1000;
      return new Date(date - millisecOff).toLocaleDateString();
    },
    destroyTodo(event) {
      const index = this.todos.indexOf(event.todo);
      this.todos.splice(index, 1);
      this.todo = "";
    },
    show(event) {
      this.selection = event.selection || event
      switch (this.selection) {
        case 'Active':
          this.showTodos = this.todos.filter(todo => todo.isDone === false);
          break;
        case 'Completed':
          this.showTodos = this.todos.filter(todo => todo.isDone === true);
          break;
        default:
          this.showTodos = this.todos;
          break;
      }
    },
    clearCompleted() {
      this.todos = this.todos.filter(item => item.isDone == false);
      this.show('All');
    },
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Fira+Sans&display=swap");
@import url("https://fonts.googleapis.com/icon?family=Material+Icons");

body {
  background: lightblue url("../public/images/post-it.webp") no-repeat center fixed;
  background-size: cover;
  height: 100%;
}

#app {
  font-family: "Fira Sans";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #002f36;
  margin: 60px 10px;
}

.title {
  font-size: 15vh;
  color: white;
  text-shadow: 0.02em 0.04em 5px #2c3e50;
  // border: 1px dashed red;
}

.container {
  display: flex;
  justify-content: center;
}

.box {
  border: 1px solid #002f36;
  margin: 5px 0;
  width: 600px;
  min-height: 30px;
  border-radius: 10px;
  border-bottom-right-radius: 0;
  box-shadow: 10px 10px 5px rgba(39, 50, 71, 0.6);
  background: rgba(245, 255, 255, 0.7);
  margin-bottom: 20px;

  .todoList {
    padding: 0;
  }

  .footer {
    border-top: 1px solid #002f36;
  }
}

.copyright {
  font-size: 1em;
}

@media (max-width: 400px) {
  .title {
    font-size: 30vw;
  }

  .footer {
    font-size: 0.6em;
  }

  .copyright {
    font-size: 0.7em;
  }
}
</style>
