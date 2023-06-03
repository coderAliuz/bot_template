from aiogram.types import Message
from config import dp
from aiogram.dispatcher.filters import Text

@dp.message_handler(text="telefon")
async def phone(mess:Message):
    await mess.answer("Senga qanaqa telefon kerak")

@dp.message_handler(text="/yordam")
async def helpme(message:Message):
    await message.reply("vooooy yooordammmmm")

@dp.message_handler(Text(equals=["kimsan","nimasan","qayerdasan"]))
async def kimsan(message:Message):
    await message.answer("Men TURSUNXONMAN!!! sog' bo'lasla")

@dp.message_handler(text_startswith="ali")
async def ali(message:Message):
    await message.answer("sen ali so'zi bilan boshlgan text yubording")

@dp.message_handler(Text(endswith="jon"))
async def ali(message:Message):
    await message.answer("||sen|| jon sozi bilan tugallangan text yubording")

@dp.message_handler(Text(contains="ahmoq"))
async def ahmoq(message:Message):
    await message.reply("siz odob doirasidan chiqib ketvossiz")

@dp.message_handler(text_contains="ona")
async def ona(message:Message):
    await message.reply("Ona buyuk zot")

@dp.message_handler(text="info")
async def nomalum(message:Message):
    await message.answer(message)