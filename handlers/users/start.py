import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from aiogram.dispatcher import FSMContext
from keyboards.default.language import language
from loader import dp, db, bot


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f'Assalomu aleykum, {message.from_user.full_name}!\n'
                         f'Shaxswear online do\'konining rasmiy botiga Xush kelibsiz!\n\n'
                         f'Здравствуйте, {message.from_user.full_name}!\n'
                         f' Добро пожаловать в официальный бот интернет-магазина Shaxswear!')
    await message.answer('Tilni tanlang👇👇👇\n\n'
                         'Выберите язык👇👇👇', reply_markup=language)
    await state.finish()
