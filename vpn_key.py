# utils/vpn_key.py

from config import VPN_LINK
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def vpn_button():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔗 Подключить VPN", url=VPN_LINK))
    return kb
