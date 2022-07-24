from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

youtube = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="You Tube",web_app=WebAppInfo(url="https://www.youtube.com/"))
        ],

    ])

til = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Uz🇺🇿", callback_data='uz')
        ],
[
            InlineKeyboardButton(text="Ru🇷🇺", callback_data='ru')
        ],
[
            InlineKeyboardButton(text="En🇺🇸", callback_data='us')
        ],

    ])