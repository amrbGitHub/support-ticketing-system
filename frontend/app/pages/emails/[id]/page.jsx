export default async function EmailDetail({ params }) {
  const res = await fetch(`http://127.0.0.1:8000/api/emails/${params.id}/`, {
    cache: "no-store",
  });
  const email = await res.json();

  return (
    <div>
      <h1>{email.mail_subject}</h1>
      <p><strong>From:</strong> {email.mail_from}</p>
      <p><strong>Date:</strong> {email.mail_date}</p>
      <p>{email.mail_text}</p>
    </div>
  );
}
