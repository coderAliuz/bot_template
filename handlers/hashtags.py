from aiogram.types import Message
from config import dp

@dp.message_handler(hashtags="money")
@dp.message_handler(text="money")
@dp.message_handler(hashtags=["pul","dengi"])
async def money(message:Message):
    await message.answer("Akang kuchaydi ||uje||.")