from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix

import subprocess
import time
import asyncio

from requirements_installer import install_library
install_library("db0mb3r -U") 


@Client.on_message(filters.command("bomber", prefixes=my_prefix()) & filters.me)
async def b0mb3r(client, message):
    await message.edit("Starting dbomber")
    global bomber

    bomber = subprocess.Popen(["db0mb3r"], stdout=subprocess.PIPE)
    await asyncio.sleep(5)
    await message.edit("Bomber started![localhost]\nLink: 127.0.0.1:8080")


@Client.on_message(filters.command("sbomber", prefixes=my_prefix()) & filters.me)
async def sbomber(client, message):
    bomber.terminate()
    await message.edit("dbomber stopped!")


module_list['Db0mb3r'] = f'{my_prefix()}bomber | {my_prefix()}sbomber'
file_list['Db0mb3r'] = 'db0mb3r.py'