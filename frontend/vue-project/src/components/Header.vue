<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'

const store = useStore()
const isAuthenticated = computed(() => store.getters.isAuthenticated)

</script>


<template>
  <div>
    <header class="flex justify-between text-white border-b border-white py-8 mx-10">
  
  <div>
    <h2>Лого</h2>
  </div>

  <ul class="flex items-center gap-5">
    <li>
      <router-link to="/"><span>Новости</span></router-link>
    </li>

    <li v-if="!isAuthenticated">
      <router-link to="/login"><span>Авторизация</span></router-link>
    </li>

    <li v-if="isAuthenticated">
      <router-link to="/add-news"><span>Добавить новость</span></router-link>
    </li>

    <li v-if="isAuthenticated">
      <router-link to="/my-news"><span>Мои посты</span></router-link>
    </li>

    <li v-if="isAuthenticated">
      <router-link to="/login"><span>Выход</span></router-link>
    </li>
  </ul>

</header>
  </div>
</template>
  