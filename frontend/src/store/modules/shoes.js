import shoeService from '@/services/shoeService'
import router from '@/router'

const state = {
  shoes: [],
  shoe: '',
  success: false
}

const getters = {
  shoes: state => {
    return state.shoes
  },
  shoe: state => {
    return state.shoe
  },
  isSuccess: state => {
    return state.success
  }
}

const actions = {
  getShoes ({ commit }) {
    shoeService.fetchShoes()
    .then(shoes => {
      commit('setShoes', shoes)
    })
    .catch(e => { console.log(e) })
  },
  getShoe ({ commit }, id) {
    shoeService.detailShoe(id)
    .then(shoe => {
      commit('setSuccess', false)
      commit('setShoe', shoe)
      router.push({ name: 'shoeDetail', params: { id: id }, })
    })
    .catch(e => { console.log(e) })
  },
  addShoe({ commit }, payload) {
    shoeService.postShoe(payload)
    .then(() => {
      commit('addShoe', payload)
    })
    .catch(e => { console.log(e) })
  },
  updateShoe({ commit }, shoe) {
    console.log(`1 - Module updateShoe: ${shoe.id} ${shoe}`)
    shoeService.putShoe(shoe.id, shoe)
    .then(() => {
      commit('setShoe', shoe)
      commit('setSuccess', true)
    })
    .catch(e => { console.log(e) })
  },
  deleteShoe({ commit }, id) {
    shoeService.deleteShoe(id)
    .then(() => {
      commit('deleteShoe', id)
    })
    .catch(e => { console.log(e) })
  }
}

const mutations = {
  setShoes (state, shoes) {
    state.shoes = shoes
  },
  setShoe (state, shoe) {
    console.log(`3 - mutation setShoe ${shoe}`)
    state.shoe = shoe
  },
  setSuccess (state, status) {
    state.success = status
  },
  addShoe (state, shoe) {
    state.shoes.push(shoe)
  },
  deleteShoe (state, id) {
    state.shoes = state.shoes.filter(obj => obj.id !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
