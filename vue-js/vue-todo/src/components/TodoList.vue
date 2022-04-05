<template>
    <div>
        <ul>
            <li v-for="(todoItem, idx) in todoItems" :key="todoItem.item" class="shadow">
                <i class="checkBtn fa-solid fa-check" :class="{checkBtnComplated: todoItem.completed}" @click="toggleComplete(todoItem)"></i>
                <span :class="{textCompleted: todoItem.completed}">{{ todoItem.item }}</span>
                <span class="removeBtn" @click="removeTodo(todoItem, idx)">
                    <i class="fa-solid fa-trash-can"></i>
                </span>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            todoItems: []
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
    methods: {
        removeTodo: function(todoItem, idx) {
            localStorage.removeItem(todoItem);
            this.todoItems.splice(idx, 1);
        },
        toggleComplete: function(todoItem) {
            todoItem.completed = !todoItem.completed;
            localStorage.removeItem(todoItem.item);
            localStorage.setItem(todoItem.item, JSON.stringify(todoItem));
        }
    }
};
</script>

<style scoped>
ul {
	list-style-type: none;
	padding-left: 0px;
	margin-top: 0;
	text-align: left;
}
li {
	display: flex;
	min-height: 50px;
	height: 50px;
	line-height: 50px;
	margin: 0.5rem 0;
	padding: 0 0.9rem;
	background: white;
	border-radius: 5px;
}
.checkBtn {
	line-height: 45px;
	color: #62acde;
	margin-right: 5px;
}
.checkBtnComplated {
	color: #b3adad;
}
.textCompleted {
	text-decoration: line-through;
	color: #b3adad;
}
.removeBtn {
	margin-left: auto;
	color: #de4343;
}
</style>