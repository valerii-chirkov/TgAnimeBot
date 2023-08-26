from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext


class CallbackAnimeSeries(CallbackData, prefix='anime'):
    anime_id: int
    series_num: str


class CallbackAnimeTitle(CallbackData, prefix='anime_title'):
    anime_id: int


class CallbackSeriesKeyboard(CallbackData, prefix='series'):
    anime_id: int
    current: int
    start_pagination: int
    end_pagination: int


class CallbackAnimeTitleSearch(CallbackData, prefix='search'):
    name: str
