from functools import wraps

from aiogram import types


def is_admin(func):
    """
    Функция декоратор, переназначена для разделения доступа,
     если пользователь есть в базе данных админ, то ему предоставляется доступ
    :param func:
    :return:
    """
    @wraps(func)
    async def wrapper(message: types.Message, *args, **kwargs):
        # Написать функцию, которая будет доставать id админов и предоставлять доступ к этой команде
        if message.from_user.id in ['ddd']:
            await message.answer('Ок')
            return await func(message, *args, **kwargs)
        else:
            await message.answer('Доступ ограничен к этой команде!')
    return wrapper
