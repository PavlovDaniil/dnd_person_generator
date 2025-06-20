from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.statuses.status import Create
from bot.utils.dnd_api import get_races, get_classes
from bot.keyboards.inline import list_races_callback

character = Router()

@character.message(F.text == "Создать персонажа")
async def cmd_create(message: Message):
    text = ""
    for item in get_races():
        text += f"{item}\n"
    await message.answer(text=f"выбери рассу за которую хочешь играть:",
                              reply_markup=await list_races_callback())