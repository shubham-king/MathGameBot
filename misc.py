from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import logging
import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)
TOKEN = config.TOKEN
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)