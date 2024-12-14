# - *- coding: utf- 8 - *-
from aiogram import Dispatcher, F

from bot.routers import main_start


# Регистрация всех роутеров
def register_all_routers(dp: Dispatcher):
    # Подключение фильтров
    dp.message.filter(F.chat.type == "private")  # Работа бота только в личке - сообщения
    dp.callback_query.filter(F.message.chat.type == "private")  # Работа бота только в личке - колбэки

    # Подключение обязательных роутеров
    dp.include_router(main_start.router)  # Роутер основных команд