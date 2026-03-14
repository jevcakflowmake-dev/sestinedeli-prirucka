'use client'

import { motion } from 'framer-motion'
import SectionWrapper from '@/components/shared/SectionWrapper'
import CtaButton from '@/components/shared/CtaButton'
import AnimatedSection from '@/components/shared/AnimatedSection'
import { Badge } from '@/components/ui/badge'

const INCLUDES = [
  '85 stran praktického obsahu',
  '11 kapitol od porodu po 6. týden',
  'Checklisty a tabulky ke každé kapitole',
  'Okamžité stažení ve formátu PDF',
  'Funguje na mobilu, tabletu i PC',
  '14denní záruka vrácení peněz',
]

export default function PricingSection() {
  return (
    <SectionWrapper id="cena" className="relative overflow-hidden bg-gradient-to-b from-blush-100 to-cream-100">
      {/* Background blobs */}
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute -top-16 left-1/2 h-64 w-64 -translate-x-1/2 rounded-full bg-blush-200/30 blur-3xl" />
        <div className="absolute -bottom-16 right-0 h-48 w-48 rounded-full bg-sage-200/30 blur-3xl" />
      </div>

      <AnimatedSection>
        <div className="relative mx-auto max-w-lg text-center">
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
          >
            <Badge className="mb-5 rounded-full border-0 bg-blush-500 px-4 py-1.5 text-sm font-semibold text-white shadow-md">
              🔥 Sleva 37 % — jen nyní
            </Badge>
          </motion.div>

          <h2 className="font-serif text-3xl font-bold text-warm-900 md:text-4xl">
            Jeden nákup. Klid na celé šestinedělí.
          </h2>

          <motion.div
            className="mt-8 flex items-baseline justify-center gap-4"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2, duration: 0.5 }}
          >
            <span className="font-serif text-6xl font-bold text-blush-500">499 Kč</span>
            <span className="text-2xl text-warm-900/35 line-through">799 Kč</span>
          </motion.div>
          <p className="mt-2 text-sm text-warm-900/45">jednorázová platba · žádné předplatné</p>

          {/* Pricing card */}
          <motion.div
            className="mt-8 rounded-3xl border border-blush-200 bg-white/80 p-8 shadow-xl backdrop-blur-sm"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.3, duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
            whileHover={{ boxShadow: '0 32px 64px rgba(232,93,93,0.12)' }}
          >
            <ul className="space-y-3 text-left">
              {INCLUDES.map((item, i) => (
                <motion.li
                  key={item}
                  className="flex items-center gap-3"
                  initial={{ opacity: 0, x: -16 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: 0.4 + i * 0.07, duration: 0.4 }}
                >
                  <span className="flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full bg-sage-400 text-xs text-white">
                    ✓
                  </span>
                  <span className="text-warm-900/75">{item}</span>
                </motion.li>
              ))}
            </ul>

            <div className="mt-8">
              <motion.div whileHover={{ scale: 1.04 }} whileTap={{ scale: 0.97 }}>
                <CtaButton size="lg" className="w-full justify-center" />
              </motion.div>
              <p className="mt-4 text-xs text-warm-900/40">
                Bezpečná platba · Okamžité stažení · 14denní záruka
              </p>
            </div>
          </motion.div>
        </div>
      </AnimatedSection>
    </SectionWrapper>
  )
}
