import asyncio
import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from data.config import ADMINS
from keyboards.default.language import dating_ru, MainMenu_ru, Clothes_ru, Shopping_ru, finish_ru, location, BoshMenuRu
from keyboards.inline.manage_post import confirmation_keyboard_ru, post_callback, confirmation_keyboard
from loader import dp, db, bot
from states.shopProduct import ShopProduct, ShopProductRu
from utils.photograph import photo_link


@dp.message_handler(text='🇷🇺RU')
async def uzbek(message: types.Message):
    video_url = 'https://t.me/foto_va_mp3lar_olami_575/112'
    await message.answer_video(video=video_url, caption='🎥Видео инструкция для пользования бота',
                               reply_markup=dating_ru)


@dp.message_handler(text='✅ Я ознакомился видео инструкцией')
@dp.message_handler(text='⬅️Назад', state='*')
@dp.message_handler(text='/menu_ru', state='*')
@dp.message_handler(text='Главное меню', state='*')
async def dating_uz(message: types.Message):
    await message.answer('Главное меню: ',
                         reply_markup=MainMenu_ru)


@dp.message_handler(text='👕Одежда', state='*')
async def dating_uz(message: types.Message):
    await message.answer('Меню одежды: ', reply_markup=Clothes_ru)


@dp.message_handler(text='📱 Поддержка', state='*')
async def murojaat(message: types.Message):
    await message.answer('Наш админ для справок: @SHAXSWEAR_ADMIN')


# Id bo'yicha qidirish
@dp.message_handler(text='🔎Поиск по id', state='*')
async def id_search(message: types.Message, state: FSMContext):
    await message.answer('Введите идентификационный номер продукта, который хотите приобрести.: \n\n'
                         '<i>Если вы не знаете идентификационный номер, вы можете узнать его на '
                         'нашем официальном канале.</i> \n'
                         '<i>Наш официальный канал: <b>@SHAXSWEAR</b></i>',
                         reply_markup=ReplyKeyboardRemove())

    await ShopProductRu.id_searchRu.set()


@dp.message_handler(state=ShopProductRu.id_searchRu)
async def id_search(message: types.Message, state: FSMContext):
    id_product = message.text
    await state.update_data(
        {'id_product': id_product}
    )
    # id_product = int(id_product)
    try:
        product = db.select_product(id=id_product)
    except sqlite3.IntegrityError as err:
        await message.answer('Такого цифрового продукта нет. Пожалуйста исправьте!!!')
        await state.finish()
    await message.reply_photo(product[2], caption=f'📌ID номер: <b>{id_product}</b>\n\n'
                                                  f'✏️Категория: <b>{product[1]}</b>\n\n'
                                                  f'📄Информация о товаре: \n<b>{product[4]}</b>\n\n'
                                                  f'💵Цена: <b>{product[3]} сум</b>\n\n'
                                                  f'📲Переходите на наш '
                                                  f'<a href=\'https://t.me/SHAXSWEAR\'>телеграмм</a> канал',
                              reply_markup=Shopping_ru)
    await ShopProductRu.next()


# kiyimlar menusining handlerlari
@dp.message_handler(text='🥾Кроссовки')
async def shoes(message: types.Message):
    products = db.select_all_products()
    i = 0
    for product in products:
        product_id = product[0]
        if product[1] == '🥾Krasovkalar':
            await message.answer_photo(product[2], caption=f'📌ID номер: <b>{product_id}</b>\n\n'
                                                           f'✏️Категория: <b>{product[1]}</b>\n\n'
                                                           f'📄Информация о товаре: \n<b>{product[4]}</b>\n\n'
                                                           f'💵Цена: <b>{product[3]} сум</b>\n\n'
                                                           f'📲Переходите на наш '
                                                           f'<a href=\'https://t.me/SHAXSWEAR\'>телеграмм</a> канал')
            await asyncio.sleep(0.05)
            i += 1
    if i == 0:
        await message.answer('Извините, этот товар сейчас недоступен')


