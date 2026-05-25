import { useState } from 'react'

export default function QueryInput({ onSend, disabled }) {
  const [texto, setTexto] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!texto.trim()) return
    onSend(texto.trim())
    setTexto('')
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSubmit(e)
    }
  }

  return (
    <form className="query-input" onSubmit={handleSubmit}>
      <textarea
        value={texto}
        onChange={(e) => setTexto(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Escribe tu consulta legal... (Ej: ¿Cuánto tiempo tengo para demandar a mi empleador?)"
        disabled={disabled}
        rows={3}
        maxLength={500}
      />
      <button type="submit" disabled={disabled || !texto.trim()}>
        {disabled ? 'Consultando...' : 'Consultar a Leya'}
      </button>
    </form>
  )
}
