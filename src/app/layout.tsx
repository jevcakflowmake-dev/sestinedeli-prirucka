import type { Metadata } from 'next'
import { Playfair_Display, DM_Sans } from 'next/font/google'
import './globals.css'

const playfair = Playfair_Display({
  subsets: ['latin'],
  variable: '--font-serif',
  display: 'swap',
})

const dmSans = DM_Sans({
  subsets: ['latin'],
  variable: '--font-sans',
  display: 'swap',
})

export const metadata: Metadata = {
  title: 'Šestinedělí s klidem — PDF příručka pro nové maminky',
  description:
    '85 stran praktických odpovědí na otázky, které tě budí ve 3 ráno. Kojení, spánek, emoce a péče o sebe — sepsáno s porodní asistentkou.',
  openGraph: {
    title: 'Šestinedělí s klidem — PDF příručka pro nové maminky',
    description: '85 stran praktických odpovědí. Kojení, spánek, emoce, péče o sebe.',
    type: 'website',
  },
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="cs" className={`${playfair.variable} ${dmSans.variable}`}>
      <body className="bg-cream-200 font-sans text-warm-900 antialiased">
        {children}
      </body>
    </html>
  )
}
