# - *- coding: utf- 8 - *-
from aiogram import Router, Bot, F
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery

from bot.utils.const_functions import ded
from bot.utils.misc.bot_models import FSM, ARS

router = Router(name=__name__)


@router.message(F.text == '/start')
async def main_start(message: Message, bot: Bot, state: FSM, arSession: ARS):
    await state.clear()

    await message.answer(
        ded("""
            🔸 Бот готов к использованию.
            🔸 Если не появились вспомогательные кнопки
            🔸 Введите /start
        """)
    )
