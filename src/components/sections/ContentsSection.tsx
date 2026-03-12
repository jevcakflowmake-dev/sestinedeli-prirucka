import { CHAPTERS } from '@/lib/content'
import SectionWrapper from '@/components/shared/SectionWrapper'
import SectionHeading from '@/components/shared/SectionHeading'

export default function ContentsSection() {
  return (
    <SectionWrapper id="obsah" className="bg-cream-200">
      <SectionHeading
        title="Co najdeš uvnitř"
        subtitle="11 kapitol napsaných tak, aby každá odpověděla na otázky, které ti nikdo jiný neodpoví."
      />
      <div className="grid gap-4 sm:grid-cols-2">
        {CHAPTERS.map((chapter) => (
          <div
            key={chapter.number}
            className="flex gap-4 rounded-2xl border border-cream-300 bg-cream-50 p-5 transition-shadow hover:shadow-md"
          >
            <div className="flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-full bg-blush-200 font-serif text-sm font-bold text-blush-500">
              {chapter.number}
            </div>
            <div>
              <div className="font-semibold text-warm-900">{chapter.title}</div>
              <div className="mt-0.5 text-sm text-warm-900/55">{chapter.subtitle}</div>
            </div>
          </div>
        ))}
      </div>
    </SectionWrapper>
  )
}
