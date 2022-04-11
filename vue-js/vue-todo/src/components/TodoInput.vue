<template>
    <div class="inputBox shadow">
        <input type="text" v-model="newTodoItem" @keyup.enter="addTodo">
        <span class="addContainer" @click="addTodo">
            <i class="fa-solid fa-plus addBtn"></i>
        </span>

        <alert-modal v-if="showModal" @close="showModal = false">
            <h3 slot="header">
                경고!
                <i class="closeModalBtn fas fa-times" @click="showModal = false"></i>
            </h3>

            <div slot="body">
                아무것도 입력하지 않았습니다.
            </div>
        </alert-modal>
    </div>
</template>

<script>
import AlertModal from './common/AlertModal.vue';

export default {
    data() {
        return {
            newTodoItem: "",
            showModal: false
        }
    },
    methods: {
        addTodo: function() {
            if(this.newTodoItem) {
                this.$emit('addTodoItem', this.newTodoItem);
                this.clearInput();
            } else {
                this.showModal = !this.showModal;
            }
        },
        clearInput: function() {
            this.newTodoItem = '';
        }
    },
    components: {
        'alert-modal': AlertModal
    }
};
</script>

<style scoped>
input:focus {
	outline: none;
}
.inputBox {
	background: white;
	height: 50px;
	line-height: 50px;
	border-radius: 5px;
}
.inputBox input {
	border-style: none;
	font-size: 0.9rem;
}
.addContainer {
	float: right;
	background: linear-gradient(to right, #6475FB, #8763FB);
	display: block;
	width: 3rem;
	border-radius: 0 5px 5px 0;
}
.addBtn {
	color: white;
	vertical-align: middle;
}
.closeModalBtn {
    cursor: pointer;
}
</style>