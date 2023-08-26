from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_start_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text="Искать аниме")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder="Искать аниме")
