from aiogram import Router, types
from aiogram.filters import CommandStart, Command

import parsing
from data_hadler import download_csv_file
from db_handler import get_user_name, connection, cursor
from parsing import get_info_zooms

router = Router()


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    """
    Функция приветствия
    """
    await message.answer('Hi')


@router.message(Command("tomorrow"))
async def next_day_work(message: types.Message):
    """
    Отображения зуммов на завтра по id пользователя.
    Получаем id пользователя находим в базе данных как он записан
    и начинаем поиск по имени.
    """
    user_name = get_user_name(message.from_user.id, connection, cursor)
    for info_zoom in get_info_zooms(user_name, day_='next'):
        await message.answer(info_zoom)


@router.message(Command("today"))
async def today_work_day(message: types.Message):
    """
    Отображения зуммов на сегодня по id пользователя.
    Получаем id пользователя находим в базе данных как он записан
    и начинаем поиск по имени.
    """
    user_name = get_user_name(message.from_user.id, connection, cursor)
    for info_zoom in parsing.get_info_zooms(user_name):
        await message.answer(info_zoom)


@router.message(Command("upd_db"))
async def upd_db(message: types.Message):
    """
    Функция для отображения даты создания и обновление файла.
    """
    last_upd = download_csv_file.get_info_last_download()
    await message.answer(last_upd)


@router.message(Command("today_zooms"))
async def current_bay(message: types.Message):
    """
    Функция для отображения всех zooms на сегодня
    """
    for zoom in parsing.get_zooms_day():
        await message.answer(zoom)


@router.message(Command("tomorrow_zooms"))
async def current_bay(message: types.Message):
    """
    Функция для отображения всех zooms на завтра
    """
    for zoom in parsing.get_zooms_day('next'):
        await message.answer(zoom)


@router.message()
async def echo(message: types.Message):
    """
    Функция эхо
    """
    await message.answer(message.text)