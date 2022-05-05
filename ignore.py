from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


i = []

def g():
    return i


@Client.on_message(filters.user(g()) & ~filters.me)
async def ignored(client, message):
    await message.delete()


@Client.on_message(filters.command("ignore", prefixes=prefix) & filters.me)
async def add_ignore(client, message):
    try:
        users = message.command[1]
    except:
        users = message.reply_to_message.from_user.id

    if users in i:
        i.remove(int(users))
        await message.edit(f"Ignor {str(users)} deactivated")
    else:
        i.append(int(users))
        await message.edit(f"Ignor {str(users)} activated")


module_list['IgnoreUser'] = f'{prefix}ignore [ID/Reply]'
file_list['IgnoreUser'] = 'ignore.py'
