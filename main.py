from aiogram import Bot, Dispatcher
import asyncio
from dotenv import find_dotenv, load_dotenv
import os

from user_handler.user import router

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()
dp.include_router(router=router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
