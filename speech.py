from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
from gtts import gTTS
import os

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("voice", prefix) & filters.me)
async def voice(client: Client, message: Message):
    lang_code = os.environ.get("lang_code", "en")
    cust_lang = None
    await message.delete()
    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang=lang_code)
    tts.save("temp/voice.mp3")
    if message.reply_to_message:
        await client.send_voice(
            message.chat.id,
            voice="temp/voice.mp3",
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await client.send_voice(message.chat.id, voice="temp/voice.mp3")
    os.remove("temp/voice.mp3")

module_list['TextToVoice'] = f'{prefix}voice [Text]'
file_list['TextToVoice'] = 'speech.py'
