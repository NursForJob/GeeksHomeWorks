from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


# @dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Сколько Минут в году?"
    answers = [
        "36500000",
        "2589200",
        "15768000",
        "32085500",
        "100000000",
        "5055500",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="умножь 60 секунд на 8760 минут ",
        open_period=10,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Следующее', callback_data="button_3")
    markup.add(button)

    question = 'Сколько планет в слонечной системе? '
    answer = [
        '6',
        '4',
        '9',
        '8',
        '7',
        '10'
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        type='quiz',
        correct_option_id=2,
        explanation='Такое стыдно не знать,',
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")
