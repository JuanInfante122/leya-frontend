import { useRef, useEffect } from 'react'
import MessageBubble from './MessageBubble'

export default function MessageList({ messages, isLoading }) {
  const bottomRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  return (
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
  )
}
