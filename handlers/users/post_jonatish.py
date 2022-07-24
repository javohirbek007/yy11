from aiogram import types
from aiogram.types import ContentType

from loader import db, dp, bot
from filters.admin import admin


from aiogram.dispatcher import FSMContext
from states.holatlar import Forma


@dp.message_handler(admin(), text='Post text')
async def bot_start(message: types.Message):
    await message.answer('Post jonatish uchun media yuboring')
    await Forma.post_qabul_qilish.set()


@dp.message_handler(admin(), state=Forma.post_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    post = message.text

    users = db.barcha_foydalanuvchilar()

    for user in users:
        await bot.send_message(chat_id=user[4], text=post)
        print(user[4])

        await state.finish()





@dp.message_handler(admin(), text='Post video')  # if

async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer('Post uchun Video Jonating')
    await Forma.psot_video.set()




@dp.message_handler(admin(),state=Forma.psot_video, content_types=ContentType.VIDEO)  # if
async def bot_echo(message: types.Message, state: FSMContext):
    video = message.video.file_id
    id = message.from_user.id
    await state.update_data({'video': video})
    await message.answer(text='Video uchun caption jonating')  # elif
    await Forma.caption_video.set()


@dp.message_handler(admin(),state=Forma.caption_video)  # elif


@dp.message_handler(admin(),state=Forma.caption_video)  # elif

async def bot_echo(message: types.Message, state: FSMContext):
    caption = message.text

    await state.update_data({'caption': caption})
    data = await state.get_data()
    video = data.get('video')
    caption = data.get('caption')
    users = db.barcha_foydalanuvchilar()
    for user in users:
        await bot.send_video(chat_id=user[4], caption=caption, video=video)
        await state.finish()


@dp.message_handler(admin(), text='Post photo')  # if
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer('Post uchun Rasm Jonating')
    await Forma.post_photo.set()



  # if

@dp.message_handler(admin(),state=Forma.post_photo, content_types=ContentType.PHOTO)  # if

async def bot_echo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    id = message.from_user.id
    await state.update_data({'photo': photo})
    await message.answer(text='Photo uchun caption jonating')  # elif
    await Forma.caption_photo.set()



  # elif

@dp.message_handler(admin(),state=Forma.caption_photo)  # elif

async def bot_echo(message: types.Message, state: FSMContext):
    caption = message.text

    await state.update_data({'caption': caption})
    data = await state.get_data()
    photo = data.get('photo')
    caption = data.get('caption')
    users = db.barcha_foydalanuvchilar()
    for user in users:
        await bot.send_photo(chat_id=user[4], caption=caption, photo=photo)
        await state.finish()
