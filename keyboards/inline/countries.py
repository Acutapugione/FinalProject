from aiogram.types import (
    InlineKeyboardMarkup as kb,
    InlineKeyboardButton as btn,
)

menu_btns = [
    [
        btn("Create", callback_data="countries/create"),
        btn("List", callback_data="countries/list"),
    ],
]
menu_kb = kb(inline_keyboard=menu_btns)
