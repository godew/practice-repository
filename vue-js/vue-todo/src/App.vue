<template>
  <div id="app">
    <TodoHeader></TodoHeader>
    <TodoInput @addTodoItem="addOneItem"></TodoInput>
    <TodoList :propsdata="todoItems" @removeItem="removeOneItem" @toggleItem="toggleOneItem"></TodoList>
    <TodoFooter @clearAll="clearAllItem"></TodoFooter>
  </div>
</template>

<script>
import TodoHeader from './components/TodoHeader.vue'
import TodoInput from'./components/TodoInput.vue'
import TodoList from './components/TodoList.vue'
import TodoFooter from './components/TodoFooter.vue'

export default {
  data() {
    return {
      todoItems: []
    }
  },
  methods: {
    addOneItem: function(todoItem) {
      let obj = {completed: false, item:(todoItem)}; 
      localStorage.setItem((todoItem), JSON.stringify(obj));
      this.todoItems.push(obj);
    },
    removeOneItem: function(todoItem, idx) {
      localStorage.removeItem(todoItem.item);
      this.todoItems.splice(idx, 1);
    },
    toggleOneItem(todoItem, idx) {
      this.todoItems[idx].completed = !this.todoItems[idx].completed;
      localStorage.removeItem(todoItem.item);
      localStorage.setItem(todoItem.item, JSON.stringify(todoItem));
    },
    clearAllItem() {
      this.todoItems = [];
      localStorage.clear();
    }
  },
  created: function() {
      if (localStorage.length > 0) {
          for(var i = 0; i < localStorage.length; i++) {
              let obj = JSON.parse(localStorage.getItem(localStorage.key(i)));
              this.todoItems.push(obj);
              // this.todoItems.push(localStorage.key(i));
          }
      }
  },

  components: {
    'TodoHeader': TodoHeader,
    'TodoInput': TodoInput,
    'TodoList': TodoList,
    'TodoFooter': TodoFooter,
  }
};
</script>

<style>
body {
  text-align: center;
  background-color: #F6F6F6;
}
input {
  border-style: groove;
  width: 200px;
}
button {
  border-style: groove;
}
.shadow {
  box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.03);
}
</style>