import datetime

from aiogram import Bot
from database.bot_db import sql_command_get_id_name
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from config import bot      #Todo ВОПРОС!!! зачем мы два раза импортировали бота


async def go_to_learn_programming(bot: Bot):
    users = await sql_command_get_id_name()
    for user in users:
        await bot.send_message(user[0], f"Настало время программировать {user[1]}")


async def set_shedule():
    sheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    sheduler.add_job(
        go_to_learn_programming,
        trigger=DateTrigger(
            run_date=datetime.datetime(
                year=2023,
                month=3,
                day=26,
                hour=23,
                minute=53
            )
        ),
        kwargs={"bot": bot}
    )
    sheduler.start()
