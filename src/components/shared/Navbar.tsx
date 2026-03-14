'use client'

import { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import CtaButton from './CtaButton'

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40)
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  return (
    <motion.header
      className="fixed top-0 z-50 w-full transition-all duration-500"
      style={{
        backgroundColor: scrolled ? 'rgba(253, 243, 211, 0.85)' : 'transparent',
        backdropFilter: scrolled ? 'blur(12px)' : 'none',
        borderBottom: scrolled ? '1px solid rgba(250, 234, 187, 0.6)' : '1px solid transparent',
        boxShadow: scrolled ? '0 4px 24px rgba(61,53,48,0.06)' : 'none',
      }}
      initial={{ y: -80, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
    >
      <div className="mx-auto flex max-w-5xl items-center justify-between px-4 py-3 md:px-8">
        <motion.span
          className="font-serif text-lg font-bold text-warm-900"
          whileHover={{ scale: 1.02 }}
        >
          Šestinedělí s klidem
        </motion.span>
        <motion.div
          whileHover={{ scale: 1.04 }}
          whileTap={{ scale: 0.97 }}
          className="hidden sm:block"
        >
          <CtaButton label="Koupit příručku" size="default" />
        </motion.div>
      </div>
    </motion.header>
  )
}
