import SourceList from './SourceList'

export default function MessageBubble({ mensaje }) {
  const esLeya = mensaje.rol === 'leya'

  return (
    <div className={`message ${esLeya ? 'message--leya' : 'message--usuario'}`}>
      <div className="message__avatar">{esLeya ? '⚖️' : '👤'}</div>
      <div className="message__content">
        <p className="message__text">{mensaje.texto}</p>
        {esLeya && <SourceList fuentes={mensaje.fuentes} />}
        <span className="message__time">
          {new Date(mensaje.timestamp).toLocaleTimeString('es-CO', { hour: '2-digit', minute: '2-digit' })}
        </span>
      </div>
    </div>
  )
}
