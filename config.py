from aiogram import Dispatcher,Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token="token yozasizlar"
bot=Bot(token)
dp=Dispatcher(bot,storage=MemoryStorage())