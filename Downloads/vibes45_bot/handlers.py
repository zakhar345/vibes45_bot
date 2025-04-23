from aiogram import types, Dispatcher

async def start(message: types.Message):
    await message.reply('Привет! Я работаю!')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
