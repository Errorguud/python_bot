from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/start')
kb_client = ReplyKeyboardMarkup()
kb_client.add(b1)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(b1)

btnTopUp = InlineKeyboardButton(text="Пополнить", callback_data="top_up")
topUpMenu = InlineKeyboardMarkup(row_width=1)
topUpMenu.insert(btnTopUp)


def buy_menu(isUrl=True, url="", bill=""):
    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if isUrl:
        btnUrlQIWI = InlineKeyboardButton(text="Ссылка на оплату", url=url)
        qiwiMenu.insert(btnUrlQIWI)

    btnCheckQIWI = InlineKeyboardButton(text="Проверить оплату", callback_data="check_" + bill)
    qiwiMenu.insert(btnCheckQIWI)
    return qiwiMenu
