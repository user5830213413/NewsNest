<script setup>
import { useRoute, useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useStore } from 'vuex';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const store = useStore()
const router = useRouter()
const postId = useRoute().params.id
const news = ref({})
const newsEditing = ref(false)
const currentNews = ref({title: '', content: ''})

const getSingleNews = async () => {
    const { data } = await axios.get(`http://127.0.0.1:5000/api/news/${postId}`)
    news.value = data
}

const editNews = () => {
    newsEditing.value = true
}

const cancelEditNews = () => {
    newsEditing.value = false
}

const saveEditNews = async () => {
        const {data}  = await axios.put(`http://127.0.0.1:5000/api/news/${postId}`, {
        title: currentNews.value.title,
        content: currentNews.value.content,
        user_id: store.state.user_id
    })
    getSingleNews()
    toast.success(data.message)
    newsEditing.value = false
}

const deleteNews = async () => {
    const { data } = await axios.delete(`http://127.0.0.1:5000/api/news/${postId}`)
    toast.success(data.message)
    await new Promise(resolve => setTimeout(resolve, 2000))

    router.push({ name: 'all-news' })
}

const isUserNews = () => {
    return store.state.user_id === news.value.user_id
}

onMounted(() => {
    getSingleNews()
})
</script>

<template>
    <div>
        <h1 class="text-center text-3xl mt-5 font-bold text-white">{{news.id}}</h1>

        <div class="mx-10 mt-10 p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
            <a href="#">
                <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-500 dark:text-white">{{ news.title }}</h5>
            </a>
            <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{ news.content }}</p>
            <p class="mt-3 text-gray-700">
                {{ news.created }}
            </p>

            <button class="bg-transparent hover:bg-red-500 text-white font-semibold hover:text-white py-2 px-4 border border-red-500 hover:border-transparent rounded mt-5" v-if="isUserNews()" @click="editNews">Edit</button>
            <button class="bg-transparent hover:bg-red-500 text-white font-semibold hover:text-white py-2 px-4 border border-red-500 hover:border-transparent rounded mt-5" v-if="isUserNews()" @click="deleteNews">Delete</button>
        </div>


        <form @submit.prevent="saveNews" class="text-center" v-if="newsEditing">
            <div>
                <div><label  class="text-white text-1xl font-semibold">Title</label></div>
                    <input v-model="currentNews.title" class="shadow  appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" required>
                </div>
            <div class="mt-10">
                <div><label class="text-white text-1xl font-semibold">Content</label></div>
                <textarea v-model="currentNews.content" class="p-2.5 text-gray-700 rounded-lg border border-gray-300 focus:ring-blue-500" required></textarea>
            </div>
            <button type="submit" class="bg-transparent hover:bg-blue-500 mt-5 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" @click="saveEditNews">Save</button>
            <button class="bg-transparent ml-5 hover:bg-blue-500 mt-5 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" @click="cancelEditNews">Cancel</button>
        </form>
    </div>
</template>