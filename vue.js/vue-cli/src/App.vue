<template>
  <!-- template root에는 하나의 element만 있어야 한다. -->
  <div>
    <AppHeader :propsdata="str" @renew="renewStr"></AppHeader>
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue';
// var AppHeader = {
//   template: '<>'
// } 와 같은 문법

export default {
  // new Vue({
  //   data: {
  //     str: 'hi'
  //   }
  // })
  // 겹칠 수 있기 때문에 function으로 만든다
  data: function() {
    return {
      str: 'roaroier'
    }
  },
  components: {
    AppHeader
  },
  methods: {
    renewStr: function() {
      this.str = 'hi';
    }
  }
}
</script>

<style>

</style>