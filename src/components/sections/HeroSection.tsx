'use client'

import { motion, useScroll, useTransform } from 'framer-motion'
import { useRef } from 'react'
import { Badge } from '@/components/ui/badge'
import CtaButton from '@/components/shared/CtaButton'

const FLOATING_BUBBLES = [
  { emoji: '🍼', x: '8%', y: '20%', delay: 0, size: 'text-3xl' },
  { emoji: '💤', x: '85%', y: '15%', delay: 0.3, size: 'text-2xl' },
  { emoji: '🌙', x: '78%', y: '65%', delay: 0.6, size: 'text-3xl' },
  { emoji: '🤱', x: '5%', y: '70%', delay: 0.9, size: 'text-2xl' },
  { emoji: '💛', x: '50%', y: '8%', delay: 1.1, size: 'text-xl' },
  { emoji: '🌿', x: '92%', y: '40%', delay: 0.5, size: 'text-2xl' },
]

const STATS = [
  { num: '11', label: 'kapitol' },
  { num: '85', label: 'stran' },
  { num: '400+', label: 'maminek' },
]

export default function HeroSection() {
  const ref = useRef<HTMLElement>(null)
  const { scrollYProgress } = useScroll({ target: ref, offset: ['start start', 'end start'] })
  const y = useTransform(scrollYProgress, [0, 1], ['0%', '30%'])
  const opacity = useTransform(scrollYProgress, [0, 0.8], [1, 0])

  return (
    <section ref={ref} className="relative min-h-screen overflow-hidden bg-gradient-to-b from-cream-100 via-cream-200 to-blush-100 pt-24 pb-16">

      {/* Floating bubbles */}
      {FLOATING_BUBBLES.map((b, i) => (
        <motion.div
          key={i}
          className={`pointer-events-none absolute hidden select-none md:block ${b.size}`}
          style={{ left: b.x, top: b.y }}
          initial={{ opacity: 0, scale: 0 }}
          animate={{ opacity: 0.5, scale: 1 }}
          transition={{ delay: b.delay + 0.8, duration: 0.6, ease: 'backOut' }}
        >
          <motion.div
            animate={{ y: [0, -12, 0] }}
            transition={{ duration: 3 + i * 0.5, repeat: Infinity, ease: 'easeInOut' }}
          >
            {b.emoji}
          </motion.div>
        </motion.div>
      ))}

      {/* Background blob */}
      <motion.div
        className="pointer-events-none absolute -top-32 -right-32 h-96 w-96 rounded-full bg-blush-200/40 blur-3xl"
        animate={{ scale: [1, 1.1, 1], rotate: [0, 10, 0] }}
        transition={{ duration: 8, repeat: Infinity, ease: 'easeInOut' }}
      />
      <motion.div
        className="pointer-events-none absolute -bottom-16 -left-16 h-72 w-72 rounded-full bg-sage-200/40 blur-3xl"
        animate={{ scale: [1, 1.15, 1] }}
        transition={{ duration: 6, repeat: Infinity, ease: 'easeInOut', delay: 1 }}
      />

      <motion.div className="relative mx-auto max-w-5xl px-4 md:px-8" style={{ y, opacity }}>
        <div className="flex flex-col items-center gap-16 md:flex-row md:items-center">

          {/* Text */}
          <div className="flex-1 text-center md:text-left">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.1 }}
            >
              <Badge className="mb-6 rounded-full border-0 bg-sage-200 px-4 py-1.5 font-sans text-sm font-semibold text-sage-500 shadow-sm">
                ✨ PDF příručka pro šestinedělí
              </Badge>
            </motion.div>

            <motion.h1
              className="font-serif text-5xl font-bold leading-[1.1] text-warm-900 md:text-6xl lg:text-7xl"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7, delay: 0.2, ease: [0.22, 1, 0.36, 1] }}
            >
              Šestinedělí
              <span className="block bg-gradient-to-r from-blush-500 to-blush-400 bg-clip-text text-transparent">
                bez chaosu
              </span>
            </motion.h1>

            <motion.p
              className="mt-6 text-lg leading-relaxed text-warm-900/65 md:text-xl"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.35 }}
            >
              85 stránek praktických odpovědí na otázky, které tě budí ve 3&nbsp;ráno.
              Kojení, spánek, emoce, péče o sebe — sepsáno s&nbsp;porodní asistentkou.
            </motion.p>

            <motion.div
              className="mt-8 flex flex-col items-center gap-4 sm:flex-row md:justify-start"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.5 }}
            >
              <motion.div whileHover={{ scale: 1.04 }} whileTap={{ scale: 0.97 }}>
                <CtaButton size="lg" />
              </motion.div>
              <p className="text-sm text-warm-900/45">
                Okamžité stažení · 14denní záruka
              </p>
            </motion.div>

            {/* Stats */}
            <motion.div
              className="mt-10 flex flex-wrap justify-center gap-8 md:justify-start"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.6, delay: 0.7 }}
            >
              {STATS.map((s, i) => (
                <motion.div
                  key={s.label}
                  className="text-center"
                  initial={{ opacity: 0, y: 16 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.7 + i * 0.1, duration: 0.5 }}
                >
                  <div className="font-serif text-3xl font-bold text-blush-500">{s.num}</div>
                  <div className="text-xs text-warm-900/45">{s.label}</div>
                </motion.div>
              ))}
            </motion.div>
          </div>

          {/* Book mockup */}
          <motion.div
            className="relative flex-shrink-0"
            initial={{ opacity: 0, x: 60 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.3, ease: [0.22, 1, 0.36, 1] }}
          >
            <motion.div
              className="relative h-[360px] w-[280px] md:h-[440px] md:w-[340px]"
              animate={{ y: [0, -10, 0] }}
              transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut' }}
            >
              {/* Shadow */}
              <div className="absolute -bottom-4 -right-4 h-full w-full rounded-3xl bg-blush-300/50 blur-sm" />
              {/* Card */}
              <div className="relative flex h-full w-full flex-col items-center justify-center overflow-hidden rounded-3xl bg-gradient-to-br from-cream-50 via-blush-100 to-cream-200 p-8 shadow-2xl">
                {/* Decorative circles */}
                <div className="absolute -top-8 -right-8 h-32 w-32 rounded-full bg-blush-200/60" />
                <div className="absolute -bottom-8 -left-8 h-24 w-24 rounded-full bg-sage-200/50" />

                <div className="relative text-7xl">👶</div>
                <div className="relative mt-4 text-center">
                  <div className="font-serif text-2xl font-bold text-warm-900">Šestinedělí</div>
                  <div className="font-serif text-xl font-bold text-blush-500">s klidem</div>
                  <div className="mt-2 text-xs text-warm-900/40">Kompletní příručka pro nové maminky</div>
                </div>

                <div className="relative mt-6 w-full space-y-2">
                  {['Kojení', 'Spánek', 'Emoce', 'Péče o tělo'].map((t, i) => (
                    <motion.div
                      key={t}
                      className="flex items-center gap-2 rounded-xl bg-white/70 px-3 py-2 shadow-sm backdrop-blur-sm"
                      initial={{ opacity: 0, x: -16 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: 1 + i * 0.1, duration: 0.4 }}
                    >
                      <span className="text-sage-400">✓</span>
                      <span className="text-sm text-warm-900/70">{t}</span>
                    </motion.div>
                  ))}
                </div>
              </div>
            </motion.div>
          </motion.div>

        </div>
      </motion.div>

      {/* Wave divider */}
      <div className="absolute bottom-0 left-0 w-full">
        <svg viewBox="0 0 1440 80" className="w-full" preserveAspectRatio="none">
          <path d="M0,40 C360,80 1080,0 1440,40 L1440,80 L0,80 Z" fill="#FDE8E8" />
        </svg>
      </div>
    </section>
  )
}
