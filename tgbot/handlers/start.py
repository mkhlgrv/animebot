from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from aiogram.dispatcher.filters import IsReplyFilter, ChatTypeFilter, CommandStart, CommandHelp
from tgbot.misc.throttling import rate_limit


@rate_limit(limit=10, key='start')
async def start_handler(message: types.Message):
    text = "Здарова епта, все работает"
    await message.answer(text)


@rate_limit(limit=10, key='start')
async def help_handler(message: types.Message):
    text = "Себе помоги"
    await message.answer(text)


def register_start(dp: Dispatcher):
    dp.register_message_handler(start_handler, CommandStart())
    dp.register_message_handler(help_handler, commands=['help'])
