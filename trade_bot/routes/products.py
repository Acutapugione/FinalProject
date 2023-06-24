from .. import dp, types

@dp.callback_query_handler(lambda call: call.data == 'products')
async def on_press_products(call: types.CallbackQuery):
    await call.message.reply("You pressed products")
