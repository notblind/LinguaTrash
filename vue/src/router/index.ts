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
  },
  {
    path: '/feedback',
    name: 'Feedback',
    component: () => import('../views/Feedback.vue'),
  },
  {
    path: '/info',
    name: 'Info',
    component: () => import('../views/Info.vue'),
  },
  // {
  //   path: '/me',
  //   name: 'Me',
  //   component: () => import('../views/addition/Me.vue'),
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
