// chatbot-ui/src/api.js
const API_BASE = import.meta.env.VITE_BACKEND_URL || "";

// ──────────── simple GET helpers ────────────
export async function fetchD20() {
  const res = await fetch(`${API_BASE}/roll/1d20`);
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  const { result } = await res.json();
  return result;
}

export async function fetch2D20() {
  const res = await fetch(`${API_BASE}/roll/2d20`);
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  const { results } = await res.json();
  return results;
}

// ─────────── main chat dispatcher ───────────
export async function sendMessage(message) {
  const trimmed = message.trim().toLowerCase();

  // | create scenario  →  GET /scenario_elements
  if (trimmed.startsWith("|") && trimmed.slice(1).trim() === "create scenario") {
    const res = await fetch(`${API_BASE}/scenario_elements`);
    if (!res.ok) throw new Error(`API error: ${res.status}`);
    return await res.json(); // { scenario, prompt }
  }

  // | test  →  just forward to /chat; backend returns "Test Satisfactory"
  if (trimmed.startsWith("|") && trimmed.slice(1).trim() === "test") {
    const res = await fetch(`${API_BASE}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });
    if (!res.ok) throw new Error(`API error: ${res.status}`);
    return await res.json(); // { response }
  }

  // all other messages  →  normal chat POST
  const res = await fetch(`${API_BASE}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return await res.json();
}
