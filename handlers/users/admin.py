import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.language import Clothes
from keyboards.inline.manage_post import post_callback
from loader import dp, db


@dp.message_handler(text="/add_product", user_id=ADMINS[0], state='*')
async def add_product(message: types.Message, state: FSMContext):
    await message.answer('Mahsulot uchun id raqam kiriting: ', reply_markup=ReplyKeyboardRemove())
    await state.set_state('add_id')


@dp.message_handler(state='add_id', user_id=ADMINS[0])
async def add_id(message: types.Message, state: FSMContext):
    id_product = message.text
    id_product = int(id_product)
    await state.update_data(
        {'id_product': id_product}
    )
    await message.answer('Mahsulot nomini kiriting: ', reply_markup=Clothes)
    await state.set_state('product_name')


@dp.message_handler(state='product_name', user_id=ADMINS[0])
async def add_id(message: types.Message, state: FSMContext):
    product_name = message.text
    data = await state.get_data()
    id_product = data.get('id_product')
    try:
        db.add_product(id=id_product,
                       name=product_name)
    except sqlite3.IntegrityError as err:
        await message.reply('Bunday id raqamli mahsulot bor!\n'
                            'Boshqattan kiriting: /add_product')
        await state.finish()
        return
    await message.answer('Mahsulot rasmini tashlang: ', reply_markup=ReplyKeyboardRemove())
    await state.set_state('product_photo')


@dp.message_handler(content_types=types.ContentType.PHOTO, state='product_photo', user_id=ADMINS[0])
async def get_file_id_p(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    data = await state.get_data()
    id_product = data.get('id_product')
    db.update_user_photo_id(photo_id=photo_id, id=id_product)
    await message.answer('Mahsulot narxini kiriting: ')
    await state.set_state('product_price')


@dp.message_handler(state='product_price', user_id=ADMINS[0])
async def add_price(message: types.Message, state: FSMContext):
    price = message.text
    data = await state.get_data()
    id_product = data.get('id_product')
    db.update_user_price(price=price, id=id_product)
    await message.answer('Mahsulot haqida yozing: ')
    await state.set_state('product_desc')


@dp.message_handler(state='product_desc', user_id=ADMINS[0])
async def product_desc(message: types.Message, state: FSMContext):
    desc = message.text
    data = await state.get_data()
    id_product = data.get('id_product')
    db.update_user_desc(desc=desc, id=id_product)
    await message.answer('Mahsulotingiz bazaga qo\'shildi')
    await state.finish()


@dp.message_handler(text="/cleandb", user_id=ADMINS[0])
async def get_all_users(message: types.Message):
    db.delete_products()
    await message.answer("Baza tozalandi!")


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS[1])
async def approve_post(call: CallbackQuery):
    await call.answer("Xarid qilishga ruhsat berdingiz.", show_alert=True)
    message = await call.message.edit_reply_markup()
    await call.message.reply('Xaridga ruxsat berildi✅✅✅')


@dp.message_handler(text="/allproducts", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_products()
    print(users[0][0])
    await message.answer(users)


@dp.message_handler(text="/delete", user_id=ADMINS)
async def get_all_users(message: types.Message, state: FSMContext):
    await message.answer('O\'chirmoqchi bo\'lgan mahsulotingizni id raqamini kiriting: ')
    await state.set_state('del_id')


@dp.message_handler(state='del_id', user_id=ADMINS)
async def get_all_users(message: types.Message, state: FSMContext):
    del_id = message.text
    db.delete_product(id=del_id)
    await message.answer('Mahsulot bazadan olib tashlandi')
    await state.finish()
