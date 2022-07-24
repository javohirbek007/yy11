from aiogram.dispatcher.filters.state import State, StatesGroup


class Forma(StatesGroup):
    post_qabul_qilish = State()
    post_photo = State()
    psot_video = State()
    caption_video = State()
    caption_photo = State()
    tasdiqlash_qabul_qilish = State()
