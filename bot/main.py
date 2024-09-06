from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

import asyncio
from config import TOKEN
from utils.routers import register_routers

# from utils.parser import currency_parser


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dp.include_router(register_routers())


async def main():
    # await currency_parser.init_session()

    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
