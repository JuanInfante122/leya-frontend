import { useLeyaChat } from '../hooks/useLeyaChat'
import MessageList from './MessageList'
import QueryInput from './QueryInput'

export default function ChatContainer() {
  const { messages, isLoading, sendQuery } = useLeyaChat()

  return (
    <div className="chat-wrapper">
      <MessageList messages={messages} isLoading={isLoading} />
      <QueryInput onSend={sendQuery} disabled={isLoading} />
    </div>
  )
}
