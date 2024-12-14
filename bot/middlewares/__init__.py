# - *- coding: utf- 8 - *-
from aiogram import Dispatcher

from bot.middlewares.middleware_logging import LoggingMiddleware


# Регистрация всех миддлварей
def register_all_middlwares(dp: Dispatcher):
    dp.message.middleware(LoggingMiddleware())

