from aiogram.types import Message,ContentTypes
from config import dp

@dp.message_handler(content_types="text")
async def texts(message:Message):
    await message.answer(f"{message.from_user.full_name} sen {message.text} xabarni yubording")

@dp.message_handler(content_types="sticker")
async def stikerlar(message:Message):

    await message.reply(f"seni stikeringni emojisi {message.sticker.emoji}")
    await message.answer_sticker("CAACAgIAAxkBAAICjWR1y1L7TjN5hKu-qzx2Yp7uBi--AAIKAAPANk8T_w2uPugO_QgvBA")
    # print(message.sticker.file_id)

@dp.message_handler(content_types=ContentTypes().PHOTO)#content_types="photo"
async def rasmlar(message:Message):
    await message.answer("sen rasm yubording")

@dp.message_handler(content_types="contact")
async def kontakt(message:Message):
    await message.reply(message.contact.phone_number)
