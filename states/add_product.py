from aiogram.fsm.state import State, StatesGroup

class AddBook(StatesGroup):
    name = State()
    author = State()
    genre = State()
    translator = State()
    cover = State()
    description = State()
    price = State()
    image = State()