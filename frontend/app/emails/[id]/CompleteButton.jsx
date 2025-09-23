"use client";

import { useState } from "react";

export default function CompleteBox()
{
    return (
        <>
            <button
            type="button"
            className="bg-green-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-green-700 transition"
            onClick={() => alert("This doesnt work at the moment")} 
            >
                Mark As Complete
            </button>
        </>
    );
}