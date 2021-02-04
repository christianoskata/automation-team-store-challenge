import shoeService from '@/services/shoeService'

const state = {
  shoes: []
}

const getters = {
  shoes: state => {
    return state.shoes
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
  addShoe({ commit }, shoe) {
    shoeService.postShoe(shoe)
    .then(() => {
      commit('addShoe', shoe)
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
