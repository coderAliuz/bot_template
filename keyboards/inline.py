from aiogram.types.inline_keyboard import InlineKeyboardButton,InlineKeyboardMarkup

test_in_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Test1",callback_data="Alisher")],
        [InlineKeyboardButton(text="Test2",callback_data="Bekmurod"),
         InlineKeyboardButton(text="link",url="https://t.me/+Jj3lWOWQoGs1Y2Ri")
         ],
        [InlineKeyboardButton(text="Tasodif",callback_data="random")]
    ]
)

def raqam_kb():
    tugmalar=[]
    for i in range(1,10):
        tugmalar.append(InlineKeyboardButton(text=f"{i}",callback_data=f"raqam_{i}"))
    kb=InlineKeyboardMarkup(row_width=3)
    kb.add(*tugmalar)
    return kb


edit_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Xabar yuborish",callback_data="message"),
         InlineKeyboardButton(text="O'zgartirish",callback_data="edit"),
         InlineKeyboardButton(text="Ochirish",callback_data="delete")],
        [InlineKeyboardButton(text="Keyingi",callback_data="next")]
    ]
)

back_in_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ortga",callback_data="back")]
    ]
)