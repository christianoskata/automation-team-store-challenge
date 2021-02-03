import shoeService from '../../services/shoeService'

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
  },
  addShoe({ commit }, shoe) {
    shoeService.postShoe(shoe)
    .then(() => {
      commit('addShoe', shoe)
    })
  },
  deleteShoe( { commit }, shoeId) {
    shoeService.deleteShoe(shoeId)
    commit('deleteShoe', shoeId)
  }
}

const mutations = {
  setShoes (state, shoes) {
    state.shoes = shoes
  },
  addShoe(state, shoe) {
    state.shoes.push(shoe)
  },
  deleteShoe(state, shoeId) {
    state.shoes = state.shoes.filter(obj => obj.pk !== shoeId)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
