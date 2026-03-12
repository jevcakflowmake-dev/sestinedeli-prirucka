import { TESTIMONIALS } from '@/lib/content'
import SectionWrapper from '@/components/shared/SectionWrapper'
import SectionHeading from '@/components/shared/SectionHeading'

export default function TestimonialsSection() {
  return (
    <SectionWrapper className="bg-cream-200">
      <SectionHeading
        title="Co říkají maminky"
        subtitle="Přes 400 maminek si příručku již stáhlo."
      />
      <div className="grid gap-6 md:grid-cols-3">
        {TESTIMONIALS.map((t) => (
          <div
            key={t.name}
            className="rounded-2xl border-l-4 border-blush-300 bg-white/80 p-6 shadow-sm"
          >
            <p className="leading-relaxed text-warm-900/75">&ldquo;{t.text}&rdquo;</p>
            <div className="mt-5 flex items-center gap-3">
              <div
                className={`flex h-10 w-10 items-center justify-center rounded-full ${t.color} font-semibold text-warm-900/70`}
              >
                {t.initials}
              </div>
              <div>
                <div className="font-semibold text-warm-900">{t.name}</div>
                <div className="text-xs text-warm-900/50">{t.babyAge}</div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </SectionWrapper>
  )
}
