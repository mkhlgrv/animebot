from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from aiogram.dispatcher.filters import IsReplyFilter, ChatTypeFilter, CommandHelp, CommandStart, Command

from tgbot.keyboards.action import action_keyboard

from tgbot.keyboards.inline.user_actions_keyboard import inline_action_keyboard
from tgbot.misc.throttling import rate_limit


@rate_limit(limit=10, key='start')
async def start_handler(message: types.Message):
    text = "Здарова епта, все работает"
    await message.answer(text=text, reply_markup=action_keyboard)


@rate_limit(limit=10, key='start')
async def inline_action_handler(message: types.Message):
    text = "Здарова епта, все работает"
    await message.answer(text=text, reply_markup=inline_action_keyboard)


# async def inline_action_handler(messege:types.Message):
#     await messege.answer(text="Выбирите действие", reply_markup=inline_action_keyboard)


def register_start(dp: Dispatcher):
    dp.register_message_handler(start_handler, CommandStart())
    dp.register_message_handler(inline_action_handler, Command("inline"))
