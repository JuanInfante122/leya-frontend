import { useRef, useEffect } from 'react'
import { useLeyaChat } from '../hooks/useLeyaChat'
import MessageBubble from './MessageBubble'
import QueryInput from './QueryInput'

export default function ChatContainer() {
  const { messages, isLoading, sendQuery } = useLeyaChat()
  const bottomRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  return (
    <div className="chat-wrapper">
      <div className="messages-area">
        {messages.map((msg) => (
          <MessageBubble key={msg.id} mensaje={msg} />
        ))}
        {isLoading && (
          <div className="typing-indicator">
            <span></span><span></span><span></span>
          </div>
        )}
        <div ref={bottomRef} />
      </div>
      <QueryInput onSend={sendQuery} disabled={isLoading} />
    </div>
  )
}
