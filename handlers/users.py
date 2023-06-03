from aiogram.types import Message
from config import dp

@dp.message_handler(commands="start",is_forwarded=False)
async def deeplink(message:Message):
    args=message.get_args()
    if args:
        await message.answer(f"Seni {args} taklif qildi")

@dp.message_handler(is_forwarded=True)
async def forward(message:Message):
    await message.answer(message.forward_sender_name)    