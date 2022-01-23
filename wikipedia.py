from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
import wikipedia

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("wiki", prefixes=prefix) & filters.me)
async def wiki(client: Client, message: Message):
    lang = message.command[1]
    user_request = " ".join(message.command[2:])
    await message.edit("<b>Search info</b>")
    if user_request == "":
        wikipedia.set_lang("en")
        user_request = " ".join(message.command[1:])
    try:
        if lang == "en":
            wikipedia.set_lang("en")

        result = wikipedia.summary(user_request)
        await message.edit(
            f"""<b>Слово:</b>
<code>{user_request}</code>

<b>Info:</b>
<code>{result}</code>"""
        )
    except Exception as exc:
        await message.edit(
            f"""<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>"""
        )

module_list['Example'] = f'{prefix}example_edit'
file_list['Example'] = 'example.py'
