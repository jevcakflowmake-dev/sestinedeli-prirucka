import CtaButton from './CtaButton'

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-cream-300 bg-cream-200/90 backdrop-blur-sm">
      <div className="mx-auto flex max-w-5xl items-center justify-between px-4 py-3 md:px-8">
        <span className="font-serif text-lg font-bold text-warm-900">
          Šestinedělí s klidem
        </span>
        <CtaButton label="Koupit příručku" size="default" className="hidden sm:inline-block" />
      </div>
    </header>
  )
}
