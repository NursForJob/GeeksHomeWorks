from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot,ADMINS
from keyboards.client_kb import start_markup
import time

# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(
        message.chat.id,
        f"Салалекум хозяин {message.from_user.full_name}",
        reply_markup=start_markup
    )


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(
        message.chat.id,
        f"Разбирайся сам!"
    )

# @dp.message_handler(commands=['mem'])
async def mem_commands(message: types.Message):
    photo = open("Troll-Face-Meme-PNG.png", 'rb')
    await bot.send_photo(
        message.chat.id,
        photo
    )

async def dice_commands(message: types.Message):    # Игра dice
        if message.chat.type != 'private':
                await bot.send_message(message.chat.id, 'Для бота')
                a = await bot.send_dice(message.chat.id)
                print(a)
                await bot.send_message(message.chat.id, 'Для игрока')
                b = await bot.send_dice(message.chat.id)
                if a.dice.value == b.dice.value:
                    time.sleep(4)
                    await bot.send_message(message.chat.id, 'Ничья')
                elif a.dice.value > b.dice.value:
                    time.sleep(4)
                    await bot.send_message(message.chat.id, 'Бот выиграл')
                else:
                    time.sleep(4)
                    await bot.send_message(message.chat.id, 'Вы выиграли')
        else:
            await message.answer('Пиши в группу')


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "By whom invented Python?"
    answers = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]
    # await message.answer_poll()
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_commands, commands=['mem'])
    dp.register_message_handler(dice_commands,commands=['dice'])
