from functools import wraps

from aiogram import types

from db_handler.work_db import connect_db, is_user_db


def is_user(func):
    """
    Функция декоратор, переназначена для разделения доступа,
     если пользователь есть в базе данных админ, то ему предоставляется доступ
    :param func:
    :return:
    """

    @wraps(func)
    async def wrapper(message: types.Message, *args, **kwargs):
        # Написать функцию, которая будет доставать id админов и предоставлять доступ к этой команде
        result_is_user_db = is_user_db(message.from_user.id)
        print(result_is_user_db)
        if result_is_user_db:
            return await func(message, *args, **kwargs)
        else:
            await message.answer('Вас нет в базе данных!')

    return wrapper
