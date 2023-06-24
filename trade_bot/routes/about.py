from .. import dp, types

@dp.callback_query_handler(lambda call: call.data == 'about')
async def on_press_about(call: types.CallbackQuery):
    await call.message.reply("You pressed about")
