"use client";

import { useState } from "react";
import CompleteBox from "./CompleteButton";

export default function ReplyBox({ ticketId }) {
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!message.trim()) return;
    setLoading(true);

    try {
      const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000"
      const res = await fetch(`${API_URL}/api/reply/${ticketId}/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });

      if (!res.ok) {
        const error = await res.json();
        alert(`Failed to send: ${error.error || "Unknown error"}`);
      } else {
        alert("Reply sent!");
        setMessage("");
      }
    } catch (err) {
      alert("Error sending reply: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="border rounded-md p-4 bg-gray-50">
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Write a reply here..."
        className="w-full h-28 border rounded-md p-3 text-sm text-gray-700 resize-none focus:ring-2 focus:ring-blue-400 mb-3"
      />

      <div className="flex gap-2 items-center">
        <button
          type="button"
          disabled={loading}
          className={`px-4 py-2 rounded-md text-sm font-medium transition ${
            loading
              ? "bg-blue-300 text-white cursor-not-allowed"
              : "bg-blue-600 text-white hover:bg-blue-700"
          }`}
          onClick={handleSend}
        >
          {loading ? "Sending..." : "Send"}
        </button>

        <button
          type="button"
          className="bg-gray-300 text-gray-800 px-4 py-2 rounded-md text-sm font-medium hover:bg-gray-400 transition"
          onClick={() => setMessage("")}
        >
          Cancel
        </button>
            <CompleteBox ticketId={ticketId}/>
      </div>
    </div>
  );
}