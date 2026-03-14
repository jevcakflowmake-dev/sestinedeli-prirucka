'use client'

import { motion } from 'framer-motion'
import CtaButton from '@/components/shared/CtaButton'

export default function FooterSection() {
  return (
    <footer className="relative overflow-hidden bg-warm-900 py-16 text-white/70">
      {/* Background decoration */}
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute -top-24 left-1/4 h-48 w-48 rounded-full bg-blush-500/10 blur-3xl" />
        <div className="absolute -bottom-16 right-1/4 h-48 w-48 rounded-full bg-sage-500/10 blur-3xl" />
      </div>

      <div className="relative mx-auto max-w-5xl px-4 md:px-8">
        <div className="flex flex-col items-center gap-6 text-center">
          <motion.span
            className="font-serif text-2xl font-bold text-white"
            initial={{ opacity: 0, y: 16 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
          >
            Šestinedělí s klidem
          </motion.span>

          <motion.p
            className="max-w-md text-sm leading-relaxed"
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1, duration: 0.5 }}
          >
            Praktická příručka pro maminky s novorozenci — od porodu po 6.&nbsp;týden.
            Napsáno s porodní asistentkou, pro reálný život.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 16 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2, duration: 0.5 }}
            whileHover={{ scale: 1.04 }}
            whileTap={{ scale: 0.97 }}
          >
            <CtaButton label="Stáhnout příručku za 499 Kč" />
          </motion.div>

          <div className="mt-4 flex flex-wrap justify-center gap-6 text-xs text-white/40">
            <a href="mailto:ahoj@sestinedeli-prirucka.cz" className="transition-colors hover:text-white/70">
              ahoj@sestinedeli-prirucka.cz
            </a>
            <span>·</span>
            <a href="#" className="transition-colors hover:text-white/70">Ochrana osobních údajů</a>
            <span>·</span>
            <a href="#" className="transition-colors hover:text-white/70">Obchodní podmínky</a>
          </div>

          <p className="text-xs text-white/25">
            © {new Date().getFullYear()} Šestinedělí s klidem. Všechna práva vyhrazena.
          </p>
        </div>
      </div>
    </footer>
  )
}
