'use client'

import { motion } from 'framer-motion'
import { FAQ_ITEMS } from '@/lib/content'
import SectionWrapper from '@/components/shared/SectionWrapper'
import SectionHeading from '@/components/shared/SectionHeading'
import AnimatedSection, { AnimatedStagger, AnimatedItem } from '@/components/shared/AnimatedSection'
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion'

export default function FaqSection() {
  return (
    <SectionWrapper className="bg-cream-200">
      <AnimatedSection>
        <SectionHeading title="Časté otázky" />
      </AnimatedSection>
      <div className="mx-auto max-w-2xl">
        <Accordion multiple={false} className="space-y-3">
          {FAQ_ITEMS.map((item, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 16 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '-40px' }}
              transition={{ delay: i * 0.07, duration: 0.45 }}
            >
              <AccordionItem
                value={`item-${i}`}
                className="rounded-2xl border border-cream-300 bg-white/70 px-5 shadow-sm transition-shadow hover:shadow-md"
              >
                <AccordionTrigger className="py-4 font-semibold text-warm-900 hover:no-underline">
                  {item.question}
                </AccordionTrigger>
                <AccordionContent className="pb-4 leading-relaxed text-warm-900/65">
                  {item.answer}
                </AccordionContent>
              </AccordionItem>
            </motion.div>
          ))}
        </Accordion>
      </div>
    </SectionWrapper>
  )
}
