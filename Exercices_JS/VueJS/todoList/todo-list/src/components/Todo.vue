<template>
  <div class="container">
    <li class="todo"
      v-for="todo in todos"
      :key="todo.index"
      @dblclick="startEdit(todo)"
    >
      <input type="checkbox"
        :class="{ done: todo.isDone }"
        v-model="todo.isDone" />
      <label for="todoText"
              id="labelText"
              :class="{ done: todo.isDone, editing: todo === editing}"
              >
        {{ todo.text }}
      </label>
      <input type="text"
            id="todoText"
            :value="todo.text"
            :class="{ editing: todo === editing}"
            @keyup.esc="cancelEdit"
            @blur="finishEdit"
            @keyup.enter="finishEdit"
            autofocus/>

      <span class="date">
        {{ todo.date }}
      </span>
      <span class="material-icons" id="delete" @click="destroy(todo)">
      delete
      </span>
    </li>
  </div>
</template>

<script>
export default {
  name: "Todo",
  props: ["todos"],
  data() {
    return {
      editing: null,
    }
  },
  computed: {
  },
  methods: {
    startEdit(todo) {
      this.editing = todo;
    },
    finishEdit(event) {
      if (!this.editing) return;
      const textbox = event.target;
      this.editing.text = textbox.value;
      this.editing = null;
    },
    cancelEdit() {
      this.editing = null;
    },
    destroy(todo) {
      this.$emit('destroy-todo', {todo: todo});
    },
  }
};
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex: auto;
  flex-direction: column;
}

.todo {
  display: flex;
  font-size: 1.5em;
  justify-content: flex-start;
  padding: 15px 0;
  * {
    margin: 0 3%;
    text-align: left;
  }
  input {
    transition: all .3s;
  }
  input:checked {
    transform: rotateZ(-15deg);

  }
  #labelText {
    display: flex;
    overflow-wrap: anywhere;
  }
  #labelText.editing {
    display: none;
  }

  #todoText {
    display: none;
    background: none;
    border: none;
    font-size: 1em;
  }
  #todoText.editing  {
    display: flex;
    flex: auto;
    background: rgba(245,255,255,.5);
  }

  .date {
    margin: 0 0;
    text-align: right;
    font-size: .8em;
    align-self: center;
    margin-left: auto;
    color: #495667;
  }
}

.todo:hover {
  background: rgba(245,255,255,0.3);
}

.done {
  text-decoration: line-through;
  color: #495667;
}

#delete {
  color:#002f36;
}

#delete:hover {
  cursor: pointer;
  color: red;
}

@media (max-width: 400px) {
    .todo {
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-size: 1em;

      * {
        text-align: center;
      }

      .date {
        margin-left: 0;
      }
    }
}
</style>