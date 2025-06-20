from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.statuses.status import Create
from bot.utils.dnd_api import get_races, get_classes
from bot.keyboards.inline import list_races_callback, list_classes_callback

character = Router()

@character.message(F.text == "Создать персонажа")
async def cmd_create(message: Message, state: FSMContext):
    await state.set_state(Create.race)

    text = ""
    for item in get_races():
        text += f"{item}\n"
    await message.answer(text=f"выбери рассу за которую хочешь играть:",
                              reply_markup=await list_races_callback())


@character.callback_query(F.data.startswith("расса_"))
async def handle_button(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Create.clas)
    await state.update_data(race=callback.data)

    await callback.message.edit_text("выберите класс за который хотите поиграть:",
                                     reply_markup=await list_classes_callback())



@character.callback_query(F.data.startswith("класс_"))
async def handle_button(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Create.background)
    await state.update_data(clas=callback.data)

    data = await state.get_data()
    await callback.message.edit_text(f"у вас получилось так:{data['race'], data['clas']}",)