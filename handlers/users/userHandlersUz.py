import asyncio
import sqlite3

import aiogram.bot.api
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from data.config import ADMINS
from keyboards.default.language import dating, MainMenu, Clothes, Shopping_uz, finish_uz, location, BoshMenu
from aiogram.dispatcher import FSMContext

from keyboards.inline.manage_post import post_callback, confirmation_keyboard
from loader import dp, db, bot
from states.shopProduct import ShopProduct
from utils.photograph import photo_link


@dp.message_handler(text='🇺🇿UZ')
async def uzbek(message: types.Message):
    video_url = 'https://t.me/foto_va_mp3lar_olami_575/111'
    await message.answer_video(video=video_url,
                               caption='🎥Botdan foydalanish haqida video yo\'riqnoma',
                               reply_markup=dating)


@dp.message_handler(text='Video yo\'riqnoma bilan tanishdim')
@dp.message_handler(text='⬅️Ortga', state='*')
@dp.message_handler(text='/menu_uz', state='*')
@dp.message_handler(text='Bosh menu', state='*')
async def dating_uz(message: types.Message):
    await message.answer('Bosh menu: ',
                         reply_markup=MainMenu)


# MainMenu menusidagi sinflarning handlerlari
@dp.message_handler(text='👕Kiyimlar', state='*')
async def dating_uz(message: types.Message):
    await message.answer('Kiyimlar menusi: ', reply_markup=Clothes)


@dp.message_handler(text='📱Murojaat uchun', state='*')
async def murojaat(message: types.Message):
    await message.answer('Murojaatlar uchun bizning admin: @SHAXSWEAR_ADMIN')


@dp.message_handler(text='🔎Id bo\'yicha qidirish', state='*')
async def id_search(message: types.Message, state: FSMContext):
    await message.answer('Olmoqchi bo\'lgan mahsulotingizni id raqamini kiriting: \n\n'
                         '<i>Id raqamni bilmasangiz bizning rasmiy kanalimizdan bilib olishingiz mummkin.</i> \n'
                         '<i>Bizning rasmiy kanalimiz: <b>@SHAXSWEAR</b></i>',
                         reply_markup=ReplyKeyboardRemove())

    await ShopProduct.id_search.set()


# Id bo'yicha qidirish


@dp.message_handler(state=ShopProduct.id_search)
async def id_search(message: types.Message, state: FSMContext):
    id_product = message.text
    await state.update_data(
        {'id_product': id_product}
    )
    # id_product = int(id_product)
    try:
        product = db.select_product(id=id_product)
    except sqlite3.IntegrityError as err:
        await message.answer('Bunaqa id raqamli mahsulot yo\'q. Iltimos to\'g\'irlab kiriting!!!')
        await state.finish()
    await message.reply_photo(product[2], caption=f'📌Id raqam: <b>{id_product}</b>\n\n'
                                                  f'✏️Kategoriyalar: <b>{product[1]}</b>\n\n'
                                                  f'📄Mahsulot haqida ma\'lumot: \n<b>{product[4]}</b>\n\n'
                                                  f'💵Narxi: <b>{product[3]} so\'m</b>\n\n'
                                                  f"📲 Bizni <a href='https://t.me/SHAXSWEAR'>telegram</a> "
                                                  f"kanalimizda kuzatib boring",
                              reply_markup=Shopping_uz)
    await ShopProduct.next()


# kiyimlar menusining handlerlari
@dp.message_handler(text='🥾Krasovkalar')
async def shoes(message: types.Message):
    products = db.select_all_products()
    i = 0
    for product in products:
        product_id = product[0]
        if product[1] == '🥾Krasovkalar':
            await message.answer_photo(product[2], caption=f'📌Id raqam: <b>{product_id}</b>\n\n'
                                                           f'✏️Kategoriyalar: <b>{product[1]}</b>\n\n'
                                                           f'📄Mahsulot haqida ma\'lumot: \n<b>{product[4]}</b>\n\n'
                                                           f'💵Narxi: <b>{product[3]} so\'m</b>\n\n'
                                                           f"📲 Bizni <a href='https://t.me/SHAXSWEAR'>telegram</a> "
                                                           f"kanalimizda kuzatib boring", )
            await asyncio.sleep(0.05)
            i += 1
    if i == 0:
        await message.answer('Uzr, hozircha bu mahsulotdan yo\'q')


