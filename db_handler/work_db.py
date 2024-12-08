import sqlite3


def get_user_name(id_tg: int, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    """Получение 

    Args:
        id_tg (int): _description_
        connection (sqlite3.Connection): _description_
        cursor (sqlite3.Cursor): _description_

    Returns:
        _type_: _description_
    """
    cursor.execute('SELECT *, id_tg FROM Users WHERE id_tg == ?', (id_tg,))
    result = cursor.fetchall()
    if not result:
        return ['Вас не в базе данных']
    user_name = result[0][2]
    connection.commit()
    return user_name


def connect_db():
    """Функция для подключение к базе данных

    Returns:
        _type_: _description_
    """
    connection = sqlite3.connect('data_base_zoom.db')
    cursor = connection.cursor()
    return cursor, connection


def delete_user(id_tg, connection, cursor):
    cursor.execute('DELETE FROM Users WHERE id_tg == ?', (id_tg,))
    connection.commit()
    connection.close()


def create_table(connection, cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    id_tg INTEGER,
    username TEXT NOT NULL)''')
    connection.commit()
    connection.close()


def chenge_user_name():
    pass


def add_user(id_tg: int, user_name: str, connection:
sqlite3.Connection, cursor: sqlite3.Cursor):
    """Функция для добавления пользователя в базу данных
    
    Аргументы:
        id_tg (int): id пользователя telegram
        user_name (str): имя пользователя в exel таблицы
        connection (sqlite3.Connection)
        cursor (sqlite3.Cursor)
    """
    cursor.execute(f"INSERT INTO Users (id_tg, username)VALUES ({id_tg}, '{user_name}');")
    connection.commit()
    connection.close()


cursor, connection = connect_db()
