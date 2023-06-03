from aiogram.types import Message
from config import dp

@dp.message_handler(chat_id=5906451521,text="admin")
async def admin(message:Message):
    await message.answer("Salom admin")