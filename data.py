
# ── UI strings ─────────────────────────────────────────────────────────────────

STRINGS = {
    "en": {
        "welcome": (
            "🎩 *Welcome to Havana Cigar Club*\n\n"
            "Let us guide you to your perfect cigar in just a few steps."
        ),
        "step1_title": "⏱ *Step 1 of 3 — Session Duration*\n\nHow long do you plan to enjoy your cigar?",
        "step2_title": "💪 *Step 2 of 3 — Strength Preference*\n\nWhat strength do you prefer?",
        "step3_title": "👃 *Step 3 of 3 — Flavor Profile*\n\nWhich flavor notes appeal to you most?",
        "dur_quick": "🕐 Quick (20–35 min)",
        "dur_medium": "🕑 Medium (45–60 min)",
        "dur_long": "🌙 Long Evening (90+ min)",
        "str_mild": "🍃 Mild",
        "str_medium": "🌿 Medium",
        "str_full": "🔥 Full-Bodied",
        "flv_chocolate": "🍫 Dark Chocolate & Cocoa",
        "flv_nuts": "🌰 Roasted Nuts & Wood",
        "flv_espresso": "☕ Espresso & Spices",
        "flv_earthy": "🌍 Earthy & Leather",
        "recommendation_header": "✨ *Your Top 3 Cigar Picks*",
        "rank_1": "🥇 Perfect Match",
        "rank_2": "🥈 Great Alternative",
        "rank_3": "🥉 Also Consider",
        "origin_label": "🌍 Origin",
        "size_label": "📏 Size",
        "why_label": "💡 Why it suits you",
        "ask_price": "💬 Ask for Price",
        "visit_store": "🌐 Visit Our Store",
        "start_over": "🔄 Start Over",
        "no_match": (
            "We couldn't find a perfect match this time.\n"
            "Contact us on WhatsApp and our team will help you personally."
        ),
        "out_of_stock": "⚠️ Out of Stock",
        "back": "🔙 Back",
    },
    "ar": {
        "welcome": (
            "🎩 *مرحباً بك في هافانا سيجار كلوب*\n\n"
            "دعنا نرشدك إلى سيجارك المثالي في خطوات قليلة."
        ),
        "step1_title": "⏱ *الخطوة ١ من ٣ — مدة الجلسة*\n\nكم من الوقت تخطط للاستمتاع بسيجارك؟",
        "step2_title": "💪 *الخطوة ٢ من ٣ — تفضيل القوة*\n\nما قوة السيجار التي تفضلها؟",
        "step3_title": "👃 *الخطوة ٣ من ٣ — النكهات المفضلة*\n\nأي النكهات تستهويك أكثر؟",
        "dur_quick": "🕐 سريعة (٢٠–٣٥ دقيقة)",
        "dur_medium": "🕑 متوسطة (٤٥–٦٠ دقيقة)",
        "dur_long": "🌙 أمسية طويلة (+٩٠ دقيقة)",
        "str_mild": "🍃 خفيفة",
        "str_medium": "🌿 متوسطة",
        "str_full": "🔥 قوية",
        "flv_chocolate": "🍫 شوكولاتة داكنة وكاكاو",
        "flv_nuts": "🌰 مكسرات محمصة وخشب",
        "flv_espresso": "☕ إسبريسو وتوابل",
        "flv_earthy": "🌍 ترابية وجلد",
        "recommendation_header": "✨ *أفضل ٣ سيجار لك*",
        "rank_1": "🥇 التطابق المثالي",
        "rank_2": "🥈 بديل رائع",
        "rank_3": "🥉 جدير بالتجربة",
        "origin_label": "🌍 المنشأ",
        "size_label": "📏 المقاس",
        "why_label": "💡 لماذا يناسبك",
        "ask_price": "💬 استفسر عن السعر",
        "visit_store": "🌐 زر متجرنا",
        "start_over": "🔄 ابدأ من جديد",
        "no_match": (
            "لم نتمكن من إيجاد تطابق تام هذه المرة.\n"
            "تواصل معنا عبر واتساب وسيساعدك فريقنا شخصياً."
        ),
        "out_of_stock": "⚠️ غير متوفر",
        "back": "🔙 رجوع",
    },
}

WHATSAPP_URL = "https://wa.me/963988614489"
STORE_URL = "https://havanacigarclubae-glitch.github.io/HavanaCigarClub/"

