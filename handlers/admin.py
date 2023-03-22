from aiogram import types, Dispatcher
from database.bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def delete_data(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await message.answer(
            f"Пользователь {user[1]} Направление {user[3]}, age= {user[-2]} группа{user[-1]}",
            reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {user[2]}",
                                                                         callback_data=f"DELETE {user[0]}"))
        )


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("DELETE ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await call.message.delete()


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(delete_data, commands=["del"])
    dp.register_callback_query_handler(complete_delete,
                                lambda call: call.data and call.data.startswith("DELETE "))
