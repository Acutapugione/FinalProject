from .. import dp, types

@dp.callback_query_handler(lambda call: call.data == 'start')
async def on_press_start(call: types.CallbackQuery):
    await call.message.reply("You pressed start")
