import apiClient from './apiClient'

export const consultarLeya = async (pregunta, sessionId) => {
  const { data } = await apiClient.post('/consulta', {
    pregunta,
    session_id: sessionId
  })
  return data
}

export const obtenerHistorial = async (usuarioId) => {
  const { data } = await apiClient.get(`/historial/${usuarioId}`)
  return data
}

export const login = async (email, password) => {
  const { data } = await apiClient.post('/auth/login', { email, password })
  return data
}
