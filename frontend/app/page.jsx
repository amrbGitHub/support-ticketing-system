import Link from "next/link";
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
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">Active Support Tickets ⚙️</h1>

      <div className="bg-white shadow rounded-lg divide-y">
        {emails.map((email) => (
          <Link
            key={email.id}
            href={`/emails/${email.id}`}
            className="block hover:bg-gray-50 transition"
            >
            <div className="p-4 flex justify-between items-center">
              <div>
                <h2 className="font-semibold text-gray-900">
                  {email.mail_subject}
                </h2>
                <p className="text-sm text-gray-600">{email.mail_from}</p>
              </div>
              <span className="text-xs text-gray-500">
                {new Date(email.mail_date).toLocaleString()}
              </span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}