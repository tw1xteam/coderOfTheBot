# - *- coding: utf- 8 - *-
import asyncio
import os
import sys

import colorama
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.data.config import get_admins, BOT_TOKEN, BOT_SCHEDULER
from bot.middlewares import register_all_middlwares
from bot.routers import register_all_routers
from bot.services.api_session import AsyncRequestSession
from bot.utils.misc.bot_logging import bot_logger

colorama.init()


# Запуск бота и базовых функций
async def main():
    BOT_SCHEDULER.start()  # Запуск Шедулера
    dp = Dispatcher()  # Образ Диспетчера
    arSession = AsyncRequestSession()  # Пул асинхронной сессии запросов
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # Образ Бота

    register_all_routers(dp)  # Регистрация всех роутеров
    register_all_middlwares(dp) # Регистрация всех мидлваров

    try:

        bot_logger.warning("BOT WAS STARTED")
        print(colorama.Fore.LIGHTYELLOW_EX + f"~~~~~ Bot was started - @{(await bot.get_me()).username} ~~~~~")
        print(colorama.Fore.LIGHTBLUE_EX + "~~~~~ TG developer - @djimbox ~~~~~")
        print(colorama.Fore.RESET)

        if len(get_admins()) == 0: print("***** ENTER ADMIN ID IN settings.ini *****")

        await bot.delete_webhook()
        await bot.get_updates(offset=-1)

        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
            arSession=arSession,
        )
    finally:
        await arSession.close()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        bot_logger.warning("Bot was stopped")
    finally:
        if sys.platform.startswith("win"):
            os.system("cls")
        else:
            os.system("clear")
