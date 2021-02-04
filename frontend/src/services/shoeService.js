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
  deleteShoe(id) {
    return api.delete(`shoes/${id}`)
              .then(response => response.data)
  }
}