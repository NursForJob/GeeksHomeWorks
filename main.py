from aiogram.utils import executor
import logging

from config import dp, bot
from handlers import client, callback, extra, FSMAdminMentor,admin
from database.bot_db import sql_create

admin.register_handler_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
FSMAdminMentor.register_handlers_FSM_anketa(dp)

extra.register_handlers_callback(dp)


# def on_startup(dp):
#     await bot.send_message(ADMINS)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=sql_create())
