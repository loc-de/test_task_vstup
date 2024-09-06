from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.utils import messages
from bot.utils.parser import currency_parser
from bot.keyboards.client_kbs import currencies_kb, menu_kb


client_rt = Router()


@client_rt.message(CommandStart())
@client_rt.message(F.text == messages.MENU_BUTTON_TEXT)
async def start(message: Message):
    currencies_list = await currency_parser.get_currency_list()

    await message.answer(
        text=messages.START_TEXT,
        reply_markup=await currencies_kb(currencies_list)
    )


@client_rt.message(F.text)
async def currency_rate(message: Message):
    currency = message.text
    currencies_list = await currency_parser.get_currency_list()

    if currency not in currencies_list:
        return await message.answer(
            text=messages.RATE_NOT_FOUND_TEXT,
            reply_markup=menu_kb
        )

    rate = await currency_parser.get_currency_rate(currency)

    await message.answer(
        text=messages.CURRENCY_RATE_TEXT.format(currency=currency, rate=rate),
        reply_markup=menu_kb
    )
