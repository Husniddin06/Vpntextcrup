# bot.py

import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database import init_db

# Routers
from handlers import start, tariffs, payment, admin, instruction

async def main():
    await init_db()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    # Include routers
    dp.include_router(start.router)
    dp.include_router(tariffs.router)
    dp.include_router(payment.router)
    dp.include_router(admin.router)
    dp.include_router(instruction.router)
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
