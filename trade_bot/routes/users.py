from .. import dp, types

@dp.callback_query_handler(lambda call: call.data == 'users')
async def on_press_users(call: types.CallbackQuery):
    await call.message.reply("You pressed users")
