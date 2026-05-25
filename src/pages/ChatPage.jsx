import ChatContainer from '../components/ChatContainer'
import Navbar from '../components/Navbar'

export default function ChatPage() {
  return (
    <div className="page">
      <Navbar />
      <main className="page__main">
        <ChatContainer />
      </main>
    </div>
  )
}
