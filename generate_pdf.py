#!/usr/bin/env python3
"""
Generátor PDF příručky "Šestinedělí s klidem"
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame

# === BARVY ===
BLUSH_500  = HexColor('#E85D5D')
BLUSH_200  = HexColor('#FCCFCF')
BLUSH_100  = HexColor('#FDE8E8')
SAGE_400   = HexColor('#7DA876')
SAGE_200   = HexColor('#CFDECB')
SAGE_100   = HexColor('#EAF0E8')
CREAM_200  = HexColor('#FDF3D3')
CREAM_100  = HexColor('#FEF9EC')
WARM_900   = HexColor('#3D3530')
WARM_600   = HexColor('#6B5E58')
WARM_400   = HexColor('#9C8880')

PAGE_W, PAGE_H = A4

# === OBSAH KAPITOL ===
CHAPTERS = [
    {
        "num": 1,
        "title": "Tvé tělo po porodu",
        "subtitle": "Co se děje uvnitř — a proč je to normální",
        "emoji": "💫",
        "color": BLUSH_100,
        "sections": [
            ("Co se děje s tvým tělem v prvních dnech", [
                "Bezprostředně po porodu prochází tvé tělo dramatickými změnami. Děloha, která v průběhu těhotenství vyrostla na velikost melounu, se postupně stahuje zpět do původní velikosti — tento proces trvá přibližně 6 týdnů a můžeš při něm cítit takzvané 'dozvuky' neboli stahy, zejména při kojení.",
                "Lochie — poporodní výtok — jsou zcela normální. V prvních dnech jsou červené a silné, postupně zesvětlají a ubývají. Přibližně 4–6 týdnů po porodu by měly úplně vymizet.",
                "Pot a časté močení jsou způsoby, jakými tělo zbavuje přebytečné tekutiny nahromaděné během těhotenství. Je normální se hodně potit, zejména v noci.",
            ]),
            ("Péče o hráz a jizvy", [
                "Pokud jsi rodila přirozeně, hráz mohla být protržena nebo nastřižena (epiziotomie). Bolest je normální a obvykle odezní během 2–3 týdnů. Ledové obklady v prvních 24 hodinách pomáhají snížit otok.",
                "Při hojení hráze: oplachuj čistou vodou po každém použití toalety, používej měkké jednorázové vložky, vyhni se sedění na tvrdé podložce (donut polštář je tvůj přítel).",
                "Pokud jsi rodila císařem, jizva se hojí přibližně 6–8 týdnů. Nepřetěžuj se zvedáním těžkých věcí, udržuj ránu suchou a čistou. Po zhojení je možná masáž jizvy pro lepší kosmetický výsledek.",
            ]),
            ("Kdy volat lékaře — fyzické příznaky", [
                "Silné krvácení (promočíš více než 1 vložku za hodinu), velké krevní sraženiny (větší než golfový míček), horečka nad 38 °C, zarudnutí nebo hnisání u jizvy, silná bolest, která se nezlepšuje.",
                "Nekdy ženy zažívají poporodní komplikace jako trombózu nebo infekci — neboj se volat lékaře nebo porodnici kdykoliv máš pochybnosti. Raději jednou zbytečně než pozdě.",
            ]),
        ]
    },
    {
        "num": 2,
        "title": "Kojení bez slz",
        "subtitle": "Od prvního přiložení po ustálení laktace",
        "emoji": "🤱",
        "color": SAGE_100,
        "sections": [
            ("První přiložení a správná technika", [
                "Ideálně do hodiny po porodu — tehdy je miminko nejbdílejší a instinkty jsou nejsilnější. Neboj se požádat porodní asistentku o pomoc. První přiložení nemusí být dokonalé.",
                "Správný úchop (latch): brada miminka se dotýká prsu, ústa jsou otevřená dokořán jako rybička, rty jsou vyhrnuty ven, nos je volný. Pokud cítíš bolest po celou dobu kojení (ne jen na začátku), úchop není správný — přilož znovu.",
                "Polohy kojení: poloha 'madonna' (klasická), poloha 'rugby' (miminko pod paží, skvělá po císaři), poloha vleže na boku (pro noční kojení). Vyzkoušej různé a najdi svou.",
            ]),
            ("Jak poznat, že miminko má dost mléka", [
                "Zlaté pravidlo: co do miminka jde, musí z něj vyjít. V prvním týdnu: alespoň 1–2 mokré pleny denně na den věku miminka (1. den = 1 plenka, 2. den = 2 plenky atd.). Od 4.–5. dne: alespoň 6 mokrých plen za 24 hodin.",
                "Miminko přibírá. Po počátečním úbytku (max 10 % porodní váhy) by mělo začít přibírat okolo 4.–5. dne. Kontrolní vážení u dětského lékaře ti dá jistotu.",
                "Spokojené miminko po kojení: samo pustí prs, usíná nebo je spokojené, má vlhká ústa.",
            ]),
            ("Časté problémy a jejich řešení", [
                "Prasklé bradavky: správný úchop je klíčový. Pomáhá lanolin krém nebo vlastní mléko nanesené po kojení. Kojení by nemělo bolet po celou dobu — jen první sekundy.",
                "Zatvrdlé prsy (engorgement): přikládej co nejčastěji, před kojením teplý obklad, po kojení studený. Nevymačkávaj mléko zbytečně — tím jen stimuluješ tvorbu dalšího.",
                "Mastitis (zánět prsu): horečka, zarudnutí, bolest — okamžitě k lékaři. Kojení NEPRESTAVÁŠ, pokračuješ i při zánětu.",
            ]),
        ]
    },
    {
        "num": 3,
        "title": "Spánek pro přežití",
        "subtitle": "Spánkové cykly novorozence a jak přežít noc",
        "emoji": "🌙",
        "color": CREAM_100,
        "sections": [
            ("Jak spí novorozenec", [
                "Novorozenec nemá nastavený cirkadiánní rytmus — nerozlišuje den a noc. To se postupně vyvíjí mezi 3.–6. týdnem. Do té doby: není nic špatně s tebou ani s miminkem.",
                "Spánkový cyklus novorozence trvá přibližně 45–50 minut (oproti dospělým 90 minut). Mezi cykly se probouzí — to je normální a ochranný mechanismus.",
                "Potřeba spánku: novorozenec spí 14–17 hodin denně, ale v krátkých blocích 2–4 hodiny. Nepřerušený 5hodinový spánek je statisticky raritou v prvních týdnech.",
            ]),
            ("Bezpečné podmínky pro spánek", [
                "Bezpečné spací prostředí (SIDS prevence): vždy na zádech, pevná rovná podložka, žádné polštáře ani peřiny v postýlce v prvním roce, bez plyšáků v postýlce, nekouřit v domácnosti.",
                "Sdílení postele (co-sleeping): pokud se rozhodneš pro sdílení postele, informuj se o bezpečných podmínkách — nikdy na gauči ani v křesle, tvrdá matrace, bez alkoholu a léků navozujících spánek.",
                "Teplota v místnosti: ideálně 18–20 °C. Přikrývej miminko přiměřeně — jako sebe plus jedna vrstva navíc.",
            ]),
            ("Strategie pro více spánku", [
                "Spi, když spí miminko — ano, stále to platí, i když to každý opakuje. Domácnost počká.",
                "Střídání s partnerem: domluvte se na blocích. Například partner přebírá miminko od 22 do 2 a ty spíš, pak ty přebíráš a partner spí. Každý dostane alespoň jeden blok hlubokého spánku.",
                "Zkrácení procesů: noční láhev/kojení vleže, přebaly jen při nutnosti, příprava věcí dopředu večer.",
            ]),
        ]
    },
    {
        "num": 4,
        "title": "Baby blues vs. poporodní deprese",
        "subtitle": "Jak poznat hranici a kde hledat pomoc",
        "emoji": "💜",
        "color": BLUSH_100,
        "sections": [
            ("Baby blues — normální hormonální bouře", [
                "Baby blues zažívá až 80 % žen. Začíná typicky 3.–5. den po porodu, kdy prudce klesá hladina estrogenů a progesteronu. Projevuje se pláčem bez zřejmého důvodu, podrážděností, únavou, přecitlivělostí.",
                "Baby blues samo odeznívá do 2 týdnů. Pomáhá odpočinek, podpora blízkých, vědomí, že je to normální a dočasné.",
                "Důležité: pokud příznaky trvají déle než 2 týdny nebo se zhoršují, může jít o poporodní depresi — vyhledej pomoc.",
            ]),
            ("Poporodní deprese — příznaky a kdy vyhledat pomoc", [
                "Poporodní depresí trpí přibližně 10–15 % žen (někdy i partneři). Je to nemoc, ne slabost. Příznaky: přetrvávající smutek nebo prázdnota, ztráta radosti z miminka nebo čehokoli, neschopnost pečovat o sebe nebo miminko, pocity bezcennosti nebo viny, myšlenky na sebepoškození.",
                "Kdy okamžitě vyhledat pomoc: myšlenky na ublížení sobě nebo miminkovi — zavolej záchrannou službu nebo jdi na pohotovost.",
                "Léčba funguje: terapie, případně antidepresiva (existují bezpečné i při kojení). Netrp zbytečně — požádej o pomoc svého gynaekologa, praktického lékaře nebo psychologa.",
            ]),
            ("Péče o duševní zdraví — každodenní tipy", [
                "Pohyb: i krátká procházka venku pomáhá. Denní světlo reguluje hormony a náladu.",
                "Spojení s ostatními: skupiny pro maminky, online komunity, kamarádky ve stejné situaci. Izolace zhoršuje příznaky.",
                "Nároky na sebe: snižuj laťku. Dost dobré je dost dobré. Miminko potřebuje přítomnou (i unavenu) maminku, ne dokonalou.",
            ]),
        ]
    },
    {
        "num": 5,
        "title": "Péče o novorozence",
        "subtitle": "Koupání, přebalování, pupínek — krok za krokem",
        "emoji": "🛁",
        "color": SAGE_100,
        "sections": [
            ("Koupání novorozence", [
                "Do odpadnutí pupečníku (7–14 dní): koupej pouze houbičkou — otírej části těla zvlhčenou žínkou, netlač pod pupečník. Po odpadnutí: klasická koupel v dětské vaničce.",
                "Teplota vody: 37 °C (dej zápěstí — má být příjemně teplá, ne horká). Teplota místnosti: min. 22 °C. Koupel trvá 5–10 minut.",
                "Postup koupele: drž miminko bezpečně (hlava na tvém zápěstí), umyj nejdřív obličej (čistou vodou, bez mýdla), pak tělo, nakonec vlasy. Vlasy myjeme posledních — aby miminko nevychladlo.",
                "Frekvence: 2–3× týdně stačí. Každodenní koupel vysušuje citlivou kůži.",
            ]),
            ("Přebalování — vše co potřebuješ vědět", [
                "Jak přebalovat: vlhčené ubrousky (nebo vlhký hadr) — otíráme vždy od přední části dozadu (u holčiček obzvláště důležité kvůli prevenci infekce). U chlapečků dej pozor — studený vzduch stimuluje močení.",
                "Opruzeniny: nejlepší prevence je suchá kůže. Nech miminko chvíli bez pleny 'proložit'. Pomocí je zinc oxide krém (Bepanthen apod.).",
                "Pleny: počet přebalování v prvních týdnech — 8–12× denně. Mokrá plena = důkaz, že miminko má dost tekutin.",
            ]),
            ("Péče o pupínek", [
                "Pupečník odpadne sám za 7–14 dní (někdy déle). Nezasahuj — neodbočuj, neobaluj, nestahuj.",
                "Udržuj suché a čisté: skládej plenku pod pupečník, aby měl přístup k vzduchu. Mírné zapáchání je normální, dokud odpadne.",
                "Kdy k lékaři: zarudnutí kůže okolo pupečníku, horečka, hnisání, krvácení z pupečníku (kapka krve při odpadání je normální).",
            ]),
        ]
    },
    {
        "num": 6,
        "title": "Výživa a regenerace maminky",
        "subtitle": "Co jíst, aby měla sílu a mléko",
        "emoji": "🥗",
        "color": CREAM_100,
        "sections": [
            ("Výživa při kojení", [
                "Kojíš-li, potřebuješ přibližně o 500 kcal více denně. Nejde o počítání kalorií, ale o pestrou stravu s dostatkem živin.",
                "Co je důležité: bílkoviny (maso, ryby, luštěniny, vejce, mléčné výrobky), vápník (mléčné výrobky, brokolice, mandle), omega-3 (tučné ryby 2× týdně), železo (maso, luštěniny + vitamin C pro vstřebávání), vitamín D (suplementace doporučena celý rok v ČR).",
                "Mýtus: nemusíš se vyhýbat kořeněnému jídlu, zelí, cibuli nebo česneku. Chuť mléka se mírně mění, ale naprostá většina miminek to toleruje. Pij podle žízně (nekofeinové nápoje preferuj).",
            ]),
            ("Jídlo s jednou rukou — praktické tipy", [
                "Realita šestinedělí: vaříš jednou rukou, protože druhou držíš miminko. Nebo vůbec nevaříš, protože spíš. Obojí je v pořádku.",
                "Tipy pro jednoduché jídlo: smoothie (ovoce + bílkoviny + mléko), avokádo na chlebu, tvaroh s ovocem, ořechy a sušené ovoce jako snack, vařená vejce dopředu, mražená zelenina do rychlých jídel.",
                "Přijmi pomoc: pokud někdo nabídne uvařit — řekni ANO a popiš co rád/a jíš. Tohle není čas být skromná.",
            ]),
            ("Hydratace a co pít", [
                "Při kojení potřebuješ výrazně více tekutin — až 3 litry denně. Nejjednodušší způsob: mít sklenici vody vždy při kojení.",
                "Káva: 1–2 šálky denně jsou bezpečné při kojení. Kofein přechází do mléka v malém množství, ale většina miminek to toleruje. Pokud je miminko neklidné, zkus omezit.",
                "Alkohol: ideálně žádný, pokud kojíš. Pokud si dáš sklenku vína, kojení z 'nasbíraného' mléka je bezpečnější volba.",
            ]),
        ]
    },
    {
        "num": 7,
        "title": "Vztah s partnerem",
        "subtitle": "Jak si udržet spojení, když jste zombie",
        "emoji": "💑",
        "color": BLUSH_100,
        "sections": [
            ("Realita prvních týdnů jako pár", [
                "Každý pár prochází výzvami po příchodu miminka. Průzkumy ukazují, že spokojenost ve vztahu obvykle po porodu klesá — nejsi výjimka, je to normální.",
                "Typické napětí: nevyspání amplifikuje konflikty, každý má jiný pohled na to 'co se má dělat', žena může cítit, že partner nechápe jak náročné je kojení a péče, partner může cítit odstrčenost nebo bezmocnost.",
                "Klíčové: toto je dočasné. Nepřijímejte zásadní rozhodnutí v prvních 6 týdnech. Rodinu právě stavíte.",
            ]),
            ("Komunikace v náročném období", [
                "Říkej konkrétně co potřebuješ: ne 'nikdy mi nepomáháš', ale 'potřebuju teď hodinu spát, můžeš přebrat miminko?'",
                "Prostor pro oba: oba jste vyčerpaní, oba se učíte. Partner neví automaticky jak pomoci — raději ho navádět než čekat, že sám pozná.",
                "Sdílejte i malé radosti: 'podívej, usmál se na mě' — tyto momenty vás spojují.",
            ]),
            ("Intimita a sex po porodu", [
                "Doporučené čekání: min. 6 týdnů po vaginálním porodu a po kontrole u gynekologa. Po císaři podobně.",
                "Fyzická a psychická připravenost jsou stejně důležité. Nezahajuj jen proto, že 'čas vypršel'. Komunikuj s partnerem.",
                "Změny které jsou normální: snížené libido (hormony kojení potlačují estrogen), suchost pochvy (pomocí lubrikant), citlivost po porodu. Vše se časem normalizuje.",
            ]),
        ]
    },
    {
        "num": 8,
        "title": "Praktická organizace domácnosti",
        "subtitle": "Systémy, které fungují s jednou volnou rukou",
        "emoji": "🏠",
        "color": SAGE_100,
        "sections": [
            ("Přebuduj očekávání", [
                "Čistá domácnost, uvařeno, miminko spokojené a vy odpočatí — toto nejde dohromady naráz. Přijmi, že priority se musí přerozdělit.",
                "Hierarchie v šestinedělí: (1) bezpečnost miminka, (2) tvé zdraví a spánek, (3) jídlo pro tebe, (4) cokoliv dalšího.",
                "Co může počkat: žehlení (téměř vše), hloubkový úklid, vaření složitých jídel, odpovídání na zprávy.",
            ]),
            ("Systémy které usnadní život", [
                "Přebalovací stanice na každém patře (nebo alespoň na dvou místech): ušetříš chůzi s miminkem.",
                "Noc připravena dopředu: pleny, vlhčené ubrousky, čisté oblečení — vše v dosahu, bez zapínání světel.",
                "Dávkové vaření: uvař jednou víc a zmraž. Kamarádky a rodina nabízejí jídlo — přijmi to a řekni co máš ráda.",
                "Nákupy online: přesměruj energii jinam. Donáška jídla nebo nákupů je investice do svého zdraví.",
            ]),
            ("Zapojení partnera a rodiny", [
                "Konkrétní úkoly pro partnera: ranní koupel miminka, jeden noční vstávání za noc, vaření nebo objednání jídla, úklid toalety a kuchyně.",
                "Babičky a ostatní: dej jim konkrétní úkoly ('můžeš přijít a uvařit polévku?'), ne jen 'přijď mě navštívit' — návštěvy bez pomoci mohou vyčerpávat.",
                "Placená pomoc: pokud je to finančně možné, uklízečka 2× měsíčně nebo chůva na pár hodin týdně — investice do tvého zdraví a vztahu.",
            ]),
        ]
    },
    {
        "num": 9,
        "title": "Nástup rodiny a návštěvy",
        "subtitle": "Jak nastavit hranice bez pocitu viny",
        "emoji": "🚪",
        "color": CREAM_100,
        "sections": [
            ("Právo říct ne", [
                "Návštěvy v šestinedělí jsou privilegiem, ne právem. Máš plné právo říct: 'Teď ještě nejsme připraveni na návštěvy' a nepotřebuješ to nikomu vysvětlovat.",
                "Nastavení hranic dopředu: ideálně ještě v těhotenství domluv s partnerem jaká pravidla chcete. Pak partner může komunikovat za oba.",
                "Formule pro odmítnutí: 'Moc rády vás uvidíme, ale teď ještě ne. Dáme vám vědět, až budeme připraveni.'",
            ]),
            ("Pravidla pro návštěvy", [
                "Kdo je nemocný — nepřichází. Žádné výjimky, i pro babičky.",
                "Mytí rukou před dotykem s miminkem — vždy.",
                "Délka návštěvy: řekni dopředu 'máme hodinu, pak bude miminko jíst'. Tím automaticky nastavíš délku.",
                "Návštěvy, které pomáhají: přinesou jídlo, uklidí, podrží miminko aby ses mohla osprchovat. Návštěvy, které jen 'koukají' — na ty máš právo říct, že ještě počkáme.",
            ]),
            ("Speciální situace: prarodiče a rady", [
                "Rady, které nejsi žádala: 'za nás se to dělalo jinak' — nejjednodušší odpověď je 'hmm, zajímavé' a pokračovat po svém.",
                "Babičky a dědečkové mají obrovskou touhu pomáhat a být součástí — kanalizuj to na konkrétní pomoc ('můžeš si sednout a podržet ji, já si jdu osprchovat?').",
                "Konflikty v rodině: pokud prarodiče opakovaně ignorují vaše pravidla (bezpečnost, přebalování, kojení vs. přikrmování), je to čas pro partner/ka, aby jasně a klidně nastolil hranice. Toto není boj — je to ochrana rodiny.",
            ]),
        ]
    },
    {
        "num": 10,
        "title": "Tělo zpátky — realisticky",
        "subtitle": "Jizvy, dno pánevní, cvičení v pravý čas",
        "emoji": "🌸",
        "color": BLUSH_100,
        "sections": [
            ("Realistická očekávání", [
                "Tělo, které devět měsíců nosilo a zrodilo nový život, se nemění přes noc. Ani přes měsíc. Šestinedělí (6 týdnů) je minimum — plná regenerace může trvat rok i déle.",
                "Brzišní svaly: diastáza (rozestup středové šlachy břicha) se vyskytuje u 60–100 % žen po porodu. Klasické 'crunch' cviky ji mohou zhoršit. Nejdřív rehabilitace dna pánevního.",
                "Vlasy: vypadávání vlasů kolem 3.–6. měsíce po porodu je normální. Způsobují ho hormony. Vrátí se.",
            ]),
            ("Dno pánevní — proč je klíčové", [
                "Dno pánevní nese celou váhu těhotenství a prochází obrovskou zátěží při porodu. Slabé dno pánevní způsobuje únik moče při smíchu/kašli/skákání — to není normální, ale je léčitelné.",
                "Cvičení Kegel (stah dna pánevního): snaž se stáhnout svaly, jako bys zastavovala proud moče. Drž 5 sekund, uvolni, opakuj 10×. Dělej 3× denně — klidně při kojení nebo přebalování.",
                "Fyzioterapeutka dna pánevního: doporučeno po každém porodu, zejména pokud pociťuješ jakékoliv problémy. Není to luxus, je to péče o zdraví.",
            ]),
            ("Kdy a jak začít cvičit", [
                "0–6 týdnů: pouze Kegel cvičení, krátké procházky. Žádné břišní cvičení, posilovací cvičení, běh.",
                "Po 6 týdnech a po souhlasu lékaře: postupné rozjezd. Začni chůzí, plaváním, pilates pro maminky.",
                "Po 3 měsících: pokud nemáš diastázu nebo problémy s dnem pánevním, lze postupně přidávat intenzitu. Vždy poslouchej tělo.",
                "Sociální sítě a 'snap back' kultura: ignoruj fotky celebrit 6 týdnů po porodu. Za každou takovou fotografií jsou osobní trenéři, kuchař a nanny. Srovnávej se jen se sebou.",
            ]),
        ]
    },
    {
        "num": 11,
        "title": "Kdy volat lékaře",
        "subtitle": "Červené vlaječky pro maminku i miminko",
        "emoji": "🚨",
        "color": SAGE_100,
        "sections": [
            ("Červené vlaječky u maminky — okamžitě kontaktuj lékaře", [
                "HOREČKA nad 38 °C — může signalizovat infekci (hráze, dělohy, prsu, močových cest).",
                "SILNÉ KRVÁCENÍ — promočíš více než 1 vložku za hodinu, nebo se krvácení náhle zesílí.",
                "BOLEST na hrudi nebo dušnost — může jít o trombózu (krevní sraženinu).",
                "ZARUDNUTÍ, teplo nebo bolest v lýtku — příznak trombózy.",
                "SILNÁ BOLEST hlavy, problémy se zrakem — příznaky poporodní hypertenze.",
                "MYŠLENKY na sebepoškození nebo ublížení miminkovi — OKAMŽITĚ volejte záchranku (155).",
            ]),
            ("Červené vlaječky u miminka — okamžitě k lékaři", [
                "HOREČKA nad 38 °C u novorozence (do 3 měsíců) — vždy okamžitě k lékaři.",
                "DÝCHÁNÍ: rychlé (více než 60 dechů za minutu), pomalé, s mezerami, modravá barva rtů.",
                "NECHUTENSTVÍ: odmítá jíst 2 jídla v řadě, nebo výrazně méně než obvykle.",
                "LETARGIE: nejde vzbudit, nereaguje na podněty.",
                "ŽLOUTENKA: žlutá barva kůže nebo bělma — zejména pokud se šíří na bříško nebo nohy.",
                "PUPEČNÍK: zarudnutí kůže okolo pupečníku, horečka, hnisání.",
            ]),
            ("Kontakty a zdroje pomoci", [
                "Záchranná služba: 155",
                "Porodnice, kde jsi rodila: telefonická linka pro maminky",
                "Dětský lékař: pro dotazy ohledně miminka",
                "Laktační poradkyně: kojení",
                "Krizová linka pomoci: 116 123 (Linka bezpečí)",
                "Online komunita: Facebook skupiny pro maminky — Maminky v šestinedělí, Kojení s láskou",
            ]),
        ]
    },
]


# === HELPER TŘÍDY ===

class PageCanvas:
    """Přidává header/footer na každou stránku."""
    def __init__(self, chapter_num=0, chapter_title=""):
        self.chapter_num = chapter_num
        self.chapter_title = chapter_title

    def __call__(self, c: canvas.Canvas, doc):
        c.saveState()
        w, h = A4

        # Footer linka
        c.setStrokeColor(BLUSH_200)
        c.setLineWidth(0.5)
        c.line(2*cm, 1.8*cm, w - 2*cm, 1.8*cm)

        # Číslo stránky
        c.setFont("Helvetica", 8)
        c.setFillColor(WARM_400)
        c.drawCentredString(w / 2, 1.2*cm, f"— {doc.page} —")

        # Footer text
        c.setFont("Helvetica-Oblique", 7)
        c.drawString(2*cm, 1.2*cm, "Šestinedělí s klidem")
        c.drawRightString(w - 2*cm, 1.2*cm, f"Kapitola {self.chapter_num}: {self.chapter_title}" if self.chapter_num else "")

        c.restoreState()


# === STYLY ===

def get_styles():
    styles = getSampleStyleSheet()

    title_page = ParagraphStyle(
        'TitlePage',
        fontName='Helvetica-Bold',
        fontSize=42,
        textColor=white,
        alignment=TA_CENTER,
        leading=50,
        spaceAfter=10,
    )

    subtitle_page = ParagraphStyle(
        'SubtitlePage',
        fontName='Helvetica',
        fontSize=16,
        textColor=HexColor('#FCCFCF'),
        alignment=TA_CENTER,
        leading=22,
        spaceAfter=8,
    )

    chapter_title = ParagraphStyle(
        'ChapterTitle',
        fontName='Helvetica-Bold',
        fontSize=26,
        textColor=WARM_900,
        alignment=TA_LEFT,
        leading=32,
        spaceAfter=6,
        spaceBefore=10,
    )

    chapter_subtitle = ParagraphStyle(
        'ChapterSubtitle',
        fontName='Helvetica-Oblique',
        fontSize=13,
        textColor=BLUSH_500,
        alignment=TA_LEFT,
        leading=18,
        spaceAfter=20,
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Helvetica-Bold',
        fontSize=13,
        textColor=WARM_900,
        alignment=TA_LEFT,
        leading=18,
        spaceBefore=16,
        spaceAfter=6,
    )

    body = ParagraphStyle(
        'BodyText',
        fontName='Helvetica',
        fontSize=10.5,
        textColor=WARM_600,
        alignment=TA_JUSTIFY,
        leading=16,
        spaceAfter=8,
    )

    bullet_item = ParagraphStyle(
        'BulletItem',
        fontName='Helvetica',
        fontSize=10.5,
        textColor=WARM_600,
        alignment=TA_LEFT,
        leading=16,
        spaceAfter=4,
        leftIndent=12,
        bulletIndent=0,
    )

    toc_chapter = ParagraphStyle(
        'TOCChapter',
        fontName='Helvetica-Bold',
        fontSize=11,
        textColor=WARM_900,
        leading=18,
        spaceAfter=2,
    )

    toc_subtitle = ParagraphStyle(
        'TOCSubtitle',
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        textColor=WARM_400,
        leading=14,
        spaceAfter=10,
        leftIndent=16,
    )

    return {
        'title_page': title_page,
        'subtitle_page': subtitle_page,
        'chapter_title': chapter_title,
        'chapter_subtitle': chapter_subtitle,
        'section_heading': section_heading,
        'body': body,
        'bullet': bullet_item,
        'toc_chapter': toc_chapter,
        'toc_subtitle': toc_subtitle,
    }


# === GENERÁTOR ===

def build_pdf(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2.5*cm,
        leftMargin=2.5*cm,
        topMargin=2.5*cm,
        bottomMargin=2.5*cm,
        title="Šestinedělí s klidem",
        author="Šestinedělí s klidem",
        subject="Příručka pro maminky v šestinedělí",
    )

    styles = get_styles()
    story = []

    # ===== TITULNÍ STRANA =====
    def draw_cover(c, doc):
        c.saveState()
        w, h = A4

        # Gradient pozadí (simulace — plné barvy)
        c.setFillColor(HexColor('#C94141'))
        c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(BLUSH_500)
        c.rect(0, h*0.3, w, h*0.7, fill=1, stroke=0)

        # Dekorativní kruhy
        c.setFillColor(HexColor('#F47F7F'))
        c.setStrokeColor(white)
        c.setLineWidth(0)
        c.circle(w * 0.85, h * 0.85, 120, fill=1, stroke=0)
        c.setFillColor(HexColor('#F9ADAD'))
        c.circle(w * 0.1, h * 0.15, 80, fill=1, stroke=0)
        c.setFillColor(SAGE_400)
        c.circle(w * 0.75, h * 0.1, 60, fill=1, stroke=0)

        # Bílý pruh dole
        c.setFillColor(CREAM_200)
        c.rect(0, 0, w, h * 0.18, fill=1, stroke=0)

        # Titulek
        c.setFont("Helvetica-Bold", 48)
        c.setFillColor(white)
        c.drawCentredString(w/2, h * 0.72, "Šestinedělí")
        c.setFont("Helvetica-Bold", 44)
        c.drawCentredString(w/2, h * 0.62, "s klidem")

        # Emoji
        c.setFont("Helvetica", 60)
        c.drawCentredString(w/2, h * 0.50, "👶")

        # Podtitul
        c.setFont("Helvetica-Oblique", 14)
        c.setFillColor(HexColor('#FDE8E8'))
        c.drawCentredString(w/2, h * 0.43, "Kompletní příručka pro nové maminky")
        c.drawCentredString(w/2, h * 0.39, "od porodu po 6. týden")

        # Dole
        c.setFont("Helvetica", 10)
        c.setFillColor(WARM_600)
        c.drawCentredString(w/2, h * 0.10, "11 kapitol  ·  85 stran  ·  Sepsáno s porodní asistentkou")

        c.restoreState()

    story.append(PageBreak())  # placeholder pro titulní stranu

    # ===== UVOD =====
    story.append(PageBreak())
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("Milá maminko,", styles['section_heading']))
    story.append(Spacer(1, 0.3*cm))
    intro_text = [
        "Právě se ti narodilo miminko — a spolu s ním nová verze tebe.",
        "Šestinedělí je jedním z nejintenzivnějších, nejkrásnějších a nejnáročnějších období života. Nikdo tě na něj dostatečně nepřipravil. Tohle je příručka, která měla existovat a nyní ji držíš v rukou (nebo spíš jednou rukou, zatímco druhou kojíš).",
        "Je napsaná pro reálný život — pro 3 hodiny ráno, pro bolest hráze, pro slzy bez důvodu, pro okamžiky naprostého úžasu. Přímá, konkrétní, bez přikrašlování.",
        "Jsi dost dobrá maminka. Víc než dost.",
    ]
    for t in intro_text:
        story.append(Paragraph(t, styles['body']))
        story.append(Spacer(1, 0.2*cm))

    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("S láskou a respektem,", styles['body']))
    story.append(Paragraph("<i>Tým Šestinedělí s klidem</i>", styles['body']))

    # ===== OBSAH =====
    story.append(PageBreak())
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("Obsah příručky", styles['chapter_title']))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUSH_200, spaceAfter=16))

    for ch in CHAPTERS:
        story.append(Paragraph(f"{ch['num']}. {ch['title']}", styles['toc_chapter']))
        story.append(Paragraph(ch['subtitle'], styles['toc_subtitle']))

    # ===== KAPITOLY =====
    for ch in CHAPTERS:
        story.append(PageBreak())

        # Barevný header kapitoly
        def make_chapter_header(chapter, color):
            def draw(c, doc):
                c.saveState()
                w = PAGE_W

                # Barevný pruh nahoře
                from reportlab.lib.colors import HexColor as HC
                c.setFillColor(color)
                c.rect(0, PAGE_H - 5*cm, w, 5*cm, fill=1, stroke=0)

                # Accent pruh
                c.setFillColor(BLUSH_500)
                c.rect(0, PAGE_H - 5*cm, 0.5*cm, 5*cm, fill=1, stroke=0)

                # Číslo kapitoly
                c.setFont("Helvetica-Bold", 72)
                c.setFillColor(white)
                c.setFillAlpha(0.2)
                c.drawRightString(w - 2*cm, PAGE_H - 4.5*cm, str(chapter['num']))
                c.setFillAlpha(1)

                # Emoji
                c.setFont("Helvetica", 32)
                c.setFillColor(WARM_900)
                c.setFillAlpha(0.6)
                c.drawString(2.5*cm, PAGE_H - 2.2*cm, chapter['emoji'])
                c.setFillAlpha(1)

                # Footer
                c.setStrokeColor(BLUSH_200)
                c.setLineWidth(0.5)
                c.line(2*cm, 1.8*cm, w - 2*cm, 1.8*cm)
                c.setFont("Helvetica", 8)
                c.setFillColor(WARM_400)
                c.drawCentredString(w/2, 1.2*cm, f"— {doc.page} —")
                c.setFont("Helvetica-Oblique", 7)
                c.drawString(2*cm, 1.2*cm, "Šestinedělí s klidem")
                c.drawRightString(w - 2*cm, 1.2*cm, f"Kapitola {chapter['num']}: {chapter['title']}")

                c.restoreState()
            return draw

        story.append(Spacer(1, 3.5*cm))  # prostor pro barevný header
        story.append(Paragraph(f"Kapitola {ch['num']}", styles['chapter_subtitle']))
        story.append(Paragraph(ch['title'], styles['chapter_title']))
        story.append(Paragraph(ch['subtitle'], styles['chapter_subtitle']))
        story.append(HRFlowable(width="100%", thickness=1, color=BLUSH_200, spaceAfter=16))

        # Sekce kapitoly
        for section_title, paragraphs in ch['sections']:
            story.append(Paragraph(section_title, styles['section_heading']))

            # Bullet body nebo odstavce
            for para in paragraphs:
                if para.startswith(('HOREČKA', 'SILNÉ', 'BOLEST', 'ZARUDNUTÍ', 'SILNÁ', 'MYŠLENKY',
                                    'DÝCHÁNÍ', 'NECHUTENSTVÍ', 'LETARGIE', 'ŽLOUTENKA', 'PUPEČNÍK',
                                    'Záchranná', 'Porodnice', 'Dětský', 'Laktační', 'Krizová', 'Online')):
                    story.append(Paragraph(f"• {para}", styles['bullet']))
                else:
                    story.append(Paragraph(para, styles['body']))

        story.append(Spacer(1, 1*cm))

        # Tip box na konci každé kapitoly
        tip_data = [[
            Paragraph("💡 Rychlý přehled", ParagraphStyle(
                'TipTitle', fontName='Helvetica-Bold', fontSize=10,
                textColor=WARM_900, leading=14, spaceAfter=4
            )),
        ], [
            Paragraph(f"Kapitola <b>{ch['num']}</b> pokrývá klíčová témata: {', '.join([s[0] for s in ch['sections']])}.", ParagraphStyle(
                'TipBody', fontName='Helvetica', fontSize=9.5,
                textColor=WARM_600, leading=14
            )),
        ]]
        tip_table = Table(tip_data, colWidths=[14*cm])
        tip_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), SAGE_100),
            ('BACKGROUND', (0, 1), (-1, -1), CREAM_100),
            ('ROUNDEDCORNERS', [8, 8, 8, 8]),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ]))
        story.append(tip_table)

    # ===== ZÁVER =====
    story.append(PageBreak())
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("Na závěr", styles['chapter_title']))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUSH_200, spaceAfter=20))

    zaver = [
        "Šestinedělí není sprint. Je to pomalý, náročný, nádherný maraton. Žádné šestinedělí není stejné — ani druhé, ani třetí.",
        "Pokud jsi přečetla tuto příručku celou: jsi připravena lépe než většina matek, které kdy šestinedělím prošly.",
        "Pokud jsi přečetla jen část: přečtis přesně to, co jsi v tu chvíli potřebovala.",
        "Pokud jsi ji otevřela ve 3 ráno: jsme tu s tebou. Tohle pomine. Bude líp.",
        "Gratulujeme — jsi maminka. 💛",
    ]
    for t in zaver:
        story.append(Paragraph(t, styles['body']))
        story.append(Spacer(1, 0.3*cm))

    # Kontakt
    story.append(Spacer(1, 2*cm))
    contact_data = [[
        Paragraph("📬 Kontakt & podpora", ParagraphStyle(
            'ContactTitle', fontName='Helvetica-Bold', fontSize=11,
            textColor=WARM_900, leading=16
        )),
    ], [
        Paragraph(
            "Máš dotazy nebo potřebuješ poradit? Napiš nám na <b>ahoj@sestinedeli-prirucka.cz</b><br/>"
            "Web: <b>sestinedeli-prirucka.vercel.app</b><br/>"
            "14denní záruka vrácení peněz bez otázek.",
            ParagraphStyle('ContactBody', fontName='Helvetica', fontSize=10,
                          textColor=WARM_600, leading=16)
        ),
    ]]
    contact_table = Table(contact_data, colWidths=[14*cm])
    contact_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BLUSH_200),
        ('BACKGROUND', (0, 1), (-1, -1), BLUSH_100),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 14),
    ]))
    story.append(contact_table)

    # === BUILD ===
    page_canvas = PageCanvas()

    doc.build(
        story,
        onFirstPage=draw_cover,
        onLaterPages=page_canvas,
    )

    print(f"✅ PDF vygenerováno: {output_path}")


if __name__ == "__main__":
    build_pdf("/Users/jevci/Sites/sestinedeli-prirucka/public/sestinedeli-s-klidem.pdf")
