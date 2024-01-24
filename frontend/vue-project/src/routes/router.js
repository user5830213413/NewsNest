import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue'
import SingleNews from '../components/SingleNews.vue'
import Login from '../components/Login.vue'
import MyNews from '../components/MyNews.vue'
import AddNews from '../components/AddNews.vue'
import store from  '../store'

const routes = [
    {
      path: '/',
      name: 'all-news',
      component: Home,
    },
    {
      path: '/news/:id',
      name: 'single-news',
      component: SingleNews,
    },
    {
      path: '/my-news',
      name: 'my-news',
      component: MyNews,
      beforeEnter: (to, from, next) => {
        if(store.getters.isAuthenticated){
          next()
        } else {
          next('/login')
        }
      }
    },
    {
      path: '/add-news',
      name: 'add-news',
      component: AddNews,
      beforeEnter: (to, from, next) => {
        if(store.getters.isAuthenticated){
          next()
        } else {
          next('/login')
        }
      }
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
      },
];
  
const router = createRouter({
    history: createWebHistory(),
    routes,
});
  
export default router;