from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

asosiy_tasdiqlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Post jonatish'),
            KeyboardButton(text='statistika'),

        ]

    ],
    resize_keyboard=True

)
psost = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Post text'),
            KeyboardButton(text='Post photo'),
        ],
        [
            KeyboardButton(text='Post video')
        ]

    ],
    resize_keyboard=True
)
