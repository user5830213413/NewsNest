<script setup>

import axios from 'axios'
import { useStore } from 'vuex'
import { onMounted, ref } from 'vue'

const store = useStore()
const news = ref([])

const getmyNews = async () => {
    const { data } = await axios.get('http://127.0.0.1:5000/api/my-news', {
        headers: {
        Authorization: `Bearer ${store.state.user_id}`,
        }
    })
    news.value = data
}

onMounted(() => {
    getmyNews()
})

</script>

<template lang="">
    <div>
        <div class="text-center mt-10" v-if="news.length === 0">
            <span class="text-white text-3xl font-semibold">У вас нет постов!</span>
        </div>


        <div class="mx-10 mt-10 p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700" v-for="item in news">
            <a href="#">
                <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-500 dark:text-white">{{ item.title.slice(0, 10) }} ...</h5>
            </a>
            <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{ item.content.slice(0, 10) }} ...</p>
            <router-link :to="{ name: 'single-news', params: { id: item.id }}">
                <p class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Перейти
                    <svg class="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
                    </svg>
                </p>
            </router-link>

            <p class="mt-3 text-gray-700">
                {{ item.created }}
            </p>
        </div>
    </div>
</template>

<style lang="">
    
</style>