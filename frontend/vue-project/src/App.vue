<script setup>
import { useStore } from 'vuex'
import { onBeforeMount } from 'vue'
import Header from './components/Header.vue'

const store = useStore()

onBeforeMount(async () => {
  await store.dispatch('initApp')
})

</script>

<template lang="">
  <div>
    <Header/>
  </div>
  <router-view></router-view>
</template>