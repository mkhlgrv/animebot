from aiogram.dispatcher.filters.state import StatesGroup, State


class ActionStates(StatesGroup):
    add_title = State()
    remove_title = State()
    watch_tittles = State()
    set_mute = State()

    