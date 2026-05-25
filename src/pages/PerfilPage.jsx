import { useContext } from 'react'
import { useNavigate } from 'react-router-dom'
import { AuthContext } from '../context/AuthContext'
import Navbar from '../components/Navbar'

export default function PerfilPage() {
  const { usuario, logout } = useContext(AuthContext)
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/')
  }

  return (
    <div className="page">
      <Navbar />
      <main className="page__main perfil-page">
        <h2>Mi perfil</h2>
        <div className="perfil-card">
          <p><strong>Nombre:</strong> {usuario.nombre}</p>
          <p><strong>Email:</strong> {usuario.email}</p>
        </div>
        <button onClick={handleLogout} className="btn btn--danger">
          Cerrar sesión
        </button>
      </main>
    </div>
  )
}
