from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇺🇿UZ'),
            KeyboardButton(text='🇷🇺RU'),
        ],
    ],
    resize_keyboard=True
)

dating = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Video yo\'riqnoma bilan tanishdim'),
        ],
    ],
    resize_keyboard=True
)

dating_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Я ознакомился видео инструкцией'),
        ],
    ],
    resize_keyboard=True
)

MainMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👕Kiyimlar'),
            KeyboardButton(text='📱Murojaat uchun'),
        ],
        [
            KeyboardButton(text='🔎Id bo\'yicha qidirish')
        ],
    ],
    resize_keyboard=True
)

MainMenu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👕Одежда'),
            KeyboardButton(text='📱 Поддержка'),
        ],
        [
            KeyboardButton(text='🔎Поиск по id')
        ],
    ],
    resize_keyboard=True
)

Clothes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🥾Krasovkalar'),
            KeyboardButton(text='👖Tolstovka va shalvar'),
            KeyboardButton(text='🧢Kepkalar'),
        ],
        [
            KeyboardButton(text='🧥Kurtkalar'),
            KeyboardButton(text='🎒Sumka va ryukzaklar'),
        ],
        [
            KeyboardButton(text='⬅️Ortga')
        ],
    ],
    resize_keyboard=True
)

Clothes_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🥾Кроссовки'),
            KeyboardButton(text='👖Толстовка и брюки'),
            KeyboardButton(text='🧢Шапки'),
        ],
        [
            KeyboardButton(text='🧥Куртки'),
            KeyboardButton(text='🎒Сумки и рюкзаки'),
        ],
        [
            KeyboardButton(text='⬅️Назад')
        ],
    ],
    resize_keyboard=True
)


Shopping_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Xarid qilish'),
            KeyboardButton(text='⬅️Ortga'),
        ],
    ],
    resize_keyboard=True
)

Shopping_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Купить'),
            KeyboardButton(text='⬅️Назад'),
        ],
    ],
    resize_keyboard=True
)


finish_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ To\'lov qildim'),
        ],
    ],
    resize_keyboard=True
)

finish_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Я оплатил'),
        ],
    ],
    resize_keyboard=True
)

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📍Location', request_location=True),
        ],
    ],
    resize_keyboard=True
)

BoshMenu = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Bosh menu')
        ],
    ],
    resize_keyboard=True
)

BoshMenuRu = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Главное меню')
        ],
    ],
    resize_keyboard=True
)
