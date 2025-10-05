import Link from "next/link";
import {FetchTickets} from "@/lib/api";
export default async function ActiveTickets() {

  const tickets = await FetchTickets();
  // filter open tickets
  const activeTickets = tickets.filter((t) => t.status === "open");

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Active Tickets</h1>
      <ul className="space-y-3">
        {activeTickets.map((ticket) => (
          <li
            key={ticket.id}
            className="bg-white p-4 rounded-lg shadow flex justify-between items-center"
          >
            <div>
              <Link
                href={`/emails/${ticket.id}`}
                className="text-blue-600 font-medium hover:underline"
              >
                [Ticket #{ticket.ticket_number}] {ticket.mail_subject}
              </Link>
              <p className="text-sm text-gray-600">From: {ticket.mail_from}</p>
            </div>
            <span className="bg-green-200 text-green-800 px-2 py-1 rounded-full text-xs">
              Open
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}
