from aiogram import Bot
from aiogram.types import Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import models
from core.message_texts import get_start_message, vlc_message, help_message, support_message


async def get_start(message: Message, bot: Bot, session: AsyncSession):
    user_data = models.UserData(
        id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        date_joined=message.date
    )

    existing_user = await session.execute(select(models.UserData).where(models.UserData.id == user_data.id))
    if existing_user.scalar() is None:
        # User doesn't exist, add them to the database
        session.add(user_data)

    await session.commit()
    await bot.send_message(chat_id=message.from_user.id, text=get_start_message, parse_mode='HTML')


async def get_help(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=help_message, parse_mode='HTML')


async def get_support(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=support_message, parse_mode='HTML')


async def get_vlc(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=vlc_message, parse_mode='HTML')

