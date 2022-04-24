<template>
    <div>
        <transition-group name="list" tag="ul">
            <li v-for="(todoItem, idx) in storedTodoItems" :key="todoItem.item" class="shadow">
                <i class="checkBtn fa-solid fa-check" :class="{checkBtnComplated: todoItem.completed}" 
                    @click="toggleComplete({todoItem, idx})"></i>
                <span :class="{textCompleted: todoItem.completed}">{{ todoItem.item }}</span>
                <span class="removeBtn" @click="removeTodo({todoItem, idx})">
                    <i class="fa-solid fa-trash-can"></i>
                </span>
            </li>
        </transition-group>
    </div>
</template>
 
<script>
import { mapState, mapGetters, mapMutations } from 'vuex';
export default {
    methods: {
        ...mapMutations({
            removeTodo: 'removeOneItem',
            toggleComplete: 'toggleOneItem'
        }),
    },

    computed: {
        ...mapState({
            todoItems: (state) => state.todoItems
        }),
        ...mapGetters(['storedTodoItems'])
        // 이름이 다를 때 객체 형태로 사용가능
        // ...mapGetters({
        //     storedTodoItems
        // })
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
.list-enter-active, .list-leave-active {
    transition: all 1s;
}
.list-enter, .list-leave-to {
    opacity: 0;
    transform: translateY(30px);
}
</style>