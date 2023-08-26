from aiogram import Bot
from aiogram.types import Message

from core.message_texts import get_start_message, vlc_message, help_message, support_message
from core.utils.db import Request


async def get_start(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.username)
    await bot.send_message(chat_id=message.from_user.id, text=get_start_message, parse_mode='HTML')


async def get_help(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=help_message, parse_mode='HTML')


async def get_support(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=support_message, parse_mode='HTML')


async def get_vlc(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=vlc_message, parse_mode='HTML')

