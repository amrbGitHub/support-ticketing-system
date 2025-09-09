import  EmailTemplate from '@/components/email-template';
import { NextResponse } from 'next/server';
// import { Resend } from 'resend';

//const resend = new Resend(process.env.RESEND_API_KEY);
/*
export async function POST() {
  try {
    const { data, error } = await resend.emails.send({
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: 'Hello world',
      react: EmailTemplate({ firstName: 'Amr' }),
    });

    if (error) {
      return Response.json({ error }, { status: 500 });
    }

    return Response.json(data);
  } catch (error) {
    return Response.json({ error }, { status: 500 });
  }
}
  */
/*
export async function GET()
{
    try 
    {
        const {data} = await resend.emails.send({
            from: 
        });
    } 
    catch (error) 
    {
        return NextResponse.json({error});
    }
}
    */