from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class admin(BoundFilter):
    async def check(self, message: types.Message):

        return message.chat.id == 1722082854


