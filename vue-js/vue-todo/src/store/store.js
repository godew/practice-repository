import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);
// 플러그인 기능
// 전역으로 등록하는 기능


const storage = {
    fetch() {
        const arr = [];
        if (localStorage.length > 0) {
            for(let i = 0; i < localStorage.length; i++) {
                arr.push(JSON.parse(localStorage.getItem(localStorage.key(i))));
            }
        }
        return arr;
    }
}
export const store = new Vuex.Store({
    state: {
        todoItems: storage.fetch()
    },

    mutations: {
        addOneItem(state, todoItem) {
            const obj = {completed: false, item:(todoItem)}; 
            localStorage.setItem((todoItem), JSON.stringify(obj));
            state.todoItems.push(obj);
        },
        removeOneItem(state, payload) {
            localStorage.removeItem(payload.todoItem.item);
            state.todoItems.splice(payload.idx, 1);
        },
        toggleOneItem(state, payload) {
            state.todoItems[payload.idx].completed = !state.todoItems[payload.idx].completed;
            localStorage.removeItem(payload.todoItem.item);
            localStorage.setItem(payload.todoItem.item, JSON.stringify(payload.todoItem));
        },
        clearAllItem(state) {
            state.todoItems = [];
            localStorage.clear();
        }
    },

    getters: {
        storedTodoItems(state) {
            return state.todoItems;
        }
    }
});