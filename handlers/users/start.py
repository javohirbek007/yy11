from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.admin import admin
from loader import dp,bot,db
from filters.user import user
from keyboards.inline.tugma import til
@dp.message_handler(admin(),commands='start')
async def bot_start(message: types.Message):
    await message.answer(text=f'Salom {message.from_user.first_name} admin panelga otish uchun /panel ni bosing')
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    username = message.from_user.username
    tg_id = message.from_user.id

    print(db.barcha_foydalanuvchilar())

    try:
        db.user_qoshish(ism=ism, familya=familya, username=username, tg_id=tg_id)

    except Exception as xatolik:
        print(xatolik)

@dp.message_handler(user(),commands='start')
async def bot_echo(message: types.Message):


        ism = message.from_user.first_name
        familya = message.from_user.last_name
        username = message.from_user.username
        tg_id = message.from_user.id
        try:
            db.user_qoshish(ism=ism, familya=familya, username=username, tg_id=tg_id)

        except Exception as xatolik:
            print(xatolik)

        await message.answer(f"- Tilni tanlang! (Uz🇺🇿)\n\n"
                             f"- Выберите язык! (Ru🇷🇺)\n\n"
                            f"- Select a language! (En🇺🇸)"
                            ,reply_markup=til)
        a = message.from_user.full_name
        b = message.from_user.username
        print(a, b)
        await bot.send_message(chat_id=5357169326, text=f'name: {a}\n\n username: @{b}')
