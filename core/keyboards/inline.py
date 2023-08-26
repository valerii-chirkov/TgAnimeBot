from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.utils.callback_data import CallbackAnimeSeries, CallbackSeriesKeyboard, CallbackAnimeTitle


def get_anime_titles_keyboard(anime_titles: list[tuple]) -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    for title, title_id in anime_titles:
        keyboard_builder.button(text=title, callback_data=CallbackAnimeTitle(anime_id=title_id))
    keyboard_builder.adjust(*[1 for _ in range(len(anime_titles))])  # TODO find a proper way to make it in a stack
    return keyboard_builder.as_markup()


def get_series_keyboard(callback_data):
    max_buttons = 7
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.adjust(max_buttons)

    anime_id = callback_data.anime_id
    st_p = callback_data.start_pagination
    end_p = callback_data.end_pagination
    current = callback_data.current

    def nav_button(text: str, cur: int) -> None:
        keyboard_builder.button(
            text=text,
            callback_data=CallbackSeriesKeyboard(
                anime_id=anime_id, current=cur, start_pagination=st_p, end_pagination=end_p
            )
        )

    def anime_button(page=0):
        cd = CallbackAnimeSeries(anime_id=anime_id, series_num=str(page))
        keyboard_builder.button(text=str(page), callback_data=cd)

    if end_p-st_p <= max_buttons:
        [anime_button(page) for page in range(st_p, end_p+1)]

    elif st_p <= current <= st_p+max_buttons-2:
        [anime_button(page) for page in range(st_p, st_p+max_buttons-1)]
        nav_button(text=">>", cur=current+6)

    elif end_p-max_buttons+2 <= current <= end_p:
        nav_button(text="<<", cur=current-5)
        [anime_button(page) for page in range(end_p-max_buttons+2, end_p+1)]

    else:
        nav_button(text="<<", cur=current-5)
        [anime_button(page) for page in range(current, current+max_buttons-2)]
        nav_button(text=">>", cur=current+5)

    return keyboard_builder.as_markup()


