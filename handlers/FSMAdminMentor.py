from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb
from database.bot_db import sql_insert
from config import ADMINS


class FSMAdmin(StatesGroup):
    name = State()
    direction_mentor = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('Ты не админ!')
    else:
        if message.chat.type == 'private':
            await FSMAdmin.name.set()
            await message.answer("Как зовут?", reply_markup=client_kb.cancel_markup)
        else:
            await message.answer('Пиши в личку', reply_markup=client_kb.cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = message.from_user.username
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какое направлени? ", reply_markup=client_kb.direction_markup)


async def load_direction(message: types.Message, state: FSMContext):
    if message.text not in ['Python', 'Java', 'Android(Kotlin)', 'UX design']:
        await message.answer("Неправильный вариант")
    else:
        async with state.proxy() as data:
            data['direction'] = message.text
        await FSMAdmin.next()
        await message.answer('Возраст? ')


async def load_age(message: types.Message, state:FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer('Какая группа? ', reply_markup=client_kb.group_markup)


async def load_group(message: types.Message, state:FSMContext):
    if message.text not in ['27', '28', '29']:
        await message.answer("Неправильный вариант")
    else:
        async with state.proxy() as data:
            data['group'] = message.text
            await FSMAdmin.next()
            await message.answer('Все верно? ')


async def submit(message: types.Message, state:FSMContext):
    if message.text == "ДА":
        # Запись в БД
        await sql_insert(state)
        await state.finish()
        await message.answer("Ты зареган!")
    elif message.text == "ЗАНОВО":
        await FSMAdmin.name.set()
        await message.answer("Как звать?")
    else:
        await message.answer("НИПОНЯЛ!?")


async def cancel(message: types.Message, state:FSMContext):
    current_state = state.get_state()
    if current_state:
        await state.finish()
        await message.answer('До встречи')


def register_handlers_FSM_anketa(dp: Dispatcher):

    dp.register_message_handler(cancel, state='*', commands=['cancel'])
    dp.register_message_handler(cancel,
                                Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction_mentor)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
