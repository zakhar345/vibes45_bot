from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import register_handlers
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
