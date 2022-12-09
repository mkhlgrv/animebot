from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hcode
from aiogram.dispatcher.filters import IsReplyFilter, ChatTypeFilter, CommandHelp, CommandStart, Text

from tgbot.keyboards.action import added_keyboard
from tgbot.misc.throttling import rate_limit
from tgbot.states.action_states import ActionStates
from tgbot.data.data_users import data


@rate_limit(limit=5, key='action')
async def add_title_handler(message: types.Message):
    text = "Напиши мне тайтл который собираешься отслеживать"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await ActionStates.add_title.set()


@rate_limit(limit=2, key="adding")
async def added_title_handler(message: types.Message, state: FSMContext):
    data[0] = "smth"
    text = "Теперь буду отслеживать эту парашу"
    await message.reply(text=data[0], reply_markup=added_keyboard)


async def from_added_to_main(message: types.Message, state: FSMContext):
    text = "Окей все добавил"
    await message.reply(text=text, reply_markup=ReplyKeyboardRemove())
    await state.reset_state()




def register_user_actions(dp: Dispatcher):
    dp.register_message_handler(add_title_handler, Text("Добавить тайтл"))
    dp.register_message_handler(from_added_to_main, Text("Я добавил все что хотел!"), state=ActionStates.add_title)
    dp.register_message_handler(added_title_handler, state=ActionStates.add_title)

    # dp.register_message_handler(add_title_handler, Text("Добавить тайтл"))
    # dp.register_message_handler(added_title_handler, state=ActionStates.add_title)
    # dp.register_message_handler(add_title_handler, Text("Добавить тайтл"))
    # dp.register_message_handler(help_handler, commands=['help'])