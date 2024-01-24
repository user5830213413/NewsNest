<script setup>
import { useStore } from 'vuex'
import { computed } from 'vue'
import axios from 'axios'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const store = useStore()
const isAuthenticated = computed(() => store.getters.isAuthenticated)


const login = async () => {

  if (isAuthenticated.value) {
    return;
  }

  try {
    const { data } = await axios.post('http://127.0.0.1:5000/api/login')
    localStorage.setItem('user_id', data.user_id)
    store.dispatch('loginUser', data.user_id)
    toast.success(data.message)
  } catch (err) {
    toast.warning(err.response.data.message)
  }
};

const handleButtonClick = () => {
  if (isAuthenticated.value) {
    logout()
  } else {
    login()
  }
};

const logout = () => {
  localStorage.removeItem('user_id')
  store.dispatch('logoutUser')
};
</script>

<template>
  <div class="text-white">
    <h1 class="text-center text-3xl mt-10">Авторизация</h1>

    <div class="text-center mt-10">
      <p class="text-2xl mb-5">
        {{ isAuthenticated ? 'Для того, чтобы выйти, нажмите кнопку Выйти!' : 'Для того, чтобы начать добавлять посты, пожалуйста, нажмите кнопку Войти!' }}
      </p>

      <button class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" @click="handleButtonClick">
        {{ isAuthenticated ? 'Выйти' : 'Войти' }}
      </button>
    </div>
  </div>
</template>