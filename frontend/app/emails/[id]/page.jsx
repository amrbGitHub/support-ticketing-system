import Link from "next/link";
import ReplyBox from "./ReplyBox";

export default async function EmailDetail({ params }) {
  
  const ticketId = String(params.id);

  const res = await fetch(`http://127.0.0.1:8000/api/emails/${ticketId}/`, {
    cache: "no-store",
  });
  const email = await res.json();

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="bg-white shadow rounded-lg p-6 max-w-3xl mx-auto">
        <h1 className="text-xl font-bold text-gray-800 mb-4">
          [Ticket #{email.ticket_number}] {email.mail_subject}
        </h1>
            <p
                className={`inline-block px-3 py-1 rounded-full text-xs font-medium mb-4 ${
                email.status === "open"
                  ? "bg-yellow-200 text-yellow-800"
                  : "bg-green-300 text-green-800"
              }`}
            >
              {email.status}
            </p>

        <p className="text-sm text-gray-600 mb-2">
          <strong>From:</strong> {email.mail_from}
        </p>
        <p className="text-sm text-gray-600 mb-4">
          <strong>Date:</strong>{" "}
          {new Date(email.mail_date).toLocaleString()}
        </p>

        {/* Original message */}
        <div className="border rounded-md p-4 bg-gray-300 mb-4">
          <p className="text-sm text-black">
            <strong>Body: </strong>
            {email.mail_text}
          </p>
        </div>

        {/* Replies */}
        {email.replies && email.replies.length > 0 && (
          <div className="mt-6">
            <h2 className="text-lg font-semibold text-gray-800 mb-2">Replies</h2>
            <div className="space-y-3">
              {email.replies.map((reply) => (
                <div
                  key={reply.id}
                  className="border rounded-md p-3 bg-gray-50 text-sm"
                >
                  <p className="text-gray-700 whitespace-pre-line">
                    {reply.reply_text}
                  </p>
                  <p className="text-xs text-gray-500 mt-2">
                    From: {reply.reply_from} → {reply.reply_to} |{" "}
                    {new Date(reply.reply_date).toLocaleString()}
                  </p>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Reply box */}
        <div className="mt-6">
          <ReplyBox ticketId={ticketId} />
        </div>

        <Link
          href="/"
          className="text-blue-600 hover:underline text-sm font-medium mt-6 block"
        >
          ← Back to Inbox
        </Link>
      </div>
    </div>
  );
}
