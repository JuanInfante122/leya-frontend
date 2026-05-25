import { useState, useEffect, useContext, useReducer } from 'react'
import { AuthContext } from '../context/AuthContext'
import { consultarLeya } from '../services/leyaService'

const chatReducer = (state, action) => {
  switch (action.type) {
    case 'ADD_MESSAGE':
      return { ...state, messages: [...state.messages, action.payload] }
    case 'SET_LOADING':
      return { ...state, isLoading: action.payload }
    case 'CLEAR':
      return { messages: [], isLoading: false }
    default:
      return state
  }
}

export function useLeyaChat() {
  const [state, dispatch] = useReducer(chatReducer, {
    messages: [],
    isLoading: false
  })
  const [sessionId] = useState(() => crypto.randomUUID())
  const { usuario } = useContext(AuthContext)

  useEffect(() => {
    dispatch({
      type: 'ADD_MESSAGE',
      payload: {
        id: crypto.randomUUID(),
        rol: 'leya',
        texto: `¡Hola${usuario ? ', ' + usuario.nombre : ''}! Soy Leya, tu asistente de orientación legal laboral. ¿En qué puedo ayudarte hoy?\n\n⚠️ Recuerda que mis respuestas son orientativas y no reemplazan la asesoría de un abogado.`,
        fuentes: [],
        timestamp: new Date()
      }
    })
  }, [])

  const sendQuery = async (pregunta) => {
    if (!pregunta.trim() || state.isLoading) return

    dispatch({
      type: 'ADD_MESSAGE',
      payload: { id: crypto.randomUUID(), rol: 'usuario', texto: pregunta, timestamp: new Date() }
    })
    dispatch({ type: 'SET_LOADING', payload: true })

    try {
      const respuesta = await consultarLeya(pregunta, sessionId)
      dispatch({
        type: 'ADD_MESSAGE',
        payload: {
          id: crypto.randomUUID(),
          rol: 'leya',
          texto: respuesta.respuesta,
          fuentes: respuesta.fuentes || [],
          timestamp: new Date()
        }
      })
    } catch {
      dispatch({
        type: 'ADD_MESSAGE',
        payload: {
          id: crypto.randomUUID(),
          rol: 'leya',
          texto: 'Lo siento, ocurrió un error al procesar tu consulta. Por favor intenta nuevamente.',
          fuentes: [],
          timestamp: new Date(),
          esError: true
        }
      })
    } finally {
      dispatch({ type: 'SET_LOADING', payload: false })
    }
  }

  return { messages: state.messages, isLoading: state.isLoading, sendQuery, sessionId }
}
