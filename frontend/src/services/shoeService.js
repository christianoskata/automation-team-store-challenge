import api from '@/services/api'

export default {
  fetchShoes(params) {
    return api.get(`shoes/`, { params: { search: params.search }})
              .then(response => response.data)
  },
  detailShoe(id) {
    return api.get(`shoes/${id}`)
              .then(response => response.data)
  },
  postShoe(payload) {
    return api.post(`shoes/`, payload)
              .then(response => response.data)
  },
  putShoe(id, payload) {
    return api.put(`shoes/${id}`, payload)
              .then(response => response.data)
  },
  deleteShoe(id) {
    return api.delete(`shoes/${id}`)
              .then(response => response.data)
  }
}