from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp

from keyboards.inline.tugma import youtube


@dp.callback_query_handler(text='uz')
async def bot_echo(message: CallbackQuery):
    full_name = f"{message.from_user.first_name}"
    reply = f'Assalom alekum , <b>{full_name}!</b> \n<b>"You Tube"</b>ning rasmiy botiga hush kelibsiz🙂\n\nEndi <b>"You Tube"</b>ni <b>"Telegram"</b>dan chiqmasdan kuzating👇'
    await message.message.answer(reply, reply_markup=youtube)

@dp.callback_query_handler(text='us')
async def bot_echo(message: CallbackQuery):
    full_name = f"{message.from_user.first_name}"
    reply = f'Hello <b>{full_name}</b>,\nWelcome to the official <b>YouTube</b> bot\n\nNow watch <b>"You Tube"</b> without leaving <b>"Telegram"</b>👇'
    await message.message.answer(reply, reply_markup=youtube)

@dp.callback_query_handler(text='ru')
async def bot_echo(message: CallbackQuery):
    full_name = f"{message.from_user.first_name}"
    reply = f'Привет <b>{full_name}</b>,\nДобро пожаловать в официальный бот <b>YouTube</b>\n\nТеперь смотрите <b>"You Tube"</b> не выходя из <b>"Telegram"</b>👇'
    await message.message.answer(reply, reply_markup=youtube)

@dp.message_handler(commands='info')
async def bot_echo(message: types.Message):
    text = 'Bot yaratuvchisi - <b>@millicoder</b>\n\nSavol va takliflar uchun yozing👆'
    await message.answer(text=text)
