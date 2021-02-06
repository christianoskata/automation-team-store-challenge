import csvService from '@/services/csvService'

const state = {
  file: '',
  show: false
}

const getters = {
  show: state => {
    return state.show
  },
  file: state => {
    return state.file
  }
}

const actions = {
  handleFileUpload({ commit }, e){
    var files = e.target.files || e.dataTransfer.files;
    if (!files.length)
      return
    commit('setFile', files[0])
  },
  sendCsv({ commit }, file) {
    let formData = new FormData()
    formData.append('file', file)

    csvService.postCsv(formData)
      .then(function() {
        commit('setShow', true)
      })
      .catch(e => {
        console.log(e)
      })
  }
}

const mutations = {
  setShow (state, status) {
    state.show = status
  },
  setFile (state, file) {
    state.file = file
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}