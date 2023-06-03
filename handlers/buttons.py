from aiogram.types import Message
from config import dp
from aiogram.dispatcher import FSMContext
from keyboards import test_kb,kara_kb,del_kb
import json

@dp.message_handler(commands="test")
async def test(message:Message):
    await message.answer("Manabu tugmalar sen uchun",reply_markup=test_kb)

@dp.message_handler(commands="karakara")
async def karakara(message:Message, state:FSMContext):
    await message.answer("Kerakli raqamni bos raqam",reply_markup=kara_kb)
    await state.set_state("karakara")

@dp.message_handler(state="karakara",text=list(range(1,10)))
async def hisobla(message:Message, state:FSMContext):
    son=int(message.text)
    info=""
    for i in range(1,11):
        info+=f"{son}*{i}={son*i}\n"
    await message.reply(info)
    await state.finish()

@dp.message_handler(commands="del")
async def tozala(message:Message):
    await message.answer("tugmalar tozalandi",reply_markup=del_kb)
