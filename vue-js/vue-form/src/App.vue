<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="username">id: </label>
      <input id="username" v-model="username">
    </div>
    <div>
      <label for="password">pw: </label>
      <input id="password" v-model="password">
    </div>
    <button type="submit">login</button>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm: function() {
      // e.preventDefault();
      console.log(this.username, this.password);
      let url = 'https://jsonplaceholder.typicode.com/users';
      let data = {
        username: this.username,
        password: this.password
      }
      axios.post(url, data)
        .then(function(resp) {
          console.log(resp.data)
        })
        .catch(function(err){
          console.log(err);
        });
    }
  }
};
</script>

<style>

</style>