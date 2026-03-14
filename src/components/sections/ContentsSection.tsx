'use client'

import { motion } from 'framer-motion'
import { CHAPTERS } from '@/lib/content'
import SectionWrapper from '@/components/shared/SectionWrapper'
import SectionHeading from '@/components/shared/SectionHeading'
import AnimatedSection, { AnimatedStagger, AnimatedItem } from '@/components/shared/AnimatedSection'

export default function ContentsSection() {
  return (
    <SectionWrapper id="obsah" className="relative bg-cream-200">
      <AnimatedSection>
        <SectionHeading
          title="Co najdeš uvnitř"
          subtitle="11 kapitol napsaných tak, aby každá odpověděla na otázky, které ti nikdo jiný neodpoví."
        />
      </AnimatedSection>

      <AnimatedStagger className="grid gap-3 sm:grid-cols-2">
        {CHAPTERS.map((chapter) => (
          <AnimatedItem key={chapter.number}>
            <motion.div
              className="flex gap-4 rounded-2xl border border-cream-300 bg-cream-50 p-5 transition-all"
              whileHover={{ scale: 1.02, borderColor: '#F9ADAD', backgroundColor: 'rgba(253,232,232,0.4)' }}
              transition={{ duration: 0.2 }}
            >
              <motion.div
                className="flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-full bg-blush-200 font-serif text-sm font-bold text-blush-500"
                whileHover={{ scale: 1.15, backgroundColor: '#F9ADAD' }}
                transition={{ type: 'spring', stiffness: 400 }}
              >
                {chapter.number}
              </motion.div>
              <div>
                <div className="font-semibold text-warm-900">{chapter.title}</div>
                <div className="mt-0.5 text-sm text-warm-900/55">{chapter.subtitle}</div>
              </div>
            </motion.div>
          </AnimatedItem>
        ))}
      </AnimatedStagger>
    </SectionWrapper>
  )
}
