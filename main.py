from aiogram.utils import executor
import logging

from config import dp
from handlers import client,callback,extra,admin

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_callback(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)