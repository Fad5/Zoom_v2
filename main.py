from aiogram import Bot, Dispatcher, types
import asyncio
from dotenv import find_dotenv, load_dotenv
import os
from aiogram.filters import CommandStart, Command

import parsing
from db_handler import get_user_name, cursor, connection
from data_hadler import download_csv_file

from user_handler import user
from parsing import get_info_zooms

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()
dp.include_router(user.user_router)


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Hi')


@dp.message(Command("today"))
async def today_work_day(message: types.Message):
    user_name = get_user_name(message.from_user.id, connection, cursor)
    for info_zoom in parsing.get_info_zooms(user_name):
        await message.answer(info_zoom)


@dp.message(Command("tomorrow"))
async def next_day_work(message: types.Message):
    user_name = get_user_name(message.from_user.id, connection, cursor)
    for info_zoom in get_info_zooms(user_name, day_='next'):
        await message.answer(info_zoom)


@dp.message(Command("upd_db"))
async def upd_db(message: types.Message):
    last_upd = download_csv_file.get_info_last_download()
    await message.answer(last_upd)


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
