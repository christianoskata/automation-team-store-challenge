import api from '@/services/api'

export default {
  postCsv(formData) {
    return api.post(`shoes/csv/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
    })
      .then(response => response.data)
  },
}