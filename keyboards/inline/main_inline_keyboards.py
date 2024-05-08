from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def social_network_inlint_buttons():
    # https://t.me/ikar_factor
    # https://t.me/factor_books
    # https://t.me/factorbooks
    inlint_button = [
        [InlineKeyboardButton(text = "IKAR | Factor Books", url="https://t.me/ikar_factor")],
        [InlineKeyboardButton(text = "Factor Books", url="https://t.me/factor_books")],
        [InlineKeyboardButton(text = "\"Factor Books\" nashriyoti", url="https://t.me/factorbooks")]
    ]

    res_buttons = InlineKeyboardMarkup(
        inline_keyboard=inlint_button,
    )

    return res_buttons
