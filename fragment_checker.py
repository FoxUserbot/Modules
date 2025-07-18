from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix

from requirements_installer import install_library
install_library("bs4 requests -U") 

import requests
from bs4 import BeautifulSoup

@Client.on_message(filters.command("fcheck", prefixes=my_prefix()) & filters.me)
async def fcheck_handler(client, message):
    args = " ".join(message.command[1:]) if len(message.command) > 1 else ""
    if not args:
        await message.edit("<emoji id=5212926868012935693>❌</emoji> <b>Please specify username</b>")
        return

    response = requests.get(f"https://fragment.com/username/{args}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        elements = soup.select(".table-cell-value.tm-value.icon-before.icon-ton")
        if elements:
            text = elements[0].text.strip()
            await message.edit(f"<emoji id=5215219508670638513>💎</emoji> <b>Username Found!</b>\n<emoji id=5467626799556992380>✈️</emoji> <b>Username:</b> <code>{args}</code>\n<emoji id=5460720028288557729>🪙</emoji> <b>Cost:</b> <code>{text}</code> TON")
        else:
            await message.edit(f"<emoji id=5212926868012935693>❌</emoji> <b>Username <code>{args}</code> not found!</b>")

module_list['FragmentChecker'] = f'{my_prefix()}fcheck'
file_list['FragmentChecker'] = 'fragment_checker.py'