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
