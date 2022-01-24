from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
from datetime import datetime

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("time", prefix) & filters.me)
async def time(client: Client, message: Message):
    await message.edit(datetime.datetime.now().strftime('Date %d.%m.%Y\nTime %H:%M:%S'))

module_list['TimeNow'] = f'{prefix}time'
file_list['TimeNow'] = 'time_now.py'
