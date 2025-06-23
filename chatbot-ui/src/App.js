import { useState } from "react";
import "./App.css";
import { fetchD20 } from "./api";

function App() {
  const [messages, setMessages] = useState([]);

  const rollD20 = async () => {
    try {
      const result = await fetchD20();
      setMessages((msgs) => [...msgs, `\ud83c\udf00 You rolled a ${result}`]);
    } catch (err) {
      setMessages((msgs) => [...msgs, `\u274c Roll failed: ${err.message}`]);
    }
  };

  return (
    <div className="App p-4">
      <h1 className="text-xl font-bold mb-4">Dune GM Chat UI</h1>
      <button
        onClick={rollD20}
        className="px-4 py-2 mb-4 rounded shadow hover:bg-gray-200"
      >
        Roll 1d20
      </button>
      <div className="chat-window border p-2 rounded">
        {messages.map((msg, i) => (
          <div key={i} className="mb-1">
            {msg}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
