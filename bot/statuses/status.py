from aiogram.fsm.state import StatesGroup, State


class Create(StatesGroup):
    race = State()
    clas = State()
    background = State()