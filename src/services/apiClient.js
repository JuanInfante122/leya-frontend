import axios from 'axios'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1',
  timeout: 30000,
  headers: { 'Content-Type': 'application/json' }
})

apiClient.interceptors.request.use((config) => {
  const usuario = JSON.parse(localStorage.getItem('leya_usuario') || '{}')
  if (usuario?.token) {
    config.headers.Authorization = `Bearer ${usuario.token}`
  }
  return config
})

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('leya_usuario')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default apiClient
