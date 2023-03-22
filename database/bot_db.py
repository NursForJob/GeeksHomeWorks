import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('База данных подключена! ')

    db.execute("CREATE TABLE IF NOT EXISTS anketa "
               "(id INTEGER PRIMARY KEY, "
               "username VARCHAR(100), "
               "name VARCHAR(50), "
               "direction VARCHAR(15), "
               "age INTEGER, "
               "groups VARCHAR(20))")   #ок-ся в базе данных есть ключевое слово group, при создлании группы у меня постоянно возникала ошибка и не мог понять
    db.commit()


async def sql_insert(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO anketa VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        db.commit()


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (id,))
    db.commit()
