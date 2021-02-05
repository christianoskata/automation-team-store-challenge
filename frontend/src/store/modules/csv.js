import csvService from '@/services/csvService'

const state = {
  file: '',
  success: false
}

const getters = {
  isSuccess: state => {
    return state.success
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
        commit('setSuccess', true)
      })
      .catch(e => {
        console.log(e)
      })
  }
}

const mutations = {
  setSuccess (state, status) {
    state.success = status
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