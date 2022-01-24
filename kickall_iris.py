import asyncio
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix

prefix = my_prefix()


@Client.on_message(filters.command("iris_kickall", prefixes=prefix) & filters.me)
async def tagall(client, message):
    await message.delete()
    chat_id = message.chat.id
    string = ""
    limit = 1
    icm = client.iter_chat_members(chat_id)
    async for member in icm:
        string = f"бан {member.user.mention}\n"
        await client.send_message(chat_id, text=string)
        await asyncio.sleep(2)


module_list['Kickall(iris)'] = f'{prefix}iris_kickall'
file_list['Kickall(iris)'] = 'kickall_iris.py'
