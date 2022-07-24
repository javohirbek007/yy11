from aiogram import types
from aiogram.types import ContentType

from loader import dp, bot, db
from filters.admin import admin

from filters.user import user


from keyboards.default.admin_panel import asosiy_tasdiqlash, psost


# Echo bot
@dp.message_handler(admin(), commands='panel')
async def bot_echo(message: types.Message):
    username = message.from_user.username
    await message.answer(text=f"Admin Panelga Hush kelibsiz  @{username}", reply_markup=asosiy_tasdiqlash)
    await message.delete()


@dp.message_handler(admin(), text=f'Post jonatish')
async def bot_echo(message: types.Message):
    await message.answer(text=f'menyulardan birini tanlang', reply_markup=psost)





@dp.message_handler(admin(), text=f'statistika')

async def bot_echo(message: types.Message):
    kiyim = db.barcha_foydalanuvchilar()
    kiyim_nomi2 = kiyim[-1][0]
    print(kiyim_nomi2)

    await message.answer(text=f'Botdagi azolar soni\n'
                              f'{kiyim_nomi2}')
        
