import Vue from 'vue'
import VueRouter from 'vue-router'
import ShoesList from "@/components/ShoesList";
import Csv from "@/components/Csv";

Vue.use(VueRouter)

export default new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'shoes',
      component: ShoesList
    },
    {
      path: '/csv',
      name: 'csv',
      component: Csv
    }
  ]
})