export default function MessageBubble({ mensaje }) {
  const esLeya = mensaje.rol === 'leya'

  return (
    <div className={`message ${esLeya ? 'message--leya' : 'message--usuario'}`}>
      <div className="message__avatar">{esLeya ? '⚖️' : '👤'}</div>
      <div className="message__content">
        <p className="message__text">{mensaje.texto}</p>
        {esLeya && mensaje.fuentes?.length > 0 && (
          <div className="message__sources">
            <p className="sources__title">Fuentes:</p>
            <ul>
              {mensaje.fuentes.map((f, i) => (
                <li key={i}>
                  <a href={f.url} target="_blank" rel="noopener noreferrer">{f.norma}</a>
                </li>
              ))}
            </ul>
          </div>
        )}
        <span className="message__time">
          {new Date(mensaje.timestamp).toLocaleTimeString('es-CO', { hour: '2-digit', minute: '2-digit' })}
        </span>
      </div>
    </div>
  )
}
