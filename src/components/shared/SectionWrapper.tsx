import { cn } from '@/lib/utils'

interface SectionWrapperProps {
  children: React.ReactNode
  className?: string
  id?: string
  inner?: string
}

export default function SectionWrapper({ children, className, id, inner }: SectionWrapperProps) {
  return (
    <section id={id} className={cn('py-16 md:py-24', className)}>
      <div className={cn('mx-auto max-w-5xl px-4 md:px-8', inner)}>
        {children}
      </div>
    </section>
  )
}
