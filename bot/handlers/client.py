from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.states.exchange_states import CurrencyExchange

from bot.utils import messages
from bot.utils.validators import is_valid_amount
from bot.utils.parser import currency_parser
from bot.keyboards.client_kbs import currencies_kb, menu_kb


client_rt = Router()


@client_rt.message(CommandStart())
@client_rt.message(F.text == messages.MENU_BUTTON_TEXT)
async def start(message: Message, state: FSMContext):
    await state.set_state(CurrencyExchange.currency)

    currencies_list = await currency_parser.get_currencies_list()

    await message.answer(
        text=messages.START_TEXT,
        reply_markup=await currencies_kb(currencies_list)
    )


@client_rt.message(CurrencyExchange.currency)
async def enter_amount(message: Message, state: FSMContext):
    currency = message.text
    currencies_list = await currency_parser.get_currencies_list()

    if currency not in currencies_list:
        await state.clear()

        return await message.answer(
            text=messages.CURRENCY_NOT_FOUND_TEXT.format(currency=currency),
            reply_markup=menu_kb
        )

    await state.update_data(currency=message.text)
    await state.set_state(CurrencyExchange.amount)

    rate = await currency_parser.get_rate(currency)

    await message.answer(
        text=messages.ENTER_AMOUNT_TEXT.format(currency=currency, rate=rate),
        reply_markup=menu_kb
    )


@client_rt.message(CurrencyExchange.amount)
async def exchange_rate(message: Message, state: FSMContext):
    amount = message.text.strip().replace(',', '.')

    if not is_valid_amount(amount) or float(amount) < 0:
        await state.set_state(CurrencyExchange.amount)

        return await message.answer(
            text=messages.INVALID_AMOUNT_TEXT,
            reply_markup=menu_kb
        )

    await state.update_data(amount=float(amount))
    data = await state.get_data()
    await state.clear()

    rate = await currency_parser.get_rate(data['currency'])

    await message.answer(
        text=messages.EXCHANGE_RATE_TEXT.format(
            amount=data['amount'],
            currency=data['currency'],
            converted_amount=data['amount'] / rate,
            rate=rate
        ),
        reply_markup=menu_kb
    )
