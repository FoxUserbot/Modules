from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import asyncio

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("eye", prefixes=prefix) & filters.me)
async def eye(client, message):
    await client.unblock_user("AnonymousEUEBot")
    number = message.command[1]
    await message.edit(f"⏳ | Проверяем аккаунт {number} на наличие данных. Это может занять некоторое время...")
    await client.send_message("AnonymousEUEBot", number)
    await asyncio.sleep(20)
    iii = await client.get_chat_history("AnonymousEUEBot")
    await message.edit("Вот что удалось найти:")
    await client.forward_messages(message.chat.id, "AnonymousEUEBot", iii[0].id)


module_list['EyeOfGod'] = f'{prefix}eye'
file_list['EyeOfGod'] = 'eye.py'
