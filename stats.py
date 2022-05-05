from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from datetime import datetime
import asyncio

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command(["stat", "stats"], prefixes=prefix) & filters.me)
async def stats(client, message):
    await message.edit(message, "Parsing stats...")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    group = ["supergroup", "group"]
    iter_dialog = client.iter_dialogs()
    async for dialog in iter_dialog:
        if dialog.chat.type == "private":
            u += 1
        elif dialog.chat.type == "bot":
            b += 1
        elif dialog.chat.type == "group":
            g += 1
        elif dialog.chat.type == "supergroup":
            sg += 1
            user_s = await dialog.chat.get_member(int(client.me.id))
            if user_s.status in ("creator", "administrator"):
                a_chat += 1
        elif dialog.chat.type == "channel":
            c += 1
    end = datetime.now()
    ms = (end - start).seconds

    private_chat = f"**Privates:** {u}\n"
    group_chat = f"**Groups:** {g}\n"
    supergroup_chat = f"**Supergroups:** {sg}\n"
    channel_chat = f"**Channels:** {c}\n"
    bot_chat = f"**Bots:** {b}\n"
    owner_chat = f"**Creators:** {a_chat}"
    statistic = private_chat + group_chat + supergroup_chat + channel_chat + bot_chat + owner_chat
    await message.edit(f"You stats:\n{statistic}\nParsed {ms} seconds")


module_list['Statistic'] = f'{prefix}stats'
file_list['Statistic'] = 'stats.py'
