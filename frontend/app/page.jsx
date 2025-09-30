import { redirect } from "next/navigation";

export default function Home() {
  // Always send user to active tickets
  redirect("/active");
}
