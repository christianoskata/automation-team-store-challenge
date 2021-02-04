import Vue from 'vue'
import Vuex from 'vuex'
import shoes from '@/store/modules/shoes'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    shoes
  }
})
