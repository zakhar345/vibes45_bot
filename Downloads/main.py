import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
scheduler = AsyncIOScheduler()

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Привет! Это бот 45 Vibes. Отправь свой мем, историю или признание.")

@dp.message_handler(content_types=['text', 'photo'])
async def post_handler(message: types.Message):
    await message.answer("Спасибо! Мы отправим твое сообщение на модерацию.")

if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
