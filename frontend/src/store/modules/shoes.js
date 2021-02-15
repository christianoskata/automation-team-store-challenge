import shoeService from '@/services/shoeService'
import router from '@/router'

const state = {
  shoes: [],
  shoe: '',
  show: false,
  search: '',
}

const getters = {
  shoes: state => {
    return state.shoes
  },
  shoe: state => {
    return state.shoe
  },
}

const actions = {
  getShoes ({ commit }, params) {
    shoeService.fetchShoes(params)
    .then(shoes => {
      commit('setShoes', shoes)
    })
    .catch(e => { console.log(e) })
  },
  getShoe ({ commit }, id) {
    shoeService.detailShoe(id)
    .then(shoe => {
      commit('setShoe', shoe)
      router.push({ name: 'shoeDetail', params: { id: id }, })
    })
    .catch(e => { console.log(e) })
  },
  addShoe({ commit }, payload) {
    shoeService.postShoe(payload)
    .then(() => {
      commit('addShoe', payload)
      commit('setShow', true)
    })
    .catch(e => { console.log(e) })
  },
  updateShoe({ commit }, shoe) {
    shoeService.putShoe(shoe.id, shoe)
    .then(() => {
      commit('setShoe', shoe)
      commit('setShow', true)
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
    state.shoe = shoe
  },
  setShow (state, status) {
    state.show = status
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
