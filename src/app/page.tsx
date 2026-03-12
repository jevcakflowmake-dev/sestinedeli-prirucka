import Navbar from '@/components/shared/Navbar'
import HeroSection from '@/components/sections/HeroSection'
import PainPointsSection from '@/components/sections/PainPointsSection'
import ContentsSection from '@/components/sections/ContentsSection'
import PreviewSection from '@/components/sections/PreviewSection'
import TestimonialsSection from '@/components/sections/TestimonialsSection'
import PricingSection from '@/components/sections/PricingSection'
import FaqSection from '@/components/sections/FaqSection'
import FooterSection from '@/components/sections/FooterSection'

export default function HomePage() {
  return (
    <main>
      <Navbar />
      <HeroSection />
      <PainPointsSection />
      <ContentsSection />
      <PreviewSection />
      <TestimonialsSection />
      <PricingSection />
      <FaqSection />
      <FooterSection />
    </main>
  )
}
