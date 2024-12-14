from functools import wraps

from aiogram import types

from db_handler.work_db import is_user_db


def is_user(func):
    """
        Функция декоратор, проверяет есть ли пользователь в базе данных,
        если есть, то выполняет функцию, которую задекорировали, иначе
        бот отправит сообщение Вас нет в базе данных!

        Аргументы:
        fuc - функция, которая буду задекорирована

        Возвращает выполнение функции
        """
    @wraps(func)
    async def wrapper(message: types.Message, *args, **kwargs):

        result_is_user_db = is_user_db(message.from_user.id)
        if result_is_user_db:
            return await func(message, *args, **kwargs)
        else:
            await message.answer('Вас нет в базе данных!')

    return wrapper
