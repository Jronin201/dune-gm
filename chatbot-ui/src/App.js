import { useState } from "react";
import "./App.css";
import { fetchD20, fetch2D20, sendMessage } from "./api";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

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

  const sendChat = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    try {
      const data = await sendMessage(input);
      if (data.response) {
        setMessages((msgs) => [...msgs, data.response]);
      } else if (data.scenario) {
        const lines = Object.entries(data.scenario)
          .map(([k, v]) => `- ${k}: ${v}`)
          .join("\n");
        setMessages((msgs) => [...msgs, `${lines}\n${data.prompt}`]);
      } else {
        setMessages((msgs) => [...msgs, JSON.stringify(data)]);
      }
    } catch (err) {
      setMessages((msgs) => [...msgs, `\u274c Command failed: ${err.message}`]);
    }
    setInput("");
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
      <form onSubmit={sendChat} data-testid="command-form" className="mt-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter command"
          className="border p-2 rounded w-64"
        />
        <button
          type="submit"
          className="ml-2 px-4 py-2 rounded shadow hover:bg-gray-200"
        >
          Send
        </button>
      </form>
    </div>
  );
}

export default App;
