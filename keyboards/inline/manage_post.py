from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")

confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 Ruxsat berish", callback_data=post_callback.new(action="post")),
    ]]
)


confirmation_keyboard_ru = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 Разрешать", callback_data=post_callback.new(action="post")),
    ]]
)