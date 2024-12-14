# - *- coding: utf- 8 - *-
from aiogram import Router, Bot, F
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery

from bot.keyboards.reply_main import menu_frep
from bot.utils.const_functions import ded
from bot.utils.misc.bot_models import FSM, ARS

router = Router(name=__name__)


@router.message(F.text == '/start')
async def main_start(message: Message, bot: Bot, state: FSM, arSession: ARS):
    await state.clear()

    await message.answer(
        "<i><b>CoderOfTheBot</b> — это бот, предназначенный для помощи "
        "разработчикам читов в популярных играх, таких как <b>Standoff 2, "
        "Black Russia, Oxide Survival, BLOCK POST MOBILE, BLOCK POST"
        "(PC)</b> и других.</i>",
        reply_markup=menu_frep(message.from_user.id)
    )
