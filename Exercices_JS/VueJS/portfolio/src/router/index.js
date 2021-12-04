import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/production',
    name: 'Production',
    component: () => import('../views/Production.vue')
  },
  {
    path: '/skills',
    name: 'Skills',
    component: () => import('../views/Skills.vue')
  },
  {
    path: '/cv',
    name: 'CV',
    component: () => import('../views/CV.vue')
  }

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
