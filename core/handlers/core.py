import os

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile

from core.handlers.utils.utils import get_list_of_anime_by_name, get_anime_titles, get_anime_content_by_id, \
    ANILIBRIA_URL, get_anime_series_by_num
from core.keyboards.inline import get_anime_titles_keyboard, get_series_keyboard
from core.utils.callback_data import CallbackAnimeTitle, CallbackSeriesKeyboard
from core.utils.states import StepsAnime


async def get_search(message: Message, state: FSMContext):
    await message.answer(text="<b>Введите название аниме:</b>", parse_mode='HTML')
    await state.set_state(StepsAnime.ANIME_NAME)


async def get_found_anime(message: Message, state: FSMContext):
    anime_found = get_list_of_anime_by_name(user_input=message.text)
    anime_titles = get_anime_titles(anime_found)
    await message.answer(text="Вот что удалось найти:", reply_markup=get_anime_titles_keyboard(anime_titles))
    await state.clear()


async def get_anime(call: CallbackQuery, callback_data: CallbackAnimeTitle):
    content = get_anime_content_by_id(anime_id=callback_data.anime_id)
    anime_name = content['names']['ru']
    anime_description = content['description'].replace("\n\n\n", "\n").replace("\n\n", "\n")
    anime_genres = ", ".join(content['genres'])
    anime_series = content['player']['episodes']['string']

    anime_thumbnail = ANILIBRIA_URL + content['posters']['small']['url']

    caption_content = "\n".join([
        "<b>Жанр:</b> " + anime_genres,
        "<b>Название:</b> " + anime_name,
        "<b>Серии:</b> " + anime_series,
        "<b>Описание:</b> " + anime_description[:2000],
        "\n<b>Выберите серию:</b>"
    ])

    anime_id = content['id']
    start_pagination, end_pagination = map(int, anime_series.split("-"))
    current = start_pagination
    callback_data = CallbackSeriesKeyboard(anime_id=anime_id, current=current, start_pagination=start_pagination, end_pagination=end_pagination)

    await call.message.answer_photo(
        photo=anime_thumbnail,
        caption=caption_content,
        reply_markup=get_series_keyboard(callback_data),
        parse_mode='HTML')


async def get_anime_title(call: CallbackQuery, callback_data: CallbackSeriesKeyboard):
    await call.message.edit_reply_markup(reply_markup=get_series_keyboard(callback_data))


async def get_anime_series(call: CallbackQuery, callback_data: CallbackSeriesKeyboard):
    filepath = get_anime_series_by_num(
        anime_id=callback_data.anime_id, series_num=callback_data.series_num)
    file = FSInputFile(path=filepath)
    await call.message.answer_document(document=file)
    os.remove(filepath)
