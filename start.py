# handlers/start.py

from aiogram import Router, types
from keyboards.menu import main_menu
from config import SUPPORT_USERNAME

router = Router()

@router.message(commands=["start"])
async def start(message: types.Message):
    text = f"👋 Добро пожаловать, {message.from_user.first_name}!\n\n" \
           "Вы можете выбрать одну из опций ниже:"
    await message.answer(text, reply_markup=main_menu())
