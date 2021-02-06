import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/words/:idVocabulary',
    name: 'Words',
    component: () => import('../views/Words.vue')
  },
  {
    path: '/home',
    name: 'Account',
    component: () => import('../views/Account.vue')
  },
  {
    path: '/training/:idVocabulary',
    name: 'Training',
    component: () => import('../views/Training.vue'),
    props: true
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
