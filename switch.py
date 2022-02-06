from pyrogram import Client, filters

from plugins.settings.main_settings import module_list, file_list
import asyncio
import time

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("sw", prefix) & filters.me)
async def switch(client, message):
    text = " ".join(message.command[1:])
    ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    en_keys = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
    if text == "":
        if message.reply_to_message:
            reply_text = message.reply_to_message.text
            change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
            reply_text = str.translate(reply_text, change)
            await message.edit(reply_text)
        else:
            await message.edit("Text not found")
            await asyncio.sleep(3)
            await message.delete()
    else:
        change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
        text = str.translate(text, change)
        await message.edit(text)


module_list['Switch'] = f'{prefix}sw [Reply | text]'
file_list['Switch'] = 'switch.py'
