import SectionWrapper from '@/components/shared/SectionWrapper'
import SectionHeading from '@/components/shared/SectionHeading'

const PREVIEW_PAGES = [
  {
    title: 'Kojení bez slz',
    lines: ['Správné přiložení', 'Frekvence kojení', 'Kdy doplnit formulí', 'Jak poznat dostatek mléka'],
    color: 'from-blush-100 to-cream-200',
    rotate: '-rotate-2',
  },
  {
    title: 'Spánek pro přežití',
    lines: ['Cykly novorozence', 'Sdílení postele bezpečně', 'Spánek ve dne', 'Sleep regressions'],
    color: 'from-sage-100 to-cream-200',
    rotate: 'rotate-1',
  },
  {
    title: 'Baby blues vs. PPD',
    lines: ['Symptomy baby blues', 'Kdy vyhledat pomoc', 'Podpůrné kontakty', 'Cvičení na emoce'],
    color: 'from-amber-50 to-cream-200',
    rotate: '-rotate-1',
  },
]

export default function PreviewSection() {
  return (
    <SectionWrapper className="bg-sage-100" id="ukazka">
      <SectionHeading
        title="Nahlédni dovnitř"
        subtitle="Každá strana je přehledná, praktická a čitelná i unavenou hlavou."
      />
      <div className="flex flex-wrap justify-center gap-6 md:gap-10">
        {PREVIEW_PAGES.map((page) => (
          <div
            key={page.title}
            className={`${page.rotate} h-64 w-44 flex-shrink-0 rounded-2xl bg-gradient-to-b ${page.color} p-5 shadow-xl transition-transform hover:scale-105 hover:rotate-0`}
          >
            <div className="mb-3 font-serif text-sm font-bold text-warm-900">{page.title}</div>
            <ul className="space-y-2">
              {page.lines.map((line) => (
                <li key={line} className="flex items-start gap-1.5 text-xs text-warm-900/65">
                  <span className="mt-0.5 text-sage-400">✓</span>
                  {line}
                </li>
              ))}
            </ul>
            <div className="mt-4 h-1 w-full rounded-full bg-white/50" />
            <div className="mt-2 h-1 w-3/4 rounded-full bg-white/30" />
            <div className="mt-2 h-1 w-1/2 rounded-full bg-white/20" />
          </div>
        ))}
      </div>
      <p className="mt-10 text-center text-sm text-warm-900/50">
        + checklisty, tabulky a rychlé přehledy v každé kapitole
      </p>
    </SectionWrapper>
  )
}
