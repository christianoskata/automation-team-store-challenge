import api from '@/services/api'

export default {
  fetchShoes() {
    return api.get(`shoes/`)
              .then(response => response.data)
  },
  postShoe(payload) {
    return api.post(`shoes/`, payload)
              .then(response => response.data)
  },
  deleteShoe(msgId) {
    return api.delete(`shoes/${msgId}`)
              .then(response => response.data)
  }
}