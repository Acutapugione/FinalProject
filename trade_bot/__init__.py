import logging

from aiogram import Bot, Dispatcher, executor, types
from .vendor import Settings
from keyboards import menu_kb

API_TOKEN = 'BOT TOKEN HERE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=Settings.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome", reply_markup=menu_kb)

from .routes import *

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)