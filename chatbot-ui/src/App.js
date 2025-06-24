import { useState } from "react";
import "./App.css";
import { fetchD20, fetch2D20 } from "./api";

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

  const roll2D20 = async () => {
    try {
      const results = await fetch2D20();
      setMessages((msgs) => [
        ...msgs,
        `\ud83c\udf00 You rolled ${results[0]} and ${results[1]}`,
      ]);
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
      <button
        onClick={roll2D20}
        className="px-4 py-2 mb-4 ml-2 rounded shadow hover:bg-gray-200"
      >
        Roll 2d20
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
