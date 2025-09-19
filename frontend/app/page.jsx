export default async function Home() {
  const res = await fetch("http://127.0.0.1:8000/api/emails/", {
    cache: "no-store",
  });

  if (!res.ok) {
    const text = await res.text();
    console.error("Backend error:", text);
    throw new Error(`Failed to fetch: ${res.status}`);
  }

  const emails = await res.json();

  return (
    <div>
      <h1>Email Tickets</h1>
      <ul>
        {emails.map((email) => (
          <li key={email.id}>
            {email.mail_subject} — {email.mail_from}
            {email.mail_text}
          </li>
        ))}
      </ul>
    </div>
  );
}
