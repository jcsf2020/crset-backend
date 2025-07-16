import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'CRSET Solutions',
  description: 'Soluções tecnológicas sob medida para o teu negócio',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt">
      <body className="min-h-screen bg-gray-50">
        {children}
      </body>
    </html>
  )
}
