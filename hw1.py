from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import logging

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Салалекум хозяин {message.from_user.full_name}"
    )


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Разбирайся сам!"
    )


@dp.message_handler(commands=['mem'])
async def mem_commends(message: types.Message):
    photo = open("C:/Users/User/HomeWork/GeekTechHomeWork/pythonAiogramBotPractice/Troll-Face-Meme-PNG.png",'rb')
    await bot.send_photo(
        message.from_user.id,
        photo
    )


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Кто создал электричество ?"
    answers = [
        "А. Вольта",
        "Ампер",
        "Александр Николаевич Лодыгин.",
        "Д. А. Лачинов",
        "Пьер Кюри",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Бывает, попытайся еще",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Сколько Минут в году?"
    answers = [
        "36500",
        "25892",
        "525600",
        "320855",
        "1000000",
        "50555",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Бывает, попытайся еще",
        open_period=10,
        reply_markup=markup
    )


@dp.message_handler()
async def echo(message: types.Message):
    isNum = message.text.isdigit()
    if isNum == True:
        num = int(message.text)
        res = num ** 2
        await bot.send_message(message.from_user.id,res)
    else:
        await bot.send_message(message.from_user.id, message.text)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
