from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons = [
    [KeyboardButton(text = "📚 Kitoblar")],
    [KeyboardButton(text = "📃 Mening buyurtmalarim")],
    [KeyboardButton(text = "🔵 Biz ijtimoiy tarmoqlarda"), KeyboardButton(text = "📞 Biz bilan bog'lanish")],
]

main_keyboard = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True
)

