from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="search",
            description="Поиск аниме."
        ),
        BotCommand(
            command="start",
            description="Как работает бот."
        ),
        BotCommand(
            command="help",
            description="Список доступных комманд."
        ),
        BotCommand(
            command="support",
            description="Узнай, как можно улучшить проект."
        ),
        BotCommand(
            command="vlc",
            description="Узнать больше про VLC-плеер."
        ),
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())

