from loader import dp, db

from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context  import FSMContext
from aiogram.methods.send_photo import SendPhoto

from states.add_product import AddBook
from filters.user_filters import AdminFilter



@dp.message(Command(commands='add_book'))
async def add_book(message: types.Message, state: FSMContext):
    text = "Kitob nomini kiriting:"
    await message.answer(text)
    await state.set_state(AddBook.name)


@dp.message(AddBook.name)
async def set_book_name(message: types.Message, state: FSMContext):
    await state.update_data({
        "name": message.text
    })

    text = "Muallif nomini kiriting:"
    await message.answer(text)
    await state.set_state(AddBook.author)


@dp.message(AddBook.author)
async def set_book_author(message: types.Message, state: FSMContext):
    await state.update_data({
        "author": message.text
    })
    text = "Kitob janrini kiriting:"
    await message.answer(text)
    await state.set_state(AddBook.genre)


@dp.message(AddBook.genre)
async def set_book_genre(message: types.Message, state: FSMContext):
    await state.update_data({
        "genre": message.text
    })
    text = "Tarjimonni kiriting:"
    await message.answer(text)
    await state.set_state(AddBook.translator)


@dp.message(AddBook.translator)
async def set_book_translator(message: types.Message, state: FSMContext):
    await state.update_data({
        "translator": message.text
    })
    text = "Muqovani turini kiriting:"
    await message.answer(text)
    await state.set_state(AddBook.cover)


@dp.message(AddBook.cover)
async def set_book_cover(message: types.Message, state: FSMContext):
    await state.update_data({
        "cover": message.text
    })
    text = "Kitob narxini kiriting:"
    await message.answer(text)
    await state.set_state(AddBook.price)


@dp.message(AddBook.price)
async def set_book_price(message: types.Message, state: FSMContext):
    await state.update_data({
        "price": message.text
    })
    text = "Kitob haqida ma'lumot kiriting:"
    await message.answer(text)
    await state.set_state(AddBook.description)


@dp.message(AddBook.description)
async def set_book_description(message: types.Message, state: FSMContext):
    await state.update_data({
        "description": message.text
    })
    text = "Kitob rasmini yuboring:"
    await message.answer(text)
    await state.set_state(AddBook.image)


@dp.message(AddBook.image, F.photo)
async def set_book_image(message: types.Message, state: FSMContext):
    data = await state.get_data()
    photo_id = message.photo[-1].file_id
    db.add_book(
        name=data.get('name'),
        author=data.get('author'),
        genre=data.get('genre'),
        translator=data.get('translator'),
        cover=data.get('cover'),
        description=data.get('description'),
        price=data.get('description'),
        image_id=photo_id
    )
    await message.answer("Kitob muvofaqiyatli saqlandi!")
    

    