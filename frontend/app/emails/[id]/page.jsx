import Link from "next/link";
import ReplyBox from "./ReplyBox";
export default async function EmailDetail({ params }) {
  const res = await fetch(`http://127.0.0.1:8000/api/emails/${params.id}/`, {
    cache: "no-store",
  });
  const email = await res.json();

 return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="bg-white shadow rounded-lg p-6 max-w-3xl mx-auto">
        <h1 className="text-xl font-bold text-gray-800 mb-4">
          {email.mail_subject}
        </h1>

        <p className="text-sm text-gray-600 mb-2">
          <strong>From:</strong> {email.mail_from}
        </p>

        <p className="text-sm text-gray-600 mb-4">
          <strong>Date:</strong>{" "}
          {new Date(email.mail_date).toLocaleString()}
        </p>
        <div className="border rounded-md p-4 bg-gray-300">
        <p className="text-sm text-black mb-4">
            <strong>Body: </strong>{email.mail_text}
        </p>
        </div>
       <ReplyBox />

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
