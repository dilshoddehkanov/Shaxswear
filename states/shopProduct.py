from aiogram.dispatcher.filters.state import StatesGroup, State


class ShopProduct(StatesGroup):
    id_search = State()
    shop = State()
    color = State()
    size = State()
    amount = State()
    full_name = State()
    address = State()
    location = State()
    phone_num = State()
    payment = State()
    photo_payment = State()
    to_admin = State()


class ShopProductRu(StatesGroup):
    id_searchRu = State()
    shopRu = State()
    colorRu = State()
    sizeRu = State()
    amountRu = State()
    full_nameRu = State()
    addressRu = State()
    locationRu = State()
    phone_numRu = State()
    paymentRu = State()
    photo_paymentRu = State()
    to_adminRu = State()
