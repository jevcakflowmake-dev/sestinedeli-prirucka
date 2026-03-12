import { PAIN_POINTS } from '@/lib/content'
import SectionWrapper from '@/components/shared/SectionWrapper'
import SectionHeading from '@/components/shared/SectionHeading'

export default function PainPointsSection() {
  return (
    <SectionWrapper className="bg-blush-100">
      <SectionHeading
        title="Znáš tohle?"
        subtitle="Šestinedělí nikdo nepopsal doopravdy. Připravili tě na porod — ale ne na to, co přijde potom."
      />
      <div className="grid gap-6 md:grid-cols-3">
        {PAIN_POINTS.map((point) => (
          <div
            key={point.headline}
            className="rounded-2xl bg-white/70 p-6 shadow-sm backdrop-blur-sm"
          >
            <div className="mb-3 text-4xl">{point.icon}</div>
            <h3 className="mb-2 font-serif text-lg font-bold text-warm-900">{point.headline}</h3>
            <p className="text-sm leading-relaxed text-warm-900/60">{point.description}</p>
          </div>
        ))}
      </div>
      <p className="mt-10 text-center text-lg font-medium text-warm-900/70">
        Tato příručka je pro tebe. Jasná. Konkrétní. Čitelná jednou rukou ve 3 ráno.
      </p>
    </SectionWrapper>
  )
}
