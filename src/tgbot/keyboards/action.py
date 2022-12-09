from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

action_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить тайтл"),
            KeyboardButton(text="Удалить тайтл")
        ],
        [
            KeyboardButton(text="Список моих тайтлов"),
            KeyboardButton(text="Установить мьют")
        ]
    ],
    resize_keyboard=True
)


added_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Я добавил все что хотел!")
        ]
    ], resize_keyboard=True
)