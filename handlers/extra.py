from aiogram import types, Dispatcher
from config import bot, ADMINS


async def echo(message: types.Message):
    isNum = message.text.isdigit()
    if isNum == True:
        num = int(message.text)
        res = num ** 2
        await bot.send_message(message.from_user.id,res)
    else:
        await bot.send_message(message.from_user.id, message.text)

    if message.text.startswith('!pin'):   #Закрепеление сообщения
        if message.chat.type != 'private':
            if not message.reply_to_message:
                await message.answer('Команда должна быть не в личике а в группе!')
            else:
                await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

    if message.text.startswith('game'):      # Игра для администраторов
        if message.chat.type != 'private':
            if message.from_user.id not in ADMINS:
                await message.answer('Ты не мой хозяин!!!')
            else:
                await bot.send_message(message.chat.id, 'Для бота')
                a = await bot.send_dice(message.chat.id)
                await bot.send_message(message.chat.id, 'Для игрока')
                b = await bot.send_dice(message.chat.id)
                if a.dice.value > b.dice.value:
                    await bot.send_message(message.chat.id, 'Бот выиграл')
                else:
                    await bot.send_message(message.chat.id, 'Вы выиграли')
        else:
            await message.answer('Пиши в группу')


def register_handlers_callback(dp: Dispatcher):
    dp.register_message_handler(echo)