from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix

import asyncio
bot_tag = "Zern0bot"

@Client.on_message(filters.command("eye", prefixes=my_prefix()) & filters.me)
async def spamban(client, message):
    number = message.command[1]
    await message.edit(f"⏳ | Проверяем аккаунт {number} на наличие данных. Это может занять некоторое время...")
    await client.unblock_user(bot_tag)
    await client.send_message(bot_tag, number)
    await asyncio.sleep(20)
    await message.edit("Вот что удалось найти:")
    async for iii in client.get_chat_history(bot_tag, limit=1):
        await client.forward_messages(message.chat.id, bot_tag, iii.id)


module_list['EyeGod'] = f'{my_prefix()}eye'
file_list['EyeGod'] = 'eye.py'
