import SectionWrapper from '@/components/shared/SectionWrapper'
import CtaButton from '@/components/shared/CtaButton'
import { Badge } from '@/components/ui/badge'

const INCLUDES = [
  '85 stran praktického obsahu',
  '11 kapitol od porodu po 6. týden',
  'Checklisty a tabulky ke každé kapitole',
  'Okamžité stažení ve formátu PDF',
  'Funguje na mobilu, tabletu i PC',
  '14denní záruka vrácení peněz',
]

export default function PricingSection() {
  return (
    <SectionWrapper id="cena" className="bg-blush-100">
      <div className="mx-auto max-w-lg text-center">
        <Badge className="mb-5 rounded-full border-0 bg-blush-500 px-4 py-1.5 text-sm font-semibold text-white">
          Sleva 37 % — jen nyní
        </Badge>
        <h2 className="font-serif text-3xl font-bold text-warm-900 md:text-4xl">
          Jeden nákup. Klid na celé šestinedělí.
        </h2>
        <div className="mt-6 flex items-baseline justify-center gap-3">
          <span className="font-serif text-5xl font-bold text-blush-500">499 Kč</span>
          <span className="text-xl text-warm-900/40 line-through">799 Kč</span>
        </div>
        <p className="mt-2 text-sm text-warm-900/50">jednorázová platba · žádné předplatné</p>

        <ul className="mt-8 space-y-3 text-left">
          {INCLUDES.map((item) => (
            <li key={item} className="flex items-center gap-3">
              <span className="flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full bg-sage-400 text-xs text-white">
                ✓
              </span>
              <span className="text-warm-900/75">{item}</span>
            </li>
          ))}
        </ul>

        <div className="mt-10">
          <CtaButton size="lg" className="w-full justify-center sm:w-auto" />
          <p className="mt-4 text-xs text-warm-900/40">
            Bezpečná platba · Okamžité stažení · 14denní záruka
          </p>
        </div>
      </div>
    </SectionWrapper>
  )
}
