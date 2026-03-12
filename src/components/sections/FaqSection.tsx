import { FAQ_ITEMS } from '@/lib/content'
import SectionWrapper from '@/components/shared/SectionWrapper'
import SectionHeading from '@/components/shared/SectionHeading'
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion'

export default function FaqSection() {
  return (
    <SectionWrapper className="bg-cream-200">
      <SectionHeading title="Časté otázky" />
      <div className="mx-auto max-w-2xl">
        <Accordion multiple={false} className="space-y-3">
          {FAQ_ITEMS.map((item, i) => (
            <AccordionItem
              key={i}
              value={`item-${i}`}
              className="rounded-2xl border border-cream-300 bg-white/70 px-5 shadow-sm"
            >
              <AccordionTrigger className="py-4 font-semibold text-warm-900 hover:no-underline">
                {item.question}
              </AccordionTrigger>
              <AccordionContent className="pb-4 text-warm-900/65 leading-relaxed">
                {item.answer}
              </AccordionContent>
            </AccordionItem>
          ))}
        </Accordion>
      </div>
    </SectionWrapper>
  )
}
