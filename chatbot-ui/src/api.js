const API_BASE = import.meta.env.VITE_BACKEND_URL || '';

export async function fetchD20() {
  const res = await fetch(`${API_BASE}/roll/1d20`);
  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  const data = await res.json();
  return data.result;
}

export async function fetch2D20() {
  const res = await fetch(`${API_BASE}/roll/2d20`);
  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  const data = await res.json();
  return data.results;
}

export async function sendMessage(message) {
  const trimmed = message.trim();

  if (
    trimmed.startsWith('|') &&
    trimmed.slice(1).trim().toLowerCase() === 'create scenario'
  ) {
    const res = await fetch(`${API_BASE}/generate_scenario`);
    if (!res.ok) {
      throw new Error(`API error: ${res.status}`);
    }
    return await res.json();
  }

  if (trimmed.startsWith('|') && trimmed.slice(1).trim().toLowerCase() === 'test') {
    const res = await fetch(`${API_BASE}/test`);
    if (!res.ok) {
      throw new Error(`API error: ${res.status}`);
    }
    return await res.json();
  }

  const res = await fetch(`${API_BASE}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });

  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  return await res.json();
}
