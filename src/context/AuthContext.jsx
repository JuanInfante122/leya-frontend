import { createContext, useState, useEffect } from 'react'

export const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [usuario, setUsuario] = useState(null)
  const [cargando, setCargando] = useState(true)

  useEffect(() => {
    const sesionGuardada = localStorage.getItem('leya_usuario')
    if (sesionGuardada) {
      try {
        setUsuario(JSON.parse(sesionGuardada))
      } catch {
        localStorage.removeItem('leya_usuario')
      }
    }
    setCargando(false)
  }, [])

  const loginUsuario = (datosUsuario) => {
    setUsuario(datosUsuario)
    localStorage.setItem('leya_usuario', JSON.stringify(datosUsuario))
  }

  const logout = () => {
    setUsuario(null)
    localStorage.removeItem('leya_usuario')
  }

  if (cargando) return <div className="loading-screen">Cargando Leya...</div>

  return (
    <AuthContext.Provider value={{ usuario, loginUsuario, logout }}>
      {children}
    </AuthContext.Provider>
  )
}
