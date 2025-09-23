"use client";

import { useState } from "react";
import CompleteBox from "./CompleteButton";
export default function ReplyBox() {
  const [message, setMessage] = useState("");

  return (
    <div className="border rounded-md p-4 bg-gray-50">
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Write a reply here..."
        className="w-full h-28 border rounded-md p-3 text-sm text-gray-700 resize-none focus:ring-2 focus:ring-blue-400 mb-3"
      />
     
      <div className="flex gap-2">
       
        <button
          type="button"
          className="bg-blue-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-blue-700 transition"
          onClick={() => alert("This doesnt work at the moment")}
        >
          Send
        </button>
        <button
          type="button"
          className="bg-gray-300 text-gray-800 px-4 py-2 rounded-md text-sm font-medium hover:bg-gray-400 transition"
          onClick={() => setMessage("")}
        >
          Cancel
        </button>
        <div className="flex justify-end">
         <CompleteBox/>
      </div>
      </div>
    </div>
  );
}
