export async function FetchTickets(){
    const API_URL= process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";
    const res = await fetch(`${API_URL}/api/emails`, {
        cache: "no-store",
});

  if (!res.ok) {
    throw new Error(`Failed to fetch tickets: ${res.status} ${res.statusText}`);
  }

  const data = await res.json();

  return Array.isArray(data) ? data : data.results || [];
}