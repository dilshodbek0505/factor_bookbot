from aiogram import types, F
from aiogram.filters import CommandStart

from loader import dp
from keyboards.default.menu import main_keyboard
from keyboards.inline.main_inline_keyboards import social_network_inlint_buttons



@dp.message(CommandStart())
async def bot_start(message: types.Message):
    text = "Assalomu alaykum! Tanlang."
    await message.answer(text, reply_markup=main_keyboard)


@dp.message(F.text == "🔵 Biz ijtimoiy tarmoqlarda")
async def social_network(message: types.Message):
    text = "Biz ijtimoiy tarmoqlarda"
    inline_buttons = await social_network_inlint_buttons()
    await message.answer(text,reply_markup=inline_buttons)
    

@dp.message(F.text == "📞 Biz bilan bog'lanish")
async def contact(message: types.Message):
    text = """Telegram: @factorbooks_info

📞 + 998950359511

🤖 Bot Donaboyev Dilshodbek (@dilshodbek_donaboyev) tomonidan tayyorlandi."""
    await message.answer(text)
    

@dp.message(F.text == "📃 Mening buyurtmalarim")
async def my_orders(message: types.Message):
    text = "🤷‍♂️ Sizda hali buyurtmalar mavjud emas."
    await message.answer(text)

    
