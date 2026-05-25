import { useState, useEffect } from 'react'
import { useLeyaChat } from '../hooks/useLeyaChat'
import MessageList from './MessageList'
import QueryInput from './QueryInput'

export default function ChatContainer() {
  const { messages, isLoading, sendQuery } = useLeyaChat()
  const [wakingUp, setWakingUp] = useState(false)

  useEffect(() => {
    if (!isLoading) {
      setWakingUp(false)
      return
    }
    const timer = setTimeout(() => setWakingUp(true), 6000)
    return () => clearTimeout(timer)
  }, [isLoading])

  return (
    <div className="chat-wrapper">
      {wakingUp && (
        <div className="wakeup-banner">
          ⏳ El servidor está despertando (Railway free tier — puede tardar hasta 30 s en la primera consulta)
        </div>
      )}
      <MessageList messages={messages} isLoading={isLoading} />
      <QueryInput onSend={sendQuery} disabled={isLoading} />
    </div>
  )
}
