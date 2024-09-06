from aiogram import Router

from bot.handlers.client import client_rt
from bot.handlers.startup import startup_rt


def register_routers() -> Router:
    root_rt = Router()
    root_rt.include_router(client_rt)
    root_rt.include_router(startup_rt)

    return root_rt
