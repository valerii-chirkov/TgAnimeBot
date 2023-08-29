import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import asyncio

from core.config import TOKEN, ADMIN_ID
from core.handlers.basic import get_start, get_vlc, get_help, get_support
from core.handlers.core import get_search, get_anime, get_found_anime, get_anime_title, get_anime_series
from core.message_texts import *
from core.middlewares.db_middleware import DbSessionMiddleware
from core.utils.callback_data import CallbackAnimeSeries, CallbackAnimeTitle, CallbackSeriesKeyboard
from core.utils.commands import set_commands
from core.db.database import SessionLocal, init_models
from core.utils.states import StepsAnime


async def start_bot(bot: Bot):
    await set_commands(bot=bot)
    await bot.send_message(chat_id=ADMIN_ID, text=start_bot_message)


async def stop_bot(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID, text=stop_bot_message)


async def start():
    logging.basicConfig(filename="logs/anime_logs",
                        filemode='a',
                        level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    await init_models()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.update.middleware(DbSessionMiddleware(session_pool=SessionLocal))

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=["start", "run"]))
    dp.message.register(get_help, Command(commands=["help"]))
    dp.message.register(get_support, Command(commands=["support"]))
    dp.message.register(get_vlc, Command(commands=["vlc"]))

    dp.message.register(get_search, Command(commands=["search"]))
    dp.message.register(get_found_anime, StepsAnime.ANIME_NAME)

    dp.callback_query.register(get_anime, CallbackAnimeTitle.filter())
    dp.callback_query.register(get_anime_title, CallbackSeriesKeyboard.filter())
    dp.callback_query.register(get_anime_series, CallbackAnimeSeries.filter())

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

