from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from keyboards import client_kb
import pyqrcode as py
from config import bot


class FSM_QR_CODE_GENERATOR(StatesGroup):
    start = State()
    value = State()


async def def_start(mesg: types.Message):
    await FSM_QR_CODE_GENERATOR.start.set()
    await mesg.answer("Введите что нужно сгенерировать:", reply_markup=client_kb.cancel_markup)
    await FSM_QR_CODE_GENERATOR.next()


async def generator(mesg: types.Message):
    qr_code = py.create(mesg.text)                          # генерация qr code
    qr_code.png('code.png', scale=6)                        # scale это масштаб qr coda

    with open('code.png', 'rb') as photo:
        await bot.send_photo(mesg.chat.id, photo)


async def cancel(message: types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state:
        await state.finish()
        await message.answer('Понял принял!')


def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(cancel, state='*', commands=['Отмена'])
    dp.register_message_handler(def_start, commands=['qrcode'])
    dp.register_message_handler(generator, state=FSM_QR_CODE_GENERATOR.value)