@dp.message_handler(text='👖Толстовка и брюки')
async def shoes(message: types.Message):
    products = db.select_all_products()
    i = 0
    for product in products:
        product_id = product[0]
        if product[1] == '👖Tolstovka va shalvar':
            await message.answer_photo(product[2], caption=f'📌ID номер: <b>{product_id}</b>\n\n'
                                                           f'✏️Категория: <b>{product[1]}</b>\n\n'
                                                           f'📄Информация о товаре: \n<b>{product[4]}</b>\n\n'
                                                           f'💵Цена: <b>{product[3]} сум</b>\n\n'
                                                           f'📲Переходите на наш '
                                                           f'<a href=\'https://t.me/SHAXSWEAR\'>телеграмм</a> канал')
            await asyncio.sleep(0.05)
            i += 1
    if i == 0:
        await message.answer('Извините, этот товар сейчас недоступен')


@dp.message_handler(text='🧢Шапки')
async def shoes(message: types.Message):
    products = db.select_all_products()
    i = 0
    for product in products:
        product_id = product[0]
        if product[1] == '🧢Kepkalar':
            await message.answer_photo(product[2], caption=f'📌ID номер: <b>{product_id}</b>\n\n'
                                                           f'✏️Категория: <b>{product[1]}</b>\n\n'
                                                           f'📄Информация о товаре: \n<b>{product[4]}</b>\n\n'
                                                           f'💵Цена: <b>{product[3]} сум</b>\n\n'
                                                           f'📲Переходите на наш '
                                                           f'<a href=\'https://t.me/SHAXSWEAR\'>телеграмм</a> канал')
            await asyncio.sleep(0.05)
            i += 1
    if i == 0:
        await message.answer('Извините, этот товар сейчас недоступен')


@dp.message_handler(text='🧥Куртки')
async def shoes(message: types.Message):
    products = db.select_all_products()
    i = 0
    for product in products:
        product_id = product[0]
        if product[1] == '🧥Kurtkalar':
            await message.answer_photo(product[2], caption=f'📌ID номер: <b>{product_id}</b>\n\n'
                                                           f'✏️Категория: <b>{product[1]}</b>\n\n'
                                                           f'📄Информация о товаре: \n<b>{product[4]}</b>\n\n'
                                                           f'💵Цена: <b>{product[3]} сум</b>\n\n'
                                                           f'📲Переходите на наш '
                                                           f'<a href=\'https://t.me/SHAXSWEAR\'>телеграмм</a> канал')
            await asyncio.sleep(0.05)
            i += 1
    if i == 0:
        await message.answer('Извините, этот товар сейчас недоступен')


@dp.message_handler(text='🎒Сумки и рюкзаки')
async def shoes(message: types.Message):
    products = db.select_all_products()
    i = 0
    for product in products:
        product_id = product[0]
        if product[1] == '🎒Sumka va ryukzaklar':
            await message.answer_photo(product[2], caption=f'📌ID номер: <b>{product_id}</b>\n\n'
                                                           f'✏️Категория: <b>{product[1]}</b>\n\n'
                                                           f'📄Информация о товаре: \n<b>{product[4]}</b>\n\n'
                                                           f'💵Цена: <b>{product[3]} сум</b>\n\n'
                                                           f'📲Переходите на наш '
                                                           f'<a href=\'https://t.me/SHAXSWEAR\'>телеграмм</a> канал')
            await asyncio.sleep(0.05)
            i += 1
    if i == 0:
        await message.answer('Извините, этот товар сейчас недоступен')


@dp.message_handler(text='Купить', state=ShopProductRu.shopRu)
async def xarid(message: types.Message, state: FSMContext):
    await message.answer('Введите цвет: \n\n'
                         '<i>Выберите из списка доступных цветов продукта в сообщении выше.!!!</i>',
                         reply_markup=ReplyKeyboardRemove())
    await ShopProductRu.next()


