from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.states.exchange_states import CurrencyExchange

from bot.utils import messages
from bot.utils.parser import currency_parser
from bot.keyboards.client_kbs import currencies_kb


start_rt = Router()


@start_rt.message(CommandStart())
@start_rt.message(F.text == messages.MENU_BUTTON_TEXT)
async def start(message: Message, state: FSMContext):
    await state.set_state(CurrencyExchange.currency)

    currencies_list = await currency_parser.get_currencies_list()

    await message.answer(
        text=messages.START_TEXT,
        reply_markup=await currencies_kb(currencies_list)
    )
