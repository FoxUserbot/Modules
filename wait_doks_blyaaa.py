from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list

from prefix import my_prefix


@Client.on_message(filters.command("wait", prefixes=my_prefix()) & filters.me)
async def wait_command(client, message):
    video_url = "https://0x0.st/X9S-.mp4"
    if message.reply_to_message:
        id_m = message.reply_to_message.id
    else:
        id_m = message.id
    try:
        await message.delete()
        await client.send_video(
        chat_id=message.chat.id,
        video=video_url,
        reply_to_message_id=id_m)
    except Exception as e:
        message.reply(f"Error | {e}")

module_list['WaitDoksBlyaaa'] = f'{my_prefix()}wait'
file_list['WaitDoksBlyaaa'] = 'wait_doks_blyaaa.py'
