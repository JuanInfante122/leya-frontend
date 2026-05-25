import { useNavigate } from 'react-router-dom'
import { useContext } from 'react'
import { AuthContext } from '../context/AuthContext'

export default function LandingPage() {
  const navigate = useNavigate()
  const { usuario } = useContext(AuthContext)

  return (
    <div className="landing">
      <header className="landing__hero">
        <h1>⚖️ Leya</h1>
        <p className="landing__tagline">
          Tu orientadora legal inteligente — gratuita, clara y siempre disponible.
        </p>
        <p className="landing__disclaimer">
          Leya orienta sobre derecho laboral colombiano. Sus respuestas son
          informativas y no reemplazan la asesoría de un abogado.
        </p>
        <div className="landing__actions">
          <button onClick={() => navigate(usuario ? '/chat' : '/login')} className="btn btn--primary">
            {usuario ? 'Ir al chat' : 'Comenzar gratis'}
          </button>
          <button onClick={() => navigate('/chat')} className="btn btn--secondary">
            Consultar sin cuenta
          </button>
        </div>
      </header>
    </div>
  )
}
