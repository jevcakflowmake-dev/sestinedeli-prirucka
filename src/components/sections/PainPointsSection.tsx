'use client'

import { motion } from 'framer-motion'
import { PAIN_POINTS } from '@/lib/content'
import SectionWrapper from '@/components/shared/SectionWrapper'
import SectionHeading from '@/components/shared/SectionHeading'
import { AnimatedStagger, AnimatedItem } from '@/components/shared/AnimatedSection'
import AnimatedSection from '@/components/shared/AnimatedSection'

export default function PainPointsSection() {
  return (
    <SectionWrapper className="bg-blush-100">
      <AnimatedSection>
        <SectionHeading
          title="Znáš tohle?"
          subtitle="Šestinedělí nikdo nepopsal doopravdy. Připravili tě na porod — ale ne na to, co přijde potom."
        />
      </AnimatedSection>

      <AnimatedStagger className="grid gap-6 md:grid-cols-3">
        {PAIN_POINTS.map((point) => (
          <AnimatedItem key={point.headline}>
            <motion.div
              className="group h-full rounded-2xl bg-white/70 p-6 shadow-sm backdrop-blur-sm transition-all"
              whileHover={{ y: -6, boxShadow: '0 20px 40px rgba(61,53,48,0.1)', backgroundColor: 'rgba(255,255,255,0.9)' }}
              transition={{ duration: 0.3 }}
            >
              <motion.div
                className="mb-3 text-4xl"
                whileHover={{ scale: 1.2, rotate: 10 }}
                transition={{ type: 'spring', stiffness: 400 }}
              >
                {point.icon}
              </motion.div>
              <h3 className="mb-2 font-serif text-lg font-bold text-warm-900">{point.headline}</h3>
              <p className="text-sm leading-relaxed text-warm-900/60">{point.description}</p>
            </motion.div>
          </AnimatedItem>
        ))}
      </AnimatedStagger>

      <AnimatedSection delay={0.3}>
        <p className="mt-10 text-center text-lg font-medium text-warm-900/70">
          Tato příručka je pro tebe. Jasná. Konkrétní. Čitelná jednou rukou ve 3&nbsp;ráno.
        </p>
      </AnimatedSection>

      <div className="absolute bottom-0 left-0 w-full">
        <svg viewBox="0 0 1440 60" className="w-full" preserveAspectRatio="none">
          <path d="M0,30 C480,60 960,0 1440,30 L1440,60 L0,60 Z" fill="#FDF3D3" />
        </svg>
      </div>
    </SectionWrapper>
  )
}
