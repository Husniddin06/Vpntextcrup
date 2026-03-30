# keyboards/admin_kb.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_payment_kb(payment_id):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("✅ Подтвердить", callback_data=f"confirm_{payment_id}"),
        InlineKeyboardButton("❌ Отклонить", callback_data=f"reject_{payment_id}")
    )
    return kb
