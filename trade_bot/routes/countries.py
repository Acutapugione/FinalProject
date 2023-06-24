from .. import dp, types

@dp.callback_query_handler(lambda call: call.data == 'countries')
async def on_press_countries(call: types.CallbackQuery):
    await call.message.reply("You pressed countries")
    
