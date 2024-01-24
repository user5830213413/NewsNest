import { createStore } from 'vuex';

export default createStore({
    state: {
        user_id: null
    },
    mutations: {
        login(state, user_id) {
            state.user_id = user_id
        },
        logout(state) {
            state.user_id = null
        }
    },
    actions: {
        loginUser({ commit }, user_id) {
            commit('login', user_id)
        },
        logoutUser({ commit }) {
            commit('logout')
        },
        initApp({commit}) {
            const user_id = localStorage.getItem('user_id')
            if (user_id) {
                commit('login', user_id)
            }
        }
    },
    getters: {
        isAuthenticated: (state) => !!state.user_id
    },
});