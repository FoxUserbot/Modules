from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix
from requirements_installer import install_library
from modules.plugins_1system.restarter import restart
import base64
import os
import shutil


install_library('openai requests')
from openai import AsyncOpenAI
import requests

async def create_module(module_text, module_name):
    prompt = (
        f"""
{requests.get("https://pastebin.com/raw/trkXmL5g").text}
{module_name}.py
И его код: 
```python
{module_text}
```
"""
    )
    
    client_ai  = AsyncOpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=str(base64.b64decode("c2stb3ItdjEtNjg1YzZiMDc2YjJhNDE4M2VkNTUzOWIyMTk3ZWY4MTk3YjkxYTE1ZDMxOTAxZjQ2YTQ5MTk0NTFjYzkxYzRmZQ==").decode('utf-8'))
            )
    response = await client_ai.chat.completions.create(
                model="deepseek/deepseek-chat-v3-0324:free",
                messages=[{"role": "user", "content": prompt}]
            )
    return response.choices[0].message.content.replace("```python", "").replace("```", "")






@Client.on_message(filters.command("wine_hikka", prefixes=my_prefix()) & filters.me)
async def wine_hikka(client, message):
    file_content = None
    module_name = None
    if message.reply_to_message and message.reply_to_message.document:
        await message.edit(f"🦊 | Loading module from reply...")
        file = await client.download_media(message.reply_to_message.document)
        with open(file, "r", encoding="utf-8") as f:
            file_content = f.read()
        os.remove(file)
        if os.path.exists("downloads"):
            shutil.rmtree("downloads")
        module_name = message.reply_to_message.document.file_name.replace(".py", "")
    elif len(message.command) > 1 and (message.command[1].startswith("http") or message.command[1].startswith("https")):
        url = message.command[1]
        await message.edit(f"🦊 | Loading module from URL: {url}")
        try:
            response = requests.get(url)
            if response.status_code != 200:
                await message.edit(f"🦊 | Error loading module from URL: {response.status_code}")
                return
            file_content = response.text
            module_name = url.split("/")[-1].replace(".py", "")
        except requests.exceptions.RequestException as e:
            await message.edit(f"🦊 | Error loading module from URL: {e}")
            return
    else:
        await message.edit("🦊 | Reply to a module file or provide a link!")
        return

    if file_content is None:
        await message.edit("🦊 | Failed to get module content.")
        return

    await message.edit(f"🦊 | Generating module...")
    answer = await create_module(file_content, module_name)
    file_path = f"modules/plugins_2custom/{module_name}.py"
    if answer is not None:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(answer)
        module_list[module_name] = f'{my_prefix()}{module_name}'
        file_list[module_name] = f'{module_name}.py'
        await message.edit(f"🦊 | Module generated at <code>{file_path}</code> \n <b>Restarting...</b>")
        await restart(message, restart_type="restart")
    else:
        await message.edit(f"🦊 | Error generating module :(")


module_list['WineHikka'] = f'{my_prefix()}wine_hikka'
file_list['WineHikka'] = 'wine_hikka.py'