@dp.message_handler(state=ShopProductRu.colorRu)
async def color(message: types.Message, state: FSMContext):
    color_product = message.text
    await state.update_data(
        {'color': color_product}
    )
    await message.answer('Введите размер: \n\n'
                         '<i>В сообщении выше выберите доступные размеры продукта.!!!</i>')
    await ShopProductRu.next()


@dp.message_handler(state=ShopProductRu.sizeRu)
async def size(message: types.Message, state: FSMContext):
    size_product = message.text
    await state.update_data(
        {'size': size_product}
    )
    await message.answer('🔢Сколько вы хотите купить?: ')
    await ShopProductRu.next()


@dp.message_handler(state=ShopProductRu.amountRu)
async def amount(message: types.Message, state: FSMContext):
    amount_p = message.text
    await state.update_data(
        {'amount': amount_p}
    )
    await message.answer('📝 Ведите Ваш Ф.И.О.: ')
    await ShopProductRu.next()


@dp.message_handler(state=ShopProductRu.full_nameRu)
async def name(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(
        {'name': full_name}
    )
    await message.answer('📝 Введите ваш адрес: ')
    await ShopProductRu.next()


@dp.message_handler(state=ShopProductRu.addressRu)
async def address(message: types.Message, state: FSMContext):
    address_user = message.text
    await state.update_data(
        {'address': address_user}
    )
    await message.answer('📍Отбросьте местоположение: \n\n'
                         '<i>Для этого нажмите кнопку location ниже.</i>', reply_markup=location)
    await ShopProductRu.next()


@dp.message_handler(content_types='location', state=ShopProductRu.locationRu)
async def location_user(message: types.Message, state: FSMContext):
    location = message.location
    await state.update_data(
        {'latitude': location.latitude,
         'longitude': location.longitude}
    )
    await message.answer('📲Оставьте свой номер телефона: ', reply_markup=ReplyKeyboardRemove())
    await ShopProductRu.next()


@dp.message_handler(state=ShopProductRu.phone_numRu)
async def phone(message: types.Message, state: FSMContext):
    phone_num = message.text
    await state.update_data(
        {'phone_num': phone_num}
    )
    await message.answer('💳Номер карты: 5440810005838189\n'
                         '🧑‍💻Ф.И.О: SANJAR PULATOV', reply_markup=finish_ru)
    await ShopProductRu.next()


@dp.message_handler(text='✅ Я оплатил', state=ShopProductRu.paymentRu)
async def payment(message: types.Message, state: FSMContext):
    await message.answer('Отправьте снимок экрана чека, который вы оплатили: ',
                         reply_markup=ReplyKeyboardRemove())
    await ShopProductRu.next()


@dp.message_handler(content_types='photo', state=ShopProductRu.photo_paymentRu)
async def enter_message(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    link = await photo_link(photo)
    mention = message.from_user.get_mention()
    await message.answer('✅Ваша заявка принята в течении 24 часов наши операторы свяжутся свами')
    await message.answer('Благодарим Вас за покупку и доверие к нам. Пусть Ваша покупка будет удачной 😊 ',
                         reply_markup=BoshMenuRu)
    data = await state.get_data()
    id_product = data.get("id_product")
    color_product = data.get("color")
    size_product = data.get("size")
    amount_product = data.get('amount')
    full_name = data.get('name')
    address_user = data.get("address")
    phone_num = data.get("phone_num")
    loc_lat = data.get('latitude')
    loc_long = data.get('longitude')

    msg = f'📌Id raqam: <b>{id_product}</b>\n\n'
    msg += f'Rangi: <b>{color_product}</b>\n\n'
    msg += f'O\'lchami: <b>{size_product}</b>\n\n'
    msg += f'Soni: <b>{amount_product}</b>\n\n'
    msg += f'F.I.Sh: <b>{full_name}</b>\n\n'
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


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=ShopProductRu.to_adminRu)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Покупка отклонена.")


@dp.message_handler(state=ShopProductRu.to_adminRu)
async def post_unknown(message: types.Message):
    await message.answer("Выберите разрешить или отклонить☝️☝️☝️")
