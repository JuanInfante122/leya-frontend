export default function SourceList({ fuentes }) {
  if (!fuentes?.length) return null

  return (
    <div className="message__sources">
      <p className="sources__title">Fuentes:</p>
      <ul>
        {fuentes.map((f, i) => (
          <li key={i}>
            <a href={f.url} target="_blank" rel="noopener noreferrer">{f.norma}</a>
          </li>
        ))}
      </ul>
    </div>
  )
}
