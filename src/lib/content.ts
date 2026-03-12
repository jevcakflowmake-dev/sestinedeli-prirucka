import type { Chapter, Testimonial, FaqItem, PainPoint } from '@/types'

export const CHAPTERS: Chapter[] = [
  {
    number: 1,
    title: 'Tvé tělo po porodu',
    subtitle: 'Co se děje uvnitř — a proč je to normální',
  },
  {
    number: 2,
    title: 'Kojení bez slz',
    subtitle: 'Od prvního přiložení po ustálení laktace',
  },
  {
    number: 3,
    title: 'Spánek pro přežití',
    subtitle: 'Spánkové cykly novorozence a jak přežít noc',
  },
  {
    number: 4,
    title: 'Baby blues vs. poporodní deprese',
    subtitle: 'Jak poznat hranici a kde hledat pomoc',
  },
  {
    number: 5,
    title: 'Péče o novorozence',
    subtitle: 'Koupání, přebalování, pupínek — krok za krokem',
  },
  {
    number: 6,
    title: 'Výživa a regenerace maminky',
    subtitle: 'Co jíst, aby měla sílu a mléko',
  },
  {
    number: 7,
    title: 'Vztah s partnerem',
    subtitle: 'Jak si udržet spojení, když jste zombie',
  },
  {
    number: 8,
    title: 'Praktická organizace domácnosti',
    subtitle: 'Systémy, které fungují s jednou volnou rukou',
  },
  {
    number: 9,
    title: 'Nástup rodiny a návštěvy',
    subtitle: 'Jak nastavit hranice bez pocitu viny',
  },
  {
    number: 10,
    title: 'Tělo zpátky — realisticky',
    subtitle: 'Jizvy, dno pánevní, cvičení v pravý čas',
  },
  {
    number: 11,
    title: 'Kdy volat lékaře',
    subtitle: 'Červené vlaječky pro maminku i miminko',
  },
]

export const PAIN_POINTS: PainPoint[] = [
  {
    icon: '🌙',
    headline: 'Nespíš a nevíš, jestli vydržíš',
    description:
      'Každé dvě hodiny vstáváš, ale nemáš sílu ani přečíst celý článek. Potřebuješ jasné odpovědi, ne dlouhé weby.',
  },
  {
    icon: '🤱',
    headline: 'Kojení bolí a nevíš, zda je to normální',
    description:
      'Nikdo ti neukázal správnou techniku. Stydíš se ptát a nevíš, komu věřit — porodnici, laktační poradkyni nebo mamince.',
  },
  {
    icon: '💭',
    headline: 'Cítíš se ztracená ve vlastním těle',
    description:
      'Hormony, emoce, zjizvené tělo — a přesto musíš fungovat. Nikdo ti neřekl, jak to reálně bude.',
  },
]

export const TESTIMONIALS: Testimonial[] = [
  {
    name: 'Tereza K.',
    babyAge: 'maminka 5týdenního Filipa',
    text: 'Přečetla jsem příručku v noci při kojení a poprvé za týdny jsem se cítila, že vím, co dělám. Kapitola o baby blues mi doslova zachránila noc.',
    initials: 'TK',
    color: 'bg-blush-200',
  },
  {
    name: 'Markéta P.',
    babyAge: 'maminka 3týdenní Sofie',
    text: 'Konečně konkrétní tipy, ne jen "poslouchej intuici". Tipy na kojení na straně 18 fungovaly hned napoprvé. Děkuju!',
    initials: 'MP',
    color: 'bg-sage-200',
  },
  {
    name: 'Lucie B.',
    babyAge: 'maminka 7týdenního Tobiáše',
    text: 'Koupila jsem to pro kamarádku jako dárek k porodu a pak si objednala druhou kopii pro sebe. Tohle by měla dostat každá maminka v porodnici.',
    initials: 'LB',
    color: 'bg-amber-100',
  },
]

export const FAQ_ITEMS: FaqItem[] = [
  {
    question: 'Co přesně dostanu po zakoupení?',
    answer:
      'Okamžitě po zaplacení obdržíš odkaz ke stažení PDF příručky (85 stran). Příručka funguje na počítači, tabletu i mobilu — ideální pro čtení při kojení.',
  },
  {
    question: 'Jak zaplatím?',
    answer:
      'Platba probíhá bezpečně kartou nebo přes Apple/Google Pay. Celý proces trvá méně než 2 minuty.',
  },
  {
    question: 'Mohu příručku sdílet s partnerem nebo kamarádkou?',
    answer:
      'Ano, příručku může číst celá vaše domácnost. Licenci na sdílení se třetími stranami nebo opětovný prodej nemáš.',
  },
  {
    question: 'Hodí se příručka i pro druhé nebo třetí dítě?',
    answer:
      'Rozhodně. Každé šestinedělí je jiné a každé miminko jiné. Praktické tabulky a checklisty v příručce jsou skvělé osvěžení i pro zkušené maminky.',
  },
  {
    question: 'A co když mi příručka nepomůže?',
    answer:
      'Do 14 dní od zakoupení ti vrátíme celou částku bez otázek. Stačí napsat na email v patičce.',
  },
  {
    question: 'Je příručka psaná lékařem?',
    answer:
      'Příručka je psaná ve spolupráci s porodní asistentkou a laktační poradkyní. Nenahrazuje lékařskou péči — obsahuje ověřené praktické informace pro každodenní péči.',
  },
]

export const PAYMENT_URL = process.env.NEXT_PUBLIC_PAYMENT_URL ?? '#'
