# - *- coding: utf- 8 - *-
from aiogram import BaseMiddleware, types
from aiogram.types import User
from bot.utils.misc.bot_logging import bot_logger


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        this_user: User = data.get("event_from_user")

        if not this_user.is_bot:
            if isinstance(event, types.Message):
                bot_logger.warning(f"MESSAGE: {event.text} | USER: {this_user.id}:{this_user.username}")
        return await handler(event, data)