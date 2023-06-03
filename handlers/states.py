from aiogram.types import Message
from config import dp
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands="register")
async def register(message:Message,state:FSMContext):
    await message.answer("Familiya ismingni kirit")
    await state.set_state("name")

@dp.message_handler(state="name")
async def fullname(message:Message,state:FSMContext):
    ism=message.text
    await message.answer(f"{ism} telefon raqam kriting")
    await state.set_state("phone")

@dp.message_handler(state="phone")
async def phone(message:Message,state:FSMContext):
    tel=message.text
    await message.answer(f"seni telefoning {tel}")
    await state.finish()
