# handlers/tariffs.py

from aiogram import Router, types
from config import TARIFFS

router = Router()

@router.message(lambda m: m.text == "💰 Тарифы")
async def show_tariffs(message: types.Message):
    text = "💰 Наши тарифы:\n\n"
    for key, t in TARIFFS.items():
        text += f"{t['name']} — {t['price']} ₽\n"
    await message.answer(text)
