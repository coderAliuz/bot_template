from aiogram.types.reply_keyboard import ReplyKeyboardMarkup,ReplyKeyboardRemove

test_kb=ReplyKeyboardMarkup(
    [
      ["test2","test1"]
    ]
    ,resize_keyboard=True
)

kara_kb=ReplyKeyboardMarkup(
    [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"]
    ]
    ,resize_keyboard=True
)

del_kb=ReplyKeyboardRemove()