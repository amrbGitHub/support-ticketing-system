"use client";

export default function CompleteBox({ ticketId }) {
  const handleComplete = async () => {
    await fetch(`http://127.0.0.1:8000/api/emails/${ticketId}/`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ status: "closed" }),
    });
    window.location.reload(); // refresh to show updated status
  };

  return (
    <button
      onClick={handleComplete}
      className="bg-green-500 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-green-600 transition"
    >
      Mark as Complete
    </button>
  );
}
