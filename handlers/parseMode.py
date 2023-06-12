from aiogram.types import Message
from config import dp

@dp.message_handler(commands="bold",state="*")
async def bold_text(message:Message):
    await message.reply("Manabu <b>xabar qalin yozilgan</b>")

@dp.message_handler(commands="italic",state="*")
async def italic_text(message:Message):
    await message.reply("Manabu <i> xabar qiyshiq yozilgan </i>")

@dp.message_handler(commands="copy",state="*")
async def copy_text(message:Message):
    await message.reply("Nusxalash :<code>Meni ustimga bos nusxalanaman</code>")


@dp.message_handler(commands="spoiler",state="*")
async def spoiler_text(message:Message):
    await message.reply("Yashirin xabar <tg-spoiler>Men agentman</tg-spoiler>")

@dp.message_handler(commands="all",state="*")
async def all_text(message:Message):
    await message.reply("<b>Mening ismim <code>Alisher</code> <tg-spoiler><i>007</i></tg-spoiler></b>")


@dp.message_handler(commands="url",state="*")
async def url(message:Message):
    await message.answer("Bizning manzil <a href='t.me//coder_ali'>shu joyda</a>")
