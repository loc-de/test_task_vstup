from aiogram.fsm.state import StatesGroup, State


class CurrencyExchange(StatesGroup):
    currency = State()
    amount = State()
