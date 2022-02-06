from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import subprocess
import time
import asyncio

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("bomber", prefix) & filters.me)
async def b0mb3r(client, message):
    await message.edit("Starting dbomber")
    global bomber

    bomber = subprocess.Popen(["db0mb3r"], stdout=subprocess.PIPE)
    await asyncio.sleep(5)
    await message.edit("Bomber started![localhost]\nLink: 127.0.0.1:8080")


@Client.on_message(filters.command("sbomber", prefix) & filters.me)
async def sbomber(client, message):
    bomber.terminate()
    await message.edit("dbomber stopped!")


module_list['Db0mb3r'] = f'{prefix}bomber | {prefix}sbomber'
file_list['Db0mb3r'] = 'db0mb3r.py'
