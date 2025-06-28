export async function fetchD20() {
  const res = await fetch('http://localhost:8000/roll/1d20');
  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  const data = await res.json();
  return data.result;
}

export async function fetch2D20() {
  const res = await fetch('http://localhost:8000/roll/2d20');
  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  const data = await res.json();
  return data.results;
}

export async function sendMessage(message) {
  const trimmed = message.trim();
  let url = 'http://localhost:8000/chat';
  let body = { message };

  if (
    trimmed.startsWith('|') &&
    trimmed.slice(1).trim().toLowerCase() === 'create scenario'
  ) {
    url = 'http://localhost:8000/generate_scenario';
    body = {};
  }

  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  return await res.json();
}
