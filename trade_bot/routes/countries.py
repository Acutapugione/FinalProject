from .. import dp, types
from db import Country, session
from sqlalchemy import select
from keyboards import countries_kb
from aiogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as kb


@dp.callback_query_handler(lambda call: call.data == "countries")
async def on_press_countries(call: types.CallbackQuery):
    await call.message.reply("You pressed countries", reply_markup=countries_kb)


@dp.callback_query_handler(lambda call: call.data == "countries/create")
async def country_create(call: types.CallbackQuery):
    await call.message.reply("You pressed create country")


@dp.callback_query_handler(lambda call: call.data == "countries/list")
async def country_list(call: types.CallbackQuery):
    await call.message.reply("You pressed list of countries", reply_markup=countries_kb)
    countries = select(Country)
    result = session.execute(countries)
    if result.first():
        markup = kb(
            inline_keyboard=[
                [btn(x.name, callback_data=f"countries/{x.id}") for x in result.all()],
            ]
        )
        await call.message.reply("select any country", reply_markup=markup)
    else:
        await call.message.reply("Countries is empty", reply_markup=countries_kb)
        
