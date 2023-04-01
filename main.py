from aiogram.utils import executor
import logging

from config import dp, bot, ADMINS
from handlers import client, callback, extra, FSMAdminMentor,admin
from database.bot_db import sql_create
from handlers.shedule import set_shedule

async def on_startup(_):
    await set_shedule()
    await bot.send_message(ADMINS[0], 'Я родился')
    sql_create()


async def on_shutdown(dp):
    await bot.send_message(ADMINS[0], 'Buy Buy Пока')

admin.register_handler_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
FSMAdminMentor.register_handlers_FSM_anketa(dp)

extra.register_handlers_callback(dp)


# def on_startup(dp):
#     await bot.send_message(ADMINS)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
