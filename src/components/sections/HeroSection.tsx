import { Badge } from '@/components/ui/badge'
import CtaButton from '@/components/shared/CtaButton'

export default function HeroSection() {
  return (
    <section className="overflow-hidden bg-cream-200 py-16 md:py-24">
      <div className="mx-auto max-w-5xl px-4 md:px-8">
        <div className="flex flex-col items-center gap-12 md:flex-row md:items-center">
          {/* Text */}
          <div className="flex-1 text-center md:text-left">
            <Badge className="mb-5 rounded-full border-0 bg-sage-200 px-4 py-1.5 font-sans text-sm font-medium text-sage-500">
              PDF příručka pro šestinedělí
            </Badge>
            <h1 className="font-serif text-4xl font-bold leading-tight text-warm-900 md:text-5xl lg:text-6xl">
              Šestinedělí
              <span className="block text-blush-500">bez chaosu</span>
            </h1>
            <p className="mt-5 text-lg leading-relaxed text-warm-900/65 md:text-xl">
              85 stránek praktických odpovědí na otázky, které tě budí ve 3 ráno.
              Kojení, spánek, emoce, péče o sebe — sepsáno s porodní asistentkou.
            </p>
            <div className="mt-8 flex flex-col items-center gap-4 sm:flex-row md:justify-start">
              <CtaButton size="lg" />
              <p className="text-sm text-warm-900/50">
                Okamžité stažení · 14denní záruka vrácení peněz
              </p>
            </div>
            <div className="mt-8 flex flex-wrap justify-center gap-6 md:justify-start">
              {[
                { num: '11', label: 'kapitol' },
                { num: '85', label: 'stran' },
                { num: '100%', label: 'praktické tipy' },
              ].map((item) => (
                <div key={item.label} className="text-center">
                  <div className="font-serif text-2xl font-bold text-blush-500">{item.num}</div>
                  <div className="text-sm text-warm-900/50">{item.label}</div>
                </div>
              ))}
            </div>
          </div>

          {/* Ilustrace / mockup */}
          <div className="relative flex-shrink-0">
            <div className="relative h-[340px] w-[260px] md:h-[420px] md:w-[320px]">
              {/* Shadow card */}
              <div className="absolute -bottom-3 -right-3 h-full w-full rounded-3xl bg-blush-200" />
              {/* Main card */}
              <div className="relative flex h-full w-full flex-col items-center justify-center rounded-3xl bg-gradient-to-b from-blush-100 to-cream-200 p-8 shadow-xl">
                <div className="mb-4 text-7xl">👶</div>
                <div className="text-center">
                  <div className="font-serif text-2xl font-bold text-warm-900">Šestinedělí</div>
                  <div className="font-serif text-xl font-bold text-blush-500">s klidem</div>
                  <div className="mt-2 text-xs text-warm-900/50">Kompletní příručka pro nové maminky</div>
                </div>
                <div className="mt-6 w-full space-y-2">
                  {['Kojení', 'Spánek', 'Emoce', 'Péče o tělo'].map((t) => (
                    <div key={t} className="flex items-center gap-2 rounded-lg bg-white/60 px-3 py-1.5">
                      <span className="text-sage-400">✓</span>
                      <span className="text-sm text-warm-900/70">{t}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