# ── Cigar Catalog ──────────────────────────────────────────────────────────────
# size_category: "petit" | "robusto" | "toro" | "churchill"
# strength: "mild" | "medium" | "full"
# flavors: list of keys matching flv_* callback suffixes

CIGARS = [
    # ── COHIBA ────────────────────────────────────────────────────────────────
    {
        "brand": "Cohiba", "name": "Siglo II",
        "size": "129 × 42", "size_category": "petit",
        "strength": "medium",
        "flavors": ["nuts", "earthy"],
        "why_en": "A refined, shorter smoke with smooth wood and nutty elegance — perfect for a quick, satisfying session.",
        "why_ar": "سيجار قصير راقٍ بنكهات خشبية ومكسرات ناعمة — مثالي لجلسة سريعة وممتعة.",
    },
    {
        "brand": "Cohiba", "name": "Siglo III",
        "size": "159 × 42", "size_category": "petit",
        "strength": "medium",
        "flavors": ["nuts", "espresso"],
        "why_en": "A classic Cohiba corona with a gentle complexity — subtle spice and roasted notes in a shorter format.",
        "why_ar": "كورونا كوهيبا الكلاسيكية بتعقيد لطيف — توابل خفيفة ونكهات محمصة في شكل أصغر.",
    },
    {
        "brand": "Cohiba", "name": "Siglo IV",
        "size": "143 × 46", "size_category": "robusto",
        "strength": "medium",
        "flavors": ["nuts", "espresso"],
        "why_en": "Balanced and elegant with roasted coffee and subtle spice — a medium-duration classic from Cuba's finest.",
        "why_ar": "متوازن وأنيق بنكهات قهوة محمصة وتوابل خفيفة — كلاسيكي بامتياز من أرقى سيجار كوبا.",
    },
    {
        "brand": "Cohiba", "name": "Siglo VI",
        "size": "160 × 54", "size_category": "toro",
        "strength": "medium",
        "flavors": ["nuts", "earthy", "espresso"],
        "why_en": "One of Cohiba's most celebrated vitolas — a long, complex journey through cedar, coffee, and gentle pepper.",
        "why_ar": "من أشهر أحجام كوهيبا — رحلة طويلة ومعقدة عبر نكهات الأرز والقهوة والفلفل اللطيف.",
    },
    {
        "brand": "Cohiba", "name": "Behike 52",
        "size": "119 × 52", "size_category": "robusto",
        "strength": "full",
        "flavors": ["chocolate", "espresso"],
        "why_en": "An ultra-premium Cohiba with rare medio tiempo leaves — intensely rich dark chocolate and espresso in a compact form.",
        "why_ar": "كوهيبا فائق الجودة بأوراق نادرة — غني بالشوكولاتة الداكنة والإسبريسو في شكل مدمج.",
    },
    {
        "brand": "Cohiba", "name": "Behike 54",
        "size": "144 × 54", "size_category": "toro",
        "strength": "full",
        "flavors": ["chocolate", "espresso"],
        "why_en": "The Behike 54 delivers profound depth — layers of dark cocoa, spice, and espresso throughout a long luxurious smoke.",
        "why_ar": "بهيكي ٥٤ يقدم عمقاً استثنائياً — طبقات من الكاكاو الداكن والتوابل والإسبريسو في تجربة تدخين فاخرة.",
    },
    {
        "brand": "Cohiba", "name": "Behike 56",
        "size": "166 × 56", "size_category": "churchill",
        "strength": "full",
        "flavors": ["chocolate", "espresso", "earthy"],
        "why_en": "The pinnacle of the Behike line — a monumental smoke with dark chocolate, earth, and espresso complexity for a grand evening.",
        "why_ar": "قمة خط بهيكي — سيجار استثنائي بنكهات الشوكولاتة الداكنة والأرض والإسبريسو لأمسية لا تُنسى.",
    },
    {
        "brand": "Cohiba", "name": "Maduro 5 Magicos",
        "size": "115 × 52", "size_category": "robusto",
        "strength": "full",
        "flavors": ["chocolate", "earthy"],
        "why_en": "Cohiba's dark maduro wrapper brings intense cocoa sweetness and earthy depth in a shorter, satisfying robusto.",
        "why_ar": "غلاف ماديرو الداكن من كوهيبا يمنحك كاكاو حلو مكثف وعمقاً ترابياً في روبوستو مُقنع.",
    },
    {
        "brand": "Cohiba", "name": "Maduro Genios",
        "size": "140 × 54", "size_category": "toro",
        "strength": "full",
        "flavors": ["chocolate", "earthy", "espresso"],
        "why_en": "A premium maduro toro combining dark cocoa richness, earthy depth, and bold espresso in a long evening smoke.",
        "why_ar": "تورو ماديرو فاخر يجمع ثراء الكاكاو الداكن والعمق الترابي والإسبريسو في سيجار أمسية طويل.",
    },
    {
        "brand": "Cohiba", "name": "Novedosos",
        "size": "156 × 50", "size_category": "toro",
        "strength": "medium",
        "flavors": ["nuts", "espresso"],
        "why_en": "A newer Cohiba expression with elegant medium body — creamy roasted notes and refined spice over a long smoke.",
        "why_ar": "إصدار كوهيبا الجديد بجسم متوسط أنيق — نكهات محمصة كريمية وتوابل راقية على مدى تدخين طويل.",
    },
    {
        "brand": "Cohiba", "name": "Robustos",
        "size": "124 × 40", "size_category": "robusto",
        "strength": "medium",
        "flavors": ["nuts", "earthy"],
        "why_en": "The iconic Cohiba Robustos — cedar, light earth, and roasted nuts in a clean medium format.",
        "why_ar": "روبوستوس كوهيبا الأيقوني — أرز وأرض خفيفة ومكسرات محمصة في شكل متوسط نظيف.",
    },
    {
        "brand": "Cohiba", "name": "Robustos Supremos EL.2014",
        "size": "127 × 58", "size_category": "robusto",
        "strength": "full",
        "flavors": ["espresso", "earthy", "chocolate"],
        "why_en": "A limited-edition robusto with an oversized ring gauge — intense, complex, and perfectly balanced for a medium session.",
        "why_ar": "روبوستو إصدار محدود بقطر كبير — مكثف ومعقد ومتوازن بشكل مثالي لجلسة متوسطة.",
    },
    {
        "brand": "Cohiba", "name": "Talisman EL.2017",
        "size": "154 × 54", "size_category": "toro",
        "strength": "full",
        "flavors": ["espresso", "chocolate", "earthy"],
        "why_en": "A sought-after limited Cohiba with deep espresso and dark cocoa character — rewarding over a long evening.",
        "why_ar": "كوهيبا محدود مطلوب بطابع إسبريسو عميق وكاكاو داكن — مجزٍ على مدار أمسية طويلة.",
    },
    {
        "brand": "Cohiba", "name": "Esplendidos",
        "size": "178 × 47", "size_category": "churchill",
        "strength": "medium",
        "flavors": ["nuts", "earthy", "espresso"],
        "why_en": "A grand Cohiba Churchill — smooth creaminess with cedar, earth, and gentle coffee over a majestic long smoke.",
        "why_ar": "تشرشيل كوهيبا الكبير — كريمي ناعم مع نكهات الأرز والأرض والقهوة الخفيفة في تدخين طويل مهيب.",
    },
    {
        "brand": "Cohiba", "name": "50 Majestuosos 1966",
        "size": "150 × 58", "size_category": "toro",
        "strength": "full",
        "flavors": ["chocolate", "espresso", "earthy"],
        "why_en": "An ultra-rare commemorative Cohiba — extraordinary richness and complexity for the most special long evenings.",
        "why_ar": "كوهيبا تذكارية نادرة للغاية — ثراء وتعقيد استثنائيان لأكثر الأمسيات تميزاً.",
    },
    {
        "brand": "Cohiba", "name": "Piramides Extra Tubos",
        "size": "156 × 54", "size_category": "toro",
        "strength": "full",
        "flavors": ["espresso", "chocolate"],
        "why_en": "A powerful piramide with a tapered head delivering concentrated espresso and cocoa — elegant and intense over a long session.",
        "why_ar": "هرمي قوي برأس مدبب يقدم إسبريسو وكاكاو مركزين — أنيق ومكثف على مدار جلسة طويلة.",
    },
    {
        "brand": "Cohiba", "name": "Siglo VI Tubos",
        "size": "150 × 52", "size_category": "toro",
        "strength": "medium",
        "flavors": ["nuts", "earthy"],
        "why_en": "The beloved Siglo VI in a convenient tube — smooth, balanced, and ideal for a relaxed long evening.",
        "why_ar": "سيجلو السادس المحبوب في أنبوب مريح — ناعم ومتوازن ومثالي لأمسية طويلة مريحة.",
    },

    # ── HOYO DE MONTERREY ─────────────────────────────────────────────────────
    {
        "brand": "Hoyo de Monterrey", "name": "Epicure No.2",
        "size": "124 × 50", "size_category": "robusto",
        "strength": "mild",
        "flavors": ["earthy", "nuts"],
        "why_en": "A gentle classic — creamy cedar, light earth, and roasted nuts in a comfortable medium-session robusto.",
        "why_ar": "كلاسيكي لطيف — أرز كريمي وأرض خفيفة ومكسرات محمصة في روبوستو مريح.",
    },
    {
        "brand": "Hoyo de Monterrey", "name": "Serie Le Hoyo San Juan",
        "size": "149 × 54", "size_category": "toro",
        "strength": "medium",
        "flavors": ["earthy", "nuts"],
        "why_en": "An approachable toro with earthy creaminess and roasted notes — refined and smooth over a longer session.",
        "why_ar": "تورو سهل الاقتراب بكريمية ترابية ونكهات محمصة — راقٍ وناعم على مدار جلسة أطول.",
    },
    {
        "brand": "Hoyo de Monterrey", "name": "Grand Epicure EL.2013",
        "size": "133 × 55", "size_category": "robusto",
        "strength": "medium",
        "flavors": ["earthy", "nuts", "espresso"],
        "why_en": "A limited Hoyo with added depth — earthy creaminess meets subtle espresso richness in a satisfying medium session.",
        "why_ar": "هوبو محدود الإصدار بعمق إضافي — كريمية ترابية تلتقي مع ثراء إسبريسو خفيف في جلسة متوسطة مُقنعة.",
    },

    # ── ROMEO Y JULIETA ───────────────────────────────────────────────────────
    {
        "brand": "Romeo y Julieta", "name": "No.1 AT",
        "size": "140 × 40", "size_category": "petit",
        "strength": "mild",
        "flavors": ["nuts", "earthy"],
        "why_en": "A slim, mild smoke with creamy cedar and light roasted character — elegant for a quick refined session.",
        "why_ar": "سيجار نحيل وخفيف بنكهات أرز كريمية ومحمصة خفيفة — أنيق لجلسة سريعة ومميزة.",
    },
    {
        "brand": "Romeo y Julieta", "name": "Short Churchill",
        "size": "124 × 50", "size_category": "robusto",
        "strength": "medium",
        "flavors": ["nuts", "earthy", "espresso"],
        "why_en": "A condensed Churchill experience — rich cedar, earth, and a whisper of coffee in a satisfying medium-session robusto.",
        "why_ar": "تجربة تشرشيل مضغوطة — أرز غني وأرض ونفحة قهوة في روبوستو مُقنع لجلسة متوسطة.",
    },
    {
        "brand": "Romeo y Julieta", "name": "Wide Churchill",
        "size": "130 × 55", "size_category": "robusto",
        "strength": "medium",
        "flavors": ["nuts", "espresso"],
        "why_en": "A wide-gauge robusto with a rich draw — roasted nuts and espresso warmth in a comfortable session.",
        "why_ar": "روبوستو واسع القطر بسحب غني — مكسرات محمصة ودفء الإسبريسو في جلسة مريحة.",
    },
    {
        "brand": "Romeo y Julieta", "name": "Churchill",
        "size": "178 × 47", "size_category": "churchill",
        "strength": "medium",
        "flavors": ["earthy", "nuts"],
        "why_en": "The legendary Romeo Churchill — smooth cedar, gentle earth, and creamy finish for a graceful long evening.",
        "why_ar": "تشرشيل روميو الأسطوري — أرز ناعم وأرض لطيفة ونهاية كريمية لأمسية طويلة رقيقة.",
    },

    # ── MONTECRISTO ────────────────────────────────────────────────────────────
    {
        "brand": "Montecristo", "name": "No.2",
        "size": "156 × 52", "size_category": "toro",
        "strength": "medium",
        "flavors": ["earthy", "nuts", "espresso"],
        "why_en": "One of the world's most iconic cigars — complex earthy creaminess with coffee and roasted notes over a long smoke.",
        "why_ar": "من أشهر السيجار في العالم — كريمية ترابية معقدة مع قهوة ونكهات محمصة على مدار تدخين طويل.",
    },
    {
        "brand": "Montecristo", "name": "Edmundo",
        "size": "135 × 52", "size_category": "robusto",
        "strength": "medium",
        "flavors": ["earthy", "espresso"],
        "why_en": "A Montecristo gem — earthy and coffee-forward with smooth creaminess in a comfortable medium session.",
        "why_ar": "جوهرة مونتيكريستو — ترابي وقهوة بارزة مع نعومة كريمية في جلسة متوسطة مريحة.",
    },
    {
        "brand": "Montecristo", "name": "Petite No.2",
        "size": "120 × 52", "size_category": "robusto",
        "strength": "medium",
        "flavors": ["earthy", "espresso"],
        "why_en": "The classic Montecristo No.2 character in a shorter form — earthy complexity and espresso in a neat robusto.",
        "why_ar": "طابع مونتيكريستو رقم ٢ الكلاسيكي في شكل أقصر — تعقيد ترابي وإسبريسو في روبوستو أنيق.",
    },
    {
        "brand": "Montecristo", "name": "Petite Edmundo",
        "size": "110 × 52", "size_category": "robusto",
        "strength": "medium",
        "flavors": ["earthy", "nuts"],
        "why_en": "A compact Edmundo — gentle earthiness and roasted warmth in one of the shortest satisfying smokes in the catalog.",
        "why_ar": "إدموندو مضغوط — ترابية لطيفة ودفء محمص في واحد من أقصر السيجار المُقنعة في الكتالوج.",
    },
    {
        "brand": "Montecristo", "name": "Open Eagle",
        "size": "150 × 54", "size_category": "toro",
        "strength": "medium",
        "flavors": ["earthy", "espresso", "nuts"],
        "why_en": "A modern Montecristo expression — earthy, espresso-rich, and smooth for a satisfying long session.",
        "why_ar": "إصدار مونتيكريستو الحديث — ترابي وغني بالإسبريسو وناعم لجلسة طويلة مُقنعة.",
    },
    {
        "brand": "Montecristo", "name": "520 EL.2012",
        "size": "155 × 55", "size_category": "toro",
        "strength": "full",
        "flavors": ["espresso", "chocolate", "earthy"],
        "why_en": "A limited Montecristo with extraordinary depth — espresso, dark cocoa, and earth converge in a bold long smoke.",
        "why_ar": "مونتيكريستو محدود الإصدار بعمق استثنائي — إسبريسو وكاكاو داكن وأرض تتلاقى في تدخين طويل جريء.",
    },
    {
        "brand": "Montecristo", "name": "25 Supremos EL.2019",
        "size": "130 × 55", "size_category": "toro",
        "strength": "full",
        "flavors": ["chocolate", "espresso"],
        "why_en": "A recent limited Montecristo with rich chocolate and espresso intensity — complex and rewarding.",
        "why_ar": "مونتيكريستو محدود حديث بكثافة شوكولاتة وإسبريسو غنية — معقد ومجزٍ.",
    },
    {
        "brand": "Montecristo", "name": "80 Aniversario",
        "size": "165 × 55", "size_category": "churchill",
        "strength": "full",
        "flavors": ["espresso", "chocolate", "earthy"],
        "why_en": "A commemorative Churchill celebrating 80 years — powerful, complex espresso and dark chocolate for a monumental evening.",
        "why_ar": "تشرشيل تذكاري للذكرى الثمانين — إسبريسو قوي ومعقد وشوكولاتة داكنة لأمسية استثنائية.",
    },

    # ── PARTAGAS ───────────────────────────────────────────────────────────────
    {
        "brand": "Partagas", "name": "Serie E No.2",
        "size": "140 × 54", "size_category": "toro",
        "strength": "full",
        "flavors": ["earthy", "espresso", "nuts"],
        "why_en": "A powerful Partagas toro — bold earthiness, leather, and espresso in a complex and satisfying long smoke.",
        "why_ar": "تورو بارتاجاس القوي — ترابية جريئة وجلد وإسبريسو في تدخين طويل معقد ومُقنع.",
    },
    {
        "brand": "Partagas", "name": "Serie P No.2",
        "size": "140 × 52", "size_category": "toro",
        "strength": "full",
        "flavors": ["earthy", "espresso"],
        "why_en": "One of the most admired Cuban piramides — concentrated earth and espresso delivered through a tapered head.",
        "why_ar": "من أكثر الهرميات الكوبية إعجاباً — أرض وإسبريسو مركزان عبر رأس مدبب.",
    },
    {
        "brand": "Partagas", "name": "Serie E No.4",
        "size": "124 × 50", "size_category": "robusto",
        "strength": "full",
        "flavors": ["earthy", "espresso"],
        "why_en": "Partagas full-bodied character in robusto format — bold earth and espresso in a medium-length powerhouse.",
        "why_ar": "طابع بارتاجاس الكامل في شكل روبوستو — أرض جريئة وإسبريسو في قوة متوسطة الطول.",
    },
    {
        "brand": "Partagas", "name": "Salamones LCDH",
        "size": "184 × 57", "size_category": "churchill",
        "strength": "full",
        "flavors": ["earthy", "espresso", "chocolate"],
        "why_en": "A rare, grand figurado exclusive to La Casa del Habano — deep earth, leather, espresso, and cocoa in a dramatic long smoke.",
        "why_ar": "فيغورادو نادر وكبير حصري لـ لا كاسا ديل هابانو — أرض عميقة وجلد وإسبريسو وكاكاو في تدخين طويل درامي.",
    },

    # ── TRINIDAD ────────────────────────────────────────────────────────────────
    {
        "brand": "Trinidad", "name": "12 Topes EL.2016",
        "size": "125 × 56", "size_category": "robusto",
        "strength": "full",
        "flavors": ["espresso", "earthy", "chocolate"],
        "why_en": "A rare Trinidad limited edition with impressive ring gauge — complex espresso, earth, and dark cocoa for a bold session.",
        "why_ar": "إصدار ترينيداد المحدود النادر بقطر مميز — إسبريسو معقد وأرض وكاكاو داكن لجلسة جريئة.",
    },

    # ── H.UPMANN ────────────────────────────────────────────────────────────────
    {
        "brand": "H.Upmann", "name": "Magnum 56 EL.2015",
        "size": "150 × 56", "size_category": "toro",
        "strength": "medium",
        "flavors": ["nuts", "earthy", "espresso"],
        "why_en": "A limited H.Upmann with a satisfying ring gauge — creamy roasted nuts and subtle earth across a long refined session.",
        "why_ar": "هـ. أوبمان محدود الإصدار بقطر مُرضٍ — مكسرات محمصة كريمية وأرض خفيفة على مدار جلسة طويلة راقية.",
    },

    # ── PUNCH ────────────────────────────────────────────────────────────────
    {
        "brand": "Punch", "name": "Double Coronas",
        "size": "194 × 49", "size_category": "churchill",
        "strength": "medium",
        "flavors": ["earthy", "nuts"],
        "why_en": "A long, classic Cuban double corona — earthy, woody, and smooth for an extended, meditative long evening.",
        "why_ar": "دبل كورونا كوبي كلاسيكي طويل — ترابي وخشبي وناعم لأمسية طويلة ومتأملة.",
    },

    # ── BOLIVAR ───────────────────────────────────────────────────────────────
    {
        "brand": "Bolivar", "name": "Belicosos Finos",
        "size": "124 × 52", "size_category": "robusto",
        "strength": "full",
        "flavors": ["earthy", "espresso", "chocolate"],
        "why_en": "A legendary Bolivar piramide — intensely earthy and leathery with espresso and dark cocoa depth in a medium session.",
        "why_ar": "هرمي بوليفار الأسطوري — ترابي وجلدي بكثافة مع عمق إسبريسو وكاكاو داكن في جلسة متوسطة.",
    },
    {
        "brand": "Bolivar", "name": "Royal Coronas AT",
        "size": "124 × 50", "size_category": "robusto",
        "strength": "full",
        "flavors": ["earthy", "espresso"],
        "why_en": "The iconic Bolivar Royal Coronas in a tube — bold earth, leather, and espresso in a powerful robusto.",
        "why_ar": "رويال كوروناس بوليفار الأيقوني في أنبوب — أرض جريئة وجلد وإسبريسو في روبوستو قوي.",
    },
    {
        "brand": "Bolivar", "name": "Royal Coronas",
        "size": "124 × 50", "size_category": "robusto",
        "strength": "full",
        "flavors": ["earthy", "espresso"],
        "why_en": "A quintessential Cuban powerhouse — bold leather, earth, and espresso intensity for the full-bodied lover.",
        "why_ar": "نموذج كوبي بامتياز — جلد جريء وأرض وكثافة إسبريسو لمحبي السيجار القوي.",
    },
]

# Size category mapping from duration selection
DURATION_SIZE_MAP = {
    "quick": ["petit"],
    "medium": ["robusto"],
    "long": ["toro", "churchill"],
}

# Strength score mapping
STRENGTH_SCORE = {
    "mild": {"mild": 3, "medium": 1, "full": 0},
    "medium": {"mild": 1, "medium": 3, "full": 1},
    "full": {"mild": 0, "medium": 1, "full": 3},
}
