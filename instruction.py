# handlers/instruction.py

from aiogram import Router, types
from config import VPN_LINK, SUPPORT_USERNAME
from keyboards.menu import main_menu
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(lambda m: m.text == "📖 Инструкция")
async def instruction(message: types.Message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔗 Подключить VPN", url=VPN_LINK))
    text = "📖 Инструкция по подключению VPN:\n" \
           "1. Установите V2RayTun (Play Market / App Store)\n" \
           "2. Нажмите кнопку Подключить VPN\n" \
           "3. Разрешите открыть приложение\n" \
           "4. Подключитесь\n\n" \
           f"Если не работает — напишите в поддержку {SUPPORT_USERNAME}"
    await message.answer(text, reply_markup=kb)
