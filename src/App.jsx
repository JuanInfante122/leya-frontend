import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { useContext } from 'react'
import { AuthProvider, AuthContext } from './context/AuthContext'
import LandingPage from './pages/LandingPage'
import LoginPage from './pages/LoginPage'
import ChatPage from './pages/ChatPage'
import HistorialPage from './pages/HistorialPage'
import PerfilPage from './pages/PerfilPage'

function RutaProtegida({ children }) {
  const { usuario } = useContext(AuthContext)
  return usuario ? children : <Navigate to="/login" replace />
}

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/chat" element={<ChatPage />} />
      <Route path="/historial" element={
        <RutaProtegida><HistorialPage /></RutaProtegida>
      } />
      <Route path="/perfil" element={
        <RutaProtegida><PerfilPage /></RutaProtegida>
      } />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <AppRoutes />
      </BrowserRouter>
    </AuthProvider>
  )
}
