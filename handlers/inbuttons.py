from aiogram.types import Message,CallbackQuery
from config import dp
from keyboards import test_in_kb,raqam_kb
from random import randint

@dp.message_handler(commands="inline")
async def inline(message:Message):
    await message.answer("Ushbu xabar osti tugmasi siz uchun",reply_markup=test_in_kb)

@dp.callback_query_handler(text="Alisher")
async def callback(call:CallbackQuery):
    # await call.answer("Sen test inline tugmasini bosding",show_alert=True)
    # name=call.message.chat.full_name
    # await call.message.answer(f"{name} test inline tugmasini bosding")

    data=call.data
    await call.answer(data,show_alert=True)

@dp.callback_query_handler(text="random")
async def rand(call:CallbackQuery):
    tasodif=randint(10,1000)
    await call.message.answer(f"Tasodifiy son {tasodif}")


@dp.message_handler(commands="kara")
async def kara(message:Message):
    await message.answer("Kerakli raqamni bos",reply_markup=raqam_kb())

@dp.callback_query_handler(text_startswith="raqam")
async def karakara(call:CallbackQuery):
    data=call.data
    son=int(data.split("_")[1])
    info=""
    for i in range(1,11):
        info+=f"{son}*{i}={son*i}\n"

    await call.message.reply(info)

