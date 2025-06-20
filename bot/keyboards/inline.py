from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.utils.dnd_api import get_races, get_classes

async def list_races_callback():
    keyboard = InlineKeyboardBuilder()
    for item in get_races():
        keyboard.add(InlineKeyboardButton(text=item, url='https://telegram.org'))
    return keyboard.adjust(1).as_markup()
