from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Создать персонажа")],
    [KeyboardButton(text="готовые персонажи"), KeyboardButton(text="редактировать персонажа")],
])