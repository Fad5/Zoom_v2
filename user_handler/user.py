from aiogram import types, Router
from aiogram.filters import CommandStart, Command

import parsing
from db_handler import get_user_name, cursor, connection

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Hi')


@user_router.message(Command("today"))
async def today_work_day(message: types.Message):
    user_name = get_user_name(message.from_user.id, connection, cursor)
    for info_zoom in parsing.get_info_zooms(user_name):
        await message.answer(info_zoom)


@user_router.message(Command("tomorrow"))
async def next_day_work(message: types.Message):
    user_name = get_user_name(message.from_user.id, connection, cursor)
    for info_zoom in get_info_zooms(user_name, day_='next'):
        await message.answer(info_zoom)


@user_router.message()
async def echo(message: types.Message):
    await message.answer(message.text)
