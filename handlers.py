from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from data import (
    STRINGS, CIGARS,
    DURATION_SIZE_MAP, STRENGTH_SCORE,
    WHATSAPP_URL, STORE_URL,
)


# ── Helpers ────────────────────────────────────────────────────────────────────

def s(key: str, lang: str) -> str:
    return STRINGS[lang][key]


def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
         InlineKeyboardButton("🇸🇦 العربية", callback_data="lang_ar")],
    ])


def find_top_cigars(duration: str, strength: str, flavor: str, top_n: int = 3):
    preferred_sizes = DURATION_SIZE_MAP[duration]
    scored = []

    for cigar in CIGARS:
        score = 0

        # Size match — highest weight (primary filter)
        if cigar["size_category"] in preferred_sizes:
            score += 4

        # Strength match
        score += STRENGTH_SCORE[strength].get(cigar["strength"], 0)

        # Flavor match
        if flavor in cigar["flavors"]:
            score += 3

        scored.append((score, cigar))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [cigar for _, cigar in scored[:top_n]]


# ── /start ────────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.clear()
    await update.message.reply_text(
        "🎩 *Havana Cigar Club*\n\n_هافانا سيجار كلوب_\n\nPlease choose your language / اختر لغتك:",
        reply_markup=main_menu_keyboard("en"),
        parse_mode=ParseMode.MARKDOWN,
    )


# ── /help ─────────────────────────────────────────────────────────────────────

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "*Havana Cigar Club Bot*\n\n"
        "/start — Begin the cigar finder\n"
        "/help — Show this message",
        parse_mode=ParseMode.MARKDOWN,
    )


# ── Main callback dispatcher ───────────────────────────────────────────────────

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data
    ud = context.user_data

    # Language selection
    if data in ("lang_en", "lang_ar"):
        lang = data.split("_")[1]
        ud["lang"] = lang
        await show_step1(query, lang)

    # Duration selection
    elif data.startswith("dur_"):
        ud["duration"] = data[4:]
        await show_step2(query, ud["lang"])

    # Strength selection
    elif data.startswith("str_"):
        ud["strength"] = data[4:]
        await show_step3(query, ud["lang"])

    # Flavor selection → compute recommendation
    elif data.startswith("flv_"):
        ud["flavor"] = data[4:]
        await show_recommendation(query, ud)

    # Restart
    elif data == "restart":
        context.user_data.clear()
        await query.edit_message_text(
            "🎩 *Havana Cigar Club*\n\n_هافانا سيجار كلوب_\n\nPlease choose your language / اختر لغتك:",
            reply_markup=main_menu_keyboard("en"),
            parse_mode=ParseMode.MARKDOWN,
        )

    # Back navigation
    elif data == "back_step1":
        await show_step1(query, ud.get("lang", "en"))
    elif data == "back_step2":
        await show_step2(query, ud.get("lang", "en"))
    elif data == "back_step3":
        await show_step3(query, ud.get("lang", "en"))


# ── Step screens ──────────────────────────────────────────────────────────────

async def show_step1(query, lang: str) -> None:
    keyboard = [
        [InlineKeyboardButton(s("dur_quick", lang), callback_data="dur_quick")],
        [InlineKeyboardButton(s("dur_medium", lang), callback_data="dur_medium")],
        [InlineKeyboardButton(s("dur_long", lang), callback_data="dur_long")],
    ]
    await query.edit_message_text(
        s("step1_title", lang),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN,
    )


async def show_step2(query, lang: str) -> None:
    keyboard = [
        [InlineKeyboardButton(s("str_mild", lang), callback_data="str_mild")],
        [InlineKeyboardButton(s("str_medium", lang), callback_data="str_medium")],
        [InlineKeyboardButton(s("str_full", lang), callback_data="str_full")],
        [InlineKeyboardButton(s("back", lang), callback_data="back_step1")],
    ]
    await query.edit_message_text(
        s("step2_title", lang),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN,
    )


async def show_step3(query, lang: str) -> None:
    keyboard = [
        [InlineKeyboardButton(s("flv_chocolate", lang), callback_data="flv_chocolate")],
        [InlineKeyboardButton(s("flv_nuts", lang), callback_data="flv_nuts")],
        [InlineKeyboardButton(s("flv_espresso", lang), callback_data="flv_espresso")],
        [InlineKeyboardButton(s("flv_earthy", lang), callback_data="flv_earthy")],
        [InlineKeyboardButton(s("back", lang), callback_data="back_step2")],
    ]
    await query.edit_message_text(
        s("step3_title", lang),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN,
    )


async def show_recommendation(query, ud: dict) -> None:
    lang = ud.get("lang", "en")
    duration = ud["duration"]
    strength = ud["strength"]
    flavor = ud["flavor"]

    top = find_top_cigars(duration, strength, flavor, top_n=3)

    if not top:
        keyboard = [
            [InlineKeyboardButton(s("ask_price", lang), url=WHATSAPP_URL)],
            [InlineKeyboardButton(s("start_over", lang), callback_data="restart")],
        ]
        await query.edit_message_text(
            s("no_match", lang),
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN,
        )
        return

    why_key = "why_en" if lang == "en" else "why_ar"
    origin = "Cuba" if lang == "en" else "كوبا"
    rank_keys = ["rank_1", "rank_2", "rank_3"]

    lines = [s("recommendation_header", lang), ""]

    for i, cigar in enumerate(top):
        lines += [
            f"*{s(rank_keys[i], lang)}*",
            f"🎩 *{cigar['brand']} — {cigar['name']}*",
            f"{s('origin_label', lang)}: {origin}",
            f"{s('size_label', lang)}: {cigar['size']} mm",
            f"{s('why_label', lang)}: _{cigar[why_key]}_",
            "",
        ]

    text = "\n".join(lines).rstrip()

    keyboard = [
        [
            InlineKeyboardButton(s("ask_price", lang), url=WHATSAPP_URL),
            InlineKeyboardButton(s("visit_store", lang), url=STORE_URL),
        ],
        [InlineKeyboardButton(s("start_over", lang), callback_data="restart")],
    ]

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN,
    )
