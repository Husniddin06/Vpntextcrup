# handlers/admin.py

from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from config import ADMIN_ID, VPN_LINK
from keyboards.admin_kb import admin_payment_kb

router = Router()

# Fake payments storage (for demo, in real use DB should be used)
payments = {}

@router.message(F.from_user.id == ADMIN_ID)
async def admin_panel(message: types.Message):
    text = "🛠 Панель администратора\n\nВсе новые платежи будут отображены здесь."
    await message.answer(text)

# Handle inline buttons
@router.callback_query(lambda c: c.data.startswith("confirm_") or c.data.startswith("reject_"))
async def handle_admin_cb(callback: CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("Вы не администратор!", show_alert=True)
        return

    payment_id = int(callback.data.split("_")[1])
    action = callback.data.split("_")[0]

    if payment_id not in payments:
        await callback.answer("Платеж не найден!", show_alert=True)
        return

    user_id = payments[payment_id]['user_id']

    if action == "confirm":
        text = f"✅ Оплата подтверждена.\nВаш VPN ключ готов."
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("🔗 Подключить VPN", url=VPN_LINK))
        await callback.bot.send_message(user_id, text, reply_markup=kb)
        payments[payment_id]['status'] = 'confirmed'
        await callback.answer("Подтверждено ✅")
    else:
        await callback.bot.send_message(user_id, "❌ Платеж отклонен. Обратитесь к администратору.")
        payments[payment_id]['status'] = 'rejected'
        await callback.answer("Отклонено ❌")
