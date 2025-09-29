import Link from "next/link";
import ReplyBox from "./ReplyBox";
import CompleteBox from "./CompleteButton";

export default async function EmailDetail({ params }) {
  const {id} = await params;
  const ticketId = String(id);
  const res = await fetch(`http://127.0.0.1:8000/api/emails/${ticketId}/`, {
    cache: "no-store",
  });
  const email = await res.json();

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="bg-white shadow rounded-lg p-6 max-w-3xl mx-auto">
        <h1 className="text-xl font-bold text-gray-800 mb-4">
          {email.mail_subject}
        </h1>
       <p
              className={`inline-block px-3 py-1 rounded-full text-xs font-medium ${
            email.status === "open"
              ? "bg-green-200 text-green-800"
              : email.status === "in_progress"
              ? "bg-yellow-200 text-yellow-800"
              : "bg-gray-300 text-gray-800"
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

        <div className="border rounded-md p-4 bg-gray-300 mb-4">
          <p className="text-sm text-black">
            <strong>Body: </strong>
            {email.mail_text}
          </p>
        </div>

        {/* Pass the ID down here */}
        <ReplyBox ticketId={ticketId} />
          <div className="ml-auto justify-end">
           <CompleteBox ticketId={ticketId}/>
        </div>
       

        <Link
          href="/"
          className="text-blue-600 hover:underline text-sm font-medium"
        >
          ← Back to Inbox
        </Link>
      </div>
    </div>
  );
}
