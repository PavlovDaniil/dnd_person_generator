from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from asyncio import run
from bot import config, commands

bot = Bot(config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(commands)

    await dp.start_polling(bot)

if __name__ == "__main__":
    run(main())