from aiogram.filters import BaseFilter
from aiogram import types

from data.config import ADMINS


class AdminFilter(BaseFilter):
    def __call__(self, message: types.Message):
        for admin in ADMINS:
            if message.from_user.id == int(admin):
                return True
        return False
