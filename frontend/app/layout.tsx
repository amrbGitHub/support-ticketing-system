import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Link from "next/link";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Email Database Viewer",
  description: "Simple UI to view the emails",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
    return (
    <html lang="en">
      <body className="flex min-h-screen bg-gray-100">
        {/* Sidebar */}
        <aside className="w-64 bg-gray-300 shadow-md border-r">
          <div className="p-6">
            <h1 className="text-2xl font-bold text-blue-600">Support Tickets</h1>
          </div>
          <nav className="px-6 space-y-3">
            <Link href="/active" className="block text-gray-700 hover:text-blue-600 font-medium">
              📬 Active Tickets
            </Link>
            <Link href="/completed" className="block text-gray-700 hover:text-blue-600 font-medium">
              📁 Completed Tickets
            </Link>
          </nav>
        </aside>

        {/* Main content */}
        <main className="flex-1 p-8">{children}</main>
      </body>
    </html>
  );
}
