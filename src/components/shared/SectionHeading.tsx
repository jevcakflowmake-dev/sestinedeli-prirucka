import { cn } from '@/lib/utils'

interface SectionHeadingProps {
  title: string
  subtitle?: string
  className?: string
  center?: boolean
}

export default function SectionHeading({ title, subtitle, className, center = true }: SectionHeadingProps) {
  return (
    <div className={cn('mb-12', center && 'text-center', className)}>
      <h2 className="font-serif text-3xl font-bold text-warm-900 md:text-4xl">{title}</h2>
      {subtitle && (
        <p className="mt-4 text-lg text-warm-900/60">{subtitle}</p>
      )}
    </div>
  )
}
