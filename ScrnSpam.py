# meta developer: @sakura_modules
from asyncio import sleep
from telethon import functions, types
from .. import loader, utils

@loader.tds
class ScrnSpamMod(loader.Module):
    """Скрин спаммер"""

    strings = {
        "name": "ScrnSpam",
        "invalid_args": "<blockquote>⚠️ Укажите число. Пример: .scrn 5</blockquote>",
        "invalid_number": "<blockquote>⚠️ Укажите корректное положительное число</blockquote>",
    }

    async def scrncmd(self, message):
        """Отправка уведомлений о скриншотах. Использование: .scrn <число>"""
        args = utils.get_args(message)
        if not args:
            await utils.answer(message, self.strings["invalid_args"])
            return

        try:
            count = int(args[0])
            if count <= 0:
                raise ValueError
        except ValueError:
            await utils.answer(message, self.strings["invalid_number"])
            return

        chat_id = message.chat_id
        await message.delete()

        for _ in range(count):
            await message.client(functions.messages.SendScreenshotNotificationRequest(
                peer=message.to_id,
                reply_to=types.InputReplyToMessage(reply_to_msg_id=0)
            ))
            await sleep(0.5)
