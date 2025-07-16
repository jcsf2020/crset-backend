export const metadata = {
  title: 'CRSET Solutions',
  description: 'Soluções tecnológicas sob medida',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt">
      <body>{children}</body>
    </html>
  )
}
