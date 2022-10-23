import { createRouter, createWebHistory } from 'vue-router'
import AP from './components/modules/App2.vue'
import HOME from './components/modules/home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HOME
  },
  {
    path: '/ap',
    name: 'ap',
    component: AP
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
export default router
