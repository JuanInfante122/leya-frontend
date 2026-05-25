import { useState, useEffect, useContext } from 'react'
import { AuthContext } from '../context/AuthContext'
import { obtenerHistorial } from '../services/leyaService'
import Navbar from '../components/Navbar'

export default function HistorialPage() {
  const { usuario } = useContext(AuthContext)
  const [historial, setHistorial] = useState([])
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    obtenerHistorial(usuario.id)
      .then(setHistorial)
      .catch(() => setError('No se pudo cargar el historial.'))
      .finally(() => setCargando(false))
  }, [usuario.id])

  return (
    <div className="page">
      <Navbar />
      <main className="page__main historial-page">
        <h2>Historial de consultas</h2>
        {cargando && <p>Cargando...</p>}
        {error && <p className="error-msg">{error}</p>}
        {!cargando && !error && historial.length === 0 && (
          <p>No tienes consultas previas.</p>
        )}
        <ul className="historial-list">
          {historial.map((item, i) => (
            <li key={i} className="historial-item">
              <p className="historial-item__pregunta">{item.pregunta}</p>
              <p className="historial-item__fecha">
                {new Date(item.fecha).toLocaleDateString('es-CO')}
              </p>
            </li>
          ))}
        </ul>
      </main>
    </div>
  )
}
