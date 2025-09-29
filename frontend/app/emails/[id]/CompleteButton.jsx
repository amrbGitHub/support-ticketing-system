"use client";

import { useState } from "react";

export default function CompleteBox()
{
  const markComplete = async () => {
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/complete/${ticketId}/`, {
        method: "POST",
      });

      if (!res.ok) {
        const error = await res.json();
        alert(`Failed: ${error.error || "Unknown error"}`);
      } else {
        alert("Ticket marked as complete ✅");
        window.location.reload(); // refresh to show updated status
      }
    } catch (err) {
      alert("Error: " + err.message);
    }
  };
    return (
        <>
            <button
            type="button"
            className="bg-green-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-green-700 transition"
            onClick={markComplete} 
            >
                Mark As Complete
            </button>
        </>
    );
}