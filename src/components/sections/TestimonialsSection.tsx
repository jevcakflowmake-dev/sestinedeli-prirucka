'use client'

import { motion } from 'framer-motion'
import { TESTIMONIALS } from '@/lib/content'
import SectionWrapper from '@/components/shared/SectionWrapper'
import SectionHeading from '@/components/shared/SectionHeading'
import AnimatedSection, { AnimatedStagger, AnimatedItem } from '@/components/shared/AnimatedSection'

export default function TestimonialsSection() {
  return (
    <SectionWrapper className="relative overflow-hidden bg-cream-200">
      {/* Large quote mark background */}
      <div className="pointer-events-none absolute left-8 top-8 font-serif text-[200px] leading-none text-blush-200/40 select-none">
        &ldquo;
      </div>

      <AnimatedSection>
        <SectionHeading
          title="Co říkají maminky"
          subtitle="Přes 400 maminek si příručku již stáhlo."
        />
      </AnimatedSection>

      <AnimatedStagger className="grid gap-6 md:grid-cols-3">
        {TESTIMONIALS.map((t) => (
          <AnimatedItem key={t.name}>
            <motion.div
              className="relative h-full rounded-2xl border-l-4 border-blush-300 bg-white/80 p-6 shadow-sm"
              whileHover={{ y: -4, boxShadow: '0 16px 40px rgba(61,53,48,0.1)', backgroundColor: 'rgba(255,255,255,0.95)' }}
              transition={{ duration: 0.3 }}
            >
              {/* Quote mark */}
              <span className="absolute right-4 top-3 font-serif text-5xl leading-none text-blush-200 select-none">
                &rdquo;
              </span>
              <p className="leading-relaxed text-warm-900/75">{t.text}</p>
              <div className="mt-5 flex items-center gap-3">
                <motion.div
                  className={`flex h-10 w-10 items-center justify-center rounded-full ${t.color} font-semibold text-warm-900/70`}
                  whileHover={{ scale: 1.1 }}
                >
                  {t.initials}
                </motion.div>
                <div>
                  <div className="font-semibold text-warm-900">{t.name}</div>
                  <div className="text-xs text-warm-900/50">{t.babyAge}</div>
                </div>
              </div>
            </motion.div>
          </AnimatedItem>
        ))}
      </AnimatedStagger>
    </SectionWrapper>
  )
}
