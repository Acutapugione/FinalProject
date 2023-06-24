from aiogram.types import (
    InlineKeyboardMarkup as kb,
    InlineKeyboardButton as btn,
)

menu_btns = [
    [
        btn("Start", callback_data="start"),
        btn("About", callback_data="about"),
    ],
    [
        btn("Products", callback_data="products"),
        btn("Countries", callback_data="countries"),
        btn("Users", callback_data="users"),
    ],
]
menu_kb = kb(inline_keyboard=menu_btns)
print(menu_kb)