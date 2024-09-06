from aiogram import Router


startup_rt = Router()


@startup_rt.startup()
async def startup():
    print('bot is running')