@dp.message_handler(text='👖Tolstovka va shalvar')
async def shoes(message: types.Message):
    products = db.select_all_products()
    i = 0
    for product in products:
        product_id = product[0]
        if product[1] == '👖Tolstovka va shalvar':
            await message.answer_photo(product[2], caption=f'📌Id raqam: <b>{product_id}</b>\n\n'
                                                           f'✏️Kategoriyalar: <b>{product[1]}</b>\n\n'
                                                           f'📄Mahsulot haqida ma\'lumot: \n<b>{product[4]}</b>\n\n'
                                                           f'💵Narxi: <b>{product[3]} so\'m</b>\n\n'
                                                           f"📲 Bizni <a href='https://t.me/SHAXSWEAR'>telegram</a> "
                                                           f"kanalimizda kuzatib boring", )
            await asyncio.sleep(0.05)
            i += 1
    if i == 0:
        await message.answer('Uzr, hozircha bu mahsulotdan yo\'q')


@dp.message_handler(text='🧢Kepkalar')
async def shoes(message: types.Message):
    products = db.select_all_products()
    i = 0
    for product in products:
        product_id = product[0]
        if product[1] == '🧢Kepkalar':
            await message.answer_photo(product[2], caption=f'📌Id raqam: <b>{product_id}</b>\n\n'
                                                           f'✏️Kategoriyalar: <b>{product[1]}</b>\n\n'
                                                           f'📄Mahsulot haqida ma\'lumot: \n<b>{product[4]}</b>\n\n'
                                                           f'💵Narxi: <b>{product[3]} so\'m</b>\n\n'
                                                           f"📲 Bizni <a href='https://t.me/SHAXSWEAR'>telegram</a> "
                                                           f"kanalimizda kuzatib boring", )
            await asyncio.sleep(0.05)
            i += 1
    if i == 0:
        await message.answer('Uzr, hozircha bu mahsulotdan yo\'q')


@dp.message_handler(text='🧥Kurtkalar')
async def shoes(message: types.Message):
    products = db.select_all_products()
    i = 0
    for product in products:
        product_id = product[0]
        if product[1] == '🧥Kurtkalar':
            await message.answer_photo(product[2], caption=f'📌Id raqam: <b>{product_id}</b>\n\n'
                                                           f'✏️Kategoriyalar: <b>{product[1]}</b>\n\n'
                                                           f'📄Mahsulot haqida ma\'lumot: \n<b>{product[4]}</b>\n\n'
                                                           f'💵Narxi: <b>{product[3]} so\'m</b>\n\n'
                                                           f"📲 Bizni <a href='https://t.me/SHAXSWEAR'>telegram</a> "
                                                           f"kanalimizda kuzatib boring", )
            await asyncio.sleep(0.05)
            i += 1
    if i == 0:
        await message.answer('Uzr, hozircha bu mahsulotdan yo\'q')


@dp.message_handler(text='🎒Sumka va ryukzaklar')
async def shoes(message: types.Message):
    products = db.select_all_products()
    i = 0
    for product in products:
        product_id = product[0]
        if product[1] == '🎒Sumka va ryukzaklar':
            await message.answer_photo(product[2], caption=f'📌Id raqam: <b>{product_id}</b>\n\n'
                                                           f'✏️Kategoriyalar: <b>{product[1]}</b>\n\n'
                                                           f'📄Mahsulot haqida ma\'lumot: \n<b>{product[4]}</b>\n\n'
                                                           f'💵Narxi: <b>{product[3]} so\'m</b>\n\n'
                                                           f"📲 Bizni <a href='https://t.me/SHAXSWEAR'>telegram</a> "
                                                           f"kanalimizda kuzatib boring", )
            await asyncio.sleep(0.05)
            i += 1
    if i == 0:
        await message.answer('Uzr, hozircha bu mahsulotdan yo\'q')


@dp.message_handler(text='Xarid qilish', state=ShopProduct.shop)
async def xarid(message: types.Message, state: FSMContext):
    await message.answer('Rangini yozing: \n\n'
                         '<i>Yuqoridagi xabarda mahsulotning mavjud ranglari yozilgan shular orasidan tanlang!!!</i>',
                         reply_markup=ReplyKeyboardRemove())
    await ShopProduct.next()


@dp.message_handler(state=ShopProduct.color)
async def color(message: types.Message, state: FSMContext):
    color_product = message.text
    await state.update_data(
        {'color': color_product}
    )
    await message.answer('O\'lchamini yozing: \n\n'
                         '<i>Yuqoridagi xabarda mahsulotning mavjud o\'lchamlari '
                         'yozilgan shular orasidan tanlang!!!</i>')
    await ShopProduct.next()


