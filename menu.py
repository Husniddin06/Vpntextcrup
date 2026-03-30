# keyboards/menu.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("🛒 Купить VPN"))
    keyboard.add(KeyboardButton("💰 Тарифы"))
    keyboard.add(KeyboardButton("📖 Инструкция"))
    keyboard.add(KeyboardButton("🆘 Поддержка"))
    return keyboard
