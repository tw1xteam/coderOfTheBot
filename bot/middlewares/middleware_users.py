# - *- coding: utf- 8 - *-
from aiogram import BaseMiddleware
from aiogram.types import User

from bot.database.db_users import Userx
from bot.utils.misc.bot_logging import bot_logger
from bot.utils.const_functions import clear_html


# Проверка юзера в БД и его добавление
class ExistsUserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        this_user: User = data.get("event_from_user")

        if not this_user.is_bot:
            get_user = Userx.get(user_id=this_user.id)

            user_id = this_user.id
            user_login = this_user.username
            user_name = clear_html(this_user.full_name)

            if user_name is None: user_name = ""
            if user_login is None: user_login = ""

            if get_user is None:
                Userx.add(user_id, user_login.lower(), user_name)
                bot_logger.warning(f"USER CREATED | USER: {user_id}:{user_name}")
            else:
                if user_name != get_user.user_name:
                    Userx.update(get_user.user_id, user_name=user_name)
                    bot_logger.warning(f"USERNAME CHANGED, UPDATE! | USER: {user_id}:{user_name}")

                if user_login.lower() != get_user.user_login:
                    Userx.update(get_user.user_id, user_login=user_login.lower())
                    bot_logger.warning(f"LOGIN CHANGED, UPDATE! | USER: {user_id}:{user_name}")

        return await handler(event, data)
