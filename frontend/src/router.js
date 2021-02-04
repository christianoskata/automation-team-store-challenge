import Vue from 'vue'
import VueRouter from 'vue-router'
import Shoes from "@/components/Shoes";

Vue.use(VueRouter)

export default new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'shoes',
      component: Shoes
    }
  ]
})