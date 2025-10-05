import Link from "next/link";
import {FetchTickets} from "../utils/api";
export default async function CompletedTickets() {
  const tickets = await FetchTickets();

  // filter closed tickets
  const completedTickets = tickets.filter((t) => t.status === "closed");

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Completed Tickets</h1>
      <ul className="space-y-3">
        {completedTickets.map((ticket) => (
          <li
            key={ticket.id}
            className="bg-white p-4 rounded-lg shadow flex justify-between items-center"
          >
            <div>
              <Link
                href={`/emails/${ticket.id}`}
                className="text-gray-700 font-medium hover:underline"
              >
                [Ticket #{ticket.ticket_number}] {ticket.mail_subject}
              </Link>
              <p className="text-sm text-gray-600">From: {ticket.mail_from}</p>
            </div>
            <span className="bg-gray-300 text-gray-800 px-2 py-1 rounded-full text-xs">
              Closed
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}
