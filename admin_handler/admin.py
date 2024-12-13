from aiogram import Router, types
from aiogram.filters import Command

from admin_handler.decorators import is_admin

admin_router = Router()


@admin_router.message(Command("add_user"))
@is_admin
async def add_user(message: types.Message):
    """
    """
    await message.answer('ddd')
