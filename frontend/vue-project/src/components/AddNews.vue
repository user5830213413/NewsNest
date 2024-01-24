<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'
import axios from 'axios'

const currentNews = ref({title: '', content: ''})
const store = useStore()

const saveNews = async () => {
    const {data} = await axios.post('http://127.0.0.1:5000/api/news', {
        user_id: store.state.user_id,
        title: currentNews.value.title,
        content: currentNews.value.content
    })
    toast.success(data.message)
}
</script>


<template lang="">
    <div>
        <div class="text-black">
            <form @submit.prevent="saveNews" class="text-center">
                <div>
                    <div><label  class="text-white text-1xl font-semibold">Title</label></div>
                    <input class="shadow  appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" v-model="currentNews.title" required>
                </div>
                <div class="mt-10">
                    <div><label class="text-white text-1xl font-semibold">Content</label></div>
                    <textarea v-model="currentNews.content" class="p-2.5 text-gray-700 rounded-lg border border-gray-300 focus:ring-blue-500" required></textarea>
                </div>
            
                <button type="submit" class="bg-transparent hover:bg-blue-500 mt-5 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">Add</button>
        
            </form>
        </div>
    </div>
</template>

<style lang="">
    
</style>