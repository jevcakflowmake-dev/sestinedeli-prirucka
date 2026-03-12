import CtaButton from '@/components/shared/CtaButton'

export default function FooterSection() {
  return (
    <footer className="bg-warm-900 py-16 text-white/70">
      <div className="mx-auto max-w-5xl px-4 md:px-8">
        <div className="flex flex-col items-center gap-6 text-center">
          <span className="font-serif text-2xl font-bold text-white">Šestinedělí s klidem</span>
          <p className="max-w-md text-sm leading-relaxed">
            Praktická příručka pro maminky s novorozenci — od porodu po 6. týden.
            Napsáno s porodní asistentkou, pro reálný život.
          </p>
          <CtaButton label="Stáhnout příručku za 499 Kč" />
          <div className="mt-4 flex flex-wrap justify-center gap-6 text-xs text-white/40">
            <a href="mailto:ahoj@sestinedeli-prirucka.cz" className="hover:text-white/70 transition-colors">
              ahoj@sestinedeli-prirucka.cz
            </a>
            <span>·</span>
            <a href="#" className="hover:text-white/70 transition-colors">
              Ochrana osobních údajů
            </a>
            <span>·</span>
            <a href="#" className="hover:text-white/70 transition-colors">
              Obchodní podmínky
            </a>
          </div>
          <p className="text-xs text-white/25">
            © {new Date().getFullYear()} Šestinedělí s klidem. Všechna práva vyhrazena.
          </p>
        </div>
      </div>
    </footer>
  )
}
