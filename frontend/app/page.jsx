"use client";
import { useEffect, useState } from "react";
import { useRouter, useSearchParams} from "next/navigation";

/*Fetch email data from server*/ 
async function getData(id)
{
  const res = await fetch(`http://127.0.0.1:8000/api/email/${id}/`)
  if (!res.ok)
  {
    throw new Error("Failed to fetch data");
  }
  return res.json()
}
export default function Home() {
  return (
    <div>

    </div>
  );
}
