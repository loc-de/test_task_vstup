from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.utils import messages


# choose_currency_kb = ReplyKeyboardMarkup(
#     [
#         [KeyboardButton(text='')]
#     ]
# )

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=messages.MENU_BUTTON_TEXT)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


async def currencies_kb(currencies_list):
    kb = ReplyKeyboardBuilder()

    for currency in currencies_list:
        kb.add(KeyboardButton(text=currency))

    return kb.adjust(2).as_markup(input_field_placeholder="обери валюту..", one_time_keyboard=True)
