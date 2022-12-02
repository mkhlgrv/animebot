from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_action_keyboard = InlineKeyboardMarkup(row_width=2,
                                              inline_keyboard=[
                                               [
                                                   InlineKeyboardButton(text="Добавить тайтл", callback_data="add"),
                                                   InlineKeyboardButton(text="Удалить тайтл", callback_data="delete")
                                               ],
                                               [
                                                   InlineKeyboardButton(text="Поставить мьют", callback_data="mute"),
                                                   InlineKeyboardButton(text="Сделать донат", callback_data="donate")
                                               ]
                                              ])
