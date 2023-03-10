from utils.callbackdata import MyAccountCallBackData
from aiogram.types import CallbackQuery

async def balance(call: CallbackQuery, callback_data: MyAccountCallBackData):
    text = f'Ваш баланс равен "из баззы данных"'
    await call.answer(text)

async def statistics(call: CallbackQuery, callback_data: MyAccountCallBackData):
    text = f'Здесь будет выводиться история ваших заказов'
    await call.answer(text)

async def price(call: CallbackQuery, callback_data: MyAccountCallBackData):
    text = f'Здесь будет выведена цена из базы'
    await call.answer(text)
