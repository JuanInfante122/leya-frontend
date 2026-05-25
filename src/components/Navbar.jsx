import { useContext } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { AuthContext } from '../context/AuthContext'

export default function Navbar() {
  const { usuario, logout } = useContext(AuthContext)
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/')
  }

  return (
    <nav className="navbar">
      <Link to="/" className="navbar__brand">⚖️ Leya</Link>
      <div className="navbar__links">
        <Link to="/chat">Chat</Link>
        {usuario && <Link to="/historial">Historial</Link>}
        {usuario && <Link to="/perfil">Perfil</Link>}
        {usuario ? (
          <button onClick={handleLogout} className="navbar__logout">Salir</button>
        ) : (
          <Link to="/login" className="btn btn--primary">Ingresar</Link>
        )}
      </div>
    </nav>
  )
}
