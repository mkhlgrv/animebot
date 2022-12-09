import asyncio
from typing import Union
from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.utils.exceptions import Throttled


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix="antiflood_"):
        self.limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def throttling(self, target: Union[types.Message, types.CallbackQuery]):
        handler = current_handler.get()
        if not handler:
            return

        dp = Dispatcher.get_current()

        limit = getattr(handler, "throttling_rate_limit", self.limit)
        key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")

        try:
            await dp.throttle(key, rate=limit)
        except Throttled as t:
            await self.target_throttled(target, t, dp, key)
            raise CancelHandler()

    @staticmethod
    async def target_throttled(target: Union[types.Message, types.CallbackQuery],
                               throttled: Throttled, dispatcher: Dispatcher, key: str):
        msg = target.message if isinstance(target, types.CallbackQuery) else target

        delta = throttled.rate - throttled.delta
        if throttled.exceeded_count == 2:
            text = "Slow down or u will be banned!!!"
            await msg.answer(text)
            return

        if throttled.exceeded_count == 3:
            text = f"You're banned for a {delta} sec"
            await msg.answer(text)
            return
        await asyncio.sleep(delta)
        await msg.answer("Теперь пиши")

        thr = await dispatcher.check_key(key)
        if thr.exceeded_count == throttled.exceeded_count:
            await msg.answer("U can continue")

    async def on_process_message(self, message, data):
        await self.throttling(message)

    async def on_process_callback_query(self, call, data):
        await self.throttling(call)


