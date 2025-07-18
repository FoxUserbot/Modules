from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix

from requirements_installer import install_library
install_library("requests -U") 

import requests


@Client.on_message(filters.command("neko", prefixes=my_prefix()) & filters.me)
async def neko(client, message):
    await message.edit("Neko tyan..~")
    try:
        resp = requests.get("https://nekos.best/api/v2/neko")
        data = resp.json()
        url = data["results"][0]["url"]
        await client.send_photo(message.chat.id, photo=str(url))
        await message.delete()
    except Exception as f:
        await message.edit(f"Oops..~\n{f}")


module_list['Neko'] = f'{my_prefix()}Neko'
file_list['Neko'] = 'neko.py'
