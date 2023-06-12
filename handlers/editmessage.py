from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from config import dp,bot
from keyboards import edit_kb,back_in_kb
import asyncio
@dp.message_handler(commands="edit",state="*")
async def edit_mess(alisher:Message,state:FSMContext):
    await alisher.answer("Menga xabar yubor men uni o'zgartiraman")
    await state.set_state("edit")

@dp.message_handler(state="edit")
async def edit_text(message:Message):
    await bot.send_message(text="BU birinchi xabar",chat_id=message.chat.id)
    await asyncio.sleep(2)
    await bot.edit_message_text("Xabar o'zgartitrildi",chat_id=message.chat.id,message_id=message.message_id+1)
    # await message.edit_text("Xabar o'zgartitrildi")
    await asyncio.sleep(2)
    await bot.delete_message(chat_id=message.chat.id,message_id=message.message_id+1)
    # await message.delete()


@dp.message_handler(commands="inline",state="*")
async def inline_mess(message:Message,state:FSMContext):
    await message.answer("Quyidagi tugmalarni tekshirib ko'r",reply_markup=edit_kb)
    await state.set_state("inline_state")

@dp.callback_query_handler(state="inline_state",text="message")
async def inline_send_message(call:CallbackQuery):
    await call.message.answer("Sen xabar yubirosh tugmasini bosding.Xabar yuborildi")

@dp.callback_query_handler(state="inline_state",text="edit")
async def inline_edit_message(call:CallbackQuery):
    data=call.data
    await call.message.edit_text(f"Xabar o'zgaritirildi {data}")

@dp.callback_query_handler(state="inline_state",text="delete")
async def inline_delete_message(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Xabar o'chirildi")

@dp.callback_query_handler(state="inline_state",text="next")
async def inline_next_message(call:CallbackQuery,state:FSMContext):
    await call.message.edit_text("Siz boshqa bo'limga o'tdingiz",reply_markup=back_in_kb)
    await state.set_state("next_state")

@dp.callback_query_handler(state="next_state",text="back")
async def back_message(call:CallbackQuery,state:FSMContext):
    await call.message.edit_text("Quyidagi tugmalarni tekshirib ko'r",reply_markup=edit_kb)
    await state.set_state("inline_state")