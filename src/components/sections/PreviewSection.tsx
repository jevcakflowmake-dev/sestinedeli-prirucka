'use client'

import { motion } from 'framer-motion'
import SectionWrapper from '@/components/shared/SectionWrapper'
import SectionHeading from '@/components/shared/SectionHeading'
import AnimatedSection from '@/components/shared/AnimatedSection'

const PREVIEW_PAGES = [
  {
    title: 'Kojení bez slz',
    lines: ['Správné přiložení', 'Frekvence kojení', 'Kdy doplnit formulí', 'Jak poznat dostatek mléka'],
    color: 'from-blush-100 to-cream-200',
    rotate: '-6deg',
    delay: 0.1,
  },
  {
    title: 'Spánek pro přežití',
    lines: ['Cykly novorozence', 'Sdílení postele bezpečně', 'Spánek ve dne', 'Sleep regressions'],
    color: 'from-sage-100 to-cream-200',
    rotate: '2deg',
    delay: 0.2,
  },
  {
    title: 'Baby blues vs. PPD',
    lines: ['Symptomy baby blues', 'Kdy vyhledat pomoc', 'Podpůrné kontakty', 'Cvičení na emoce'],
    color: 'from-amber-50 to-cream-200',
    rotate: '-3deg',
    delay: 0.3,
  },
]

export default function PreviewSection() {
  return (
    <SectionWrapper className="relative overflow-hidden bg-sage-100" id="ukazka">
      {/* Background decoration */}
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div className="absolute -top-20 -left-20 h-64 w-64 rounded-full bg-sage-200/40 blur-3xl" />
        <div className="absolute -bottom-20 -right-20 h-64 w-64 rounded-full bg-cream-200/60 blur-3xl" />
      </div>

      <AnimatedSection>
        <SectionHeading
          title="Nahlédni dovnitř"
          subtitle="Každá strana je přehledná, praktická a čitelná i unavenou hlavou."
        />
      </AnimatedSection>

      <div className="relative flex flex-wrap justify-center gap-8 md:gap-12">
        {PREVIEW_PAGES.map((page, i) => (
          <motion.div
            key={page.title}
            className={`h-64 w-44 flex-shrink-0 rounded-2xl bg-gradient-to-b ${page.color} p-5 shadow-xl`}
            style={{ rotate: page.rotate }}
            initial={{ opacity: 0, y: 60, rotate: page.rotate }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: '-60px' }}
            transition={{ delay: page.delay, duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
            whileHover={{
              rotate: '0deg',
              scale: 1.08,
              boxShadow: '0 24px 48px rgba(61,53,48,0.18)',
              zIndex: 10,
            }}
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
          </motion.div>
        ))}
      </div>

      <AnimatedSection delay={0.4}>
        <p className="mt-12 text-center text-sm text-warm-900/50">
          + checklisty, tabulky a rychlé přehledy v každé kapitole
        </p>
      </AnimatedSection>
    </SectionWrapper>
  )
}