@dp.message_handler(state=ShopProduct.size)
async def size(message: types.Message, state: FSMContext):
    size_product = message.text
    await state.update_data(
        {'size': size_product}
    )
    await message.answer('🔢Nechta olmoqchisiz? ')
    await ShopProduct.next()


@dp.message_handler(state=ShopProduct.amount)
async def amount_t(message: types.Message, state: FSMContext):
    amount_p = message.text
    await state.update_data(
        {'amount': amount_p}
    )
    await message.answer('📝 To\'liq ism-familiyangizni kiriting: ')
    await ShopProduct.next()


@dp.message_handler(state=ShopProduct.full_name)
async def full_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'full_name': name}
    )
    await message.answer('📝 To\'liq manzilingizni yozin: ')
    await ShopProduct.next()


@dp.message_handler(state=ShopProduct.address)
async def address(message: types.Message, state: FSMContext):
    address_user = message.text
    await state.update_data(
        {'address': address_user}
    )
    await message.answer('📍Lokatsiyangizni yuboring: \n\n'
                         '<i>Buning uchun pastdagi location tugamasini bosing.</i>', reply_markup=location)
    await ShopProduct.next()


@dp.message_handler(content_types='location', state=ShopProduct.location)
async def location_user(message: types.Message, state: FSMContext):
    location = message.location
    await state.update_data(
        {'latitude': location.latitude,
         'longitude': location.longitude}
    )
    await message.answer('📲Telefon raqamingizni yozing: ', reply_markup=ReplyKeyboardRemove())
    await ShopProduct.next()


@dp.message_handler(state=ShopProduct.phone_num)
async def phone(message: types.Message, state: FSMContext):
    phone_num = message.text
    await state.update_data(
        {'phone_num': phone_num}
    )
    await message.answer('💳Karta raqami: 5440810005838189\n'
                         '🧑‍💻F.I.SH: SANJAR PULATOV', reply_markup=finish_uz)
    await ShopProduct.next()


@dp.message_handler(text='✅ To\'lov qildim', state=ShopProduct.payment)
async def payment(message: types.Message, state: FSMContext):
    await message.answer('To\'lov qilganiz haqidagi chekning screen shotini yuboring: ',
                         reply_markup=ReplyKeyboardRemove())
    await ShopProduct.next()


@dp.message_handler(content_types='photo', state=ShopProduct.photo_payment)
async def enter_message(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    link = await photo_link(photo)
    mention = message.from_user.get_mention()

    await message.answer('✅ Arizangiz qabul qilindi. 24 soat mobaynida operatorlarimiz siz bilan bog\'lanadi.')
    await message.answer('Bizga ishonch bildirib xarid qilganingiz uchun minnatdorchilik bildiramz.\n'
                         'Qilgan xaridingiz hayirli bo\'lsin 😊',
                         reply_markup=BoshMenu)
    data = await state.get_data()
    id_product = data.get("id_product")
    color_product = data.get("color")
    size_product = data.get("size")
    amount_product = data.get('amount')
    full_name = data.get('full_name')
    address_user = data.get("address")
    phone_num = data.get("phone_num")
    loc_lat = data.get('latitude')
    loc_long = data.get('longitude')

    msg = f'📌Id raqam: <b>{id_product}</b>\n\n'
    msg += f'Rangi: <b>{color_product}</b>\n\n'
    msg += f'O\'lchami: <b>{size_product}</b>\n\n'
    msg += f'Soni: <b>{amount_product}</b>\n\n'
    msg += f'F.I.Sh: <b>{full_name}</b>'
    msg += f'Manzili: <b>{address_user}</b>\n\n'
    msg += f'Telefon raqami: <b>{phone_num}</b>'

    await state.finish()
    await bot.send_message(ADMINS[1], f"Foydalanuvchi {mention} quyidagi mahsulotni sotib oldi. Chekni tekshiring.\n\n")
    await bot.send_photo(ADMINS[1],
                         photo=link,
                         caption=msg,
                         reply_markup=confirmation_keyboard)
    await bot.send_location(ADMINS[1],
                            latitude=loc_lat,
                            longitude=loc_long)


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=ShopProduct.to_admin)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Xarid rad etildi.")


@dp.message_handler(state=ShopProduct.to_admin)
async def post_unknown(message: types.Message):
    await message.answer("Ruxsat berish yoki rad etishni tanlang☝️☝️☝️")
