// import Vue from 'vue'
// import VueRouter from 'vue-router'
//
// import ShoesComponent from '@/components/ShoesComponent.vue'
//
// const routes = [
//   {path: '*', component: ShoesComponent}
// ]
//
// Vue.use(VueRouter)
// const router = new VueRouter({
//   scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
//   mode: 'history',
//   routes
// })
//
// export default router


import Vue from 'vue'
import Router from 'vue-router'
import Shoes from "@/components/Shoes";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'shoes',
      component: Shoes
    }
  ]
})