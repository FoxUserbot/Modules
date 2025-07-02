from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix
from requirements_installer import install_library
from modules.plugins_1system.restarter import restart
import base64
import os
import shutil
import requests

install_library('openai')
from openai import AsyncOpenAI

async def create_module(module_text):
    promt = """
Ты — разработчик модулей под FoxUserBot. Твоя задача — **переписать модуль с Hikka (на Telethon)** на **FoxUserBot (на Pyrogram)**.

🔧 Основные правила:
- Отвечай __ТОЛЬКО КОДОМ__, без комментариев, Markdown, кавычек или пояснений.
- Используй только Pyrogram. **НЕЛЬЗЯ** использовать методы и синтаксис Telethon (`.conversation`, `.event`, `.respond`, `.pattern`, `await event.edit()`, и т.п.).
- Все команды должны быть реализованы через `@Client.on_message(...)` и `filters.command(..., prefixes=my_prefix()) & filters.me`.
- В конце обязательно добавляй строки для `module_list[...]` и `file_list[...]`.

📥 Для сторонних библиотек (если нужно) используй:
from requirements_installer import install_library  
install_library("название_библиотеки")

💡 Внимание: В Pyrogram для кастомных эмодзи в тексте используйте атрибут id, а не document_id.
Пример:
<emoji id=5326015457155620929></emoji>
Вместо:
<emoji document_id=5326015457155620929></emoji>

📦 Предустановленные библиотеки (НЕ нужно устанавливать):
- wheel
- telegraph
- requests
- wget
- pystyle
- wikipedia
- gTTS
- kurigram
- lyricsgenius

🔁 Работа с async-генераторами:
- Методы вроде `search_messages`, `get_chat_history`, `get_chat_members` — это async-генераторы.
- Используй их через `async for`, **БЕЗ `await` перед ними**.

✅ Пример:
async for msg in client.get_chat_history("spambot", limit=1):  
    await message.edit(msg.text)

🚫 **Запрещено:**
- НЕЛЬЗЯ использовать `await client.get_chat_history(...)` — вызовет ошибку.
- НЕЛЬЗЯ создавать хендлеры (`@Client.on_message(...)`) внутри других функций. Это не работает в Pyrogram.
- НЕЛЬЗЯ использовать `client.remove_handler(...)`, `conversation`, или `await conv.send_message(...)`.
⚠️ Для ожидания ответа от бота, вместо Telethon-style `.conversation`, используй `client.listen()` с фильтром по ID бота и таймаутом.  



📦 Пример корректного Pyrogram-модуля:
from pyrogram import Client, filters  
from modules.plugins_1system.settings.main_settings import module_list, file_list  
from prefix import my_prefix  

@Client.on_message(filters.command("spamban", prefixes=my_prefix()) & filters.me)  
async def spamban(client, message):  
    await message.edit("Checking your account for Spamban...")  
    await client.unblock_user("spambot")  
    await client.send_message("spambot", "/start")  
    async for msg in client.get_chat_history("spambot", limit=1):  
        await message.edit(msg.text)  

module_list["SpamBan"] = f"{my_prefix()}spamban"  
file_list["SpamBan"] = "spamban.py"

==================

Вот модуль, который нужно переписать:

""" + module_text




    client_ai  = AsyncOpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=str(base64.b64decode("c2stb3ItdjEtNjg1YzZiMDc2YjJhNDE4M2VkNTUzOWIyMTk3ZWY4MTk3YjkxYTE1ZDMxOTAxZjQ2YTQ5MTk0NTFjYzkxYzRmZQ==").decode('utf-8'))
            )
    response = await client_ai.chat.completions.create(
                model="deepseek/deepseek-chat:free",
                messages=[{"role": "user", "content": promt}]
            )
    return response.choices[0].message.content






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
    elif len(message.command) > 1 and message.command[1].startswith("http"):
        url = message.command[1]
        await message.edit(f"🦊 | Loading module from URL: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status() 
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
    answer = await create_module(file_content)
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


module_list['Wine Hikka'] = f'{my_prefix()}wine_hikka'
file_list['Wine Hikka'] = 'wine_hikka.py'
