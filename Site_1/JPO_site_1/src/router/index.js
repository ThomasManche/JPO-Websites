import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/Home.vue'
import Connected from '@/Main.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/connected',
      name: 'Main',
      component: Connected,
      props: route => ({
        username: route.query.username
      })
    }
  ]
})

export default router
