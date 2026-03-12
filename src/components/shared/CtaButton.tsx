import { PAYMENT_URL } from '@/lib/content'
import { cn } from '@/lib/utils'

interface CtaButtonProps {
  label?: string
  className?: string
  size?: 'default' | 'lg'
}

export default function CtaButton({
  label = 'Chci příručku za 499 Kč',
  className,
  size = 'default',
}: CtaButtonProps) {
  return (
    <a
      href={PAYMENT_URL}
      className={cn(
        'inline-block rounded-full bg-blush-500 font-sans font-semibold text-white shadow-lg transition-all hover:bg-blush-600 hover:shadow-xl hover:-translate-y-0.5 active:translate-y-0',
        size === 'lg' ? 'px-10 py-4 text-lg' : 'px-8 py-3 text-base',
        className,
      )}
    >
      {label}
    </a>
  )
}
