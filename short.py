from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import requests


from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("short", prefix) & filters.me)
async def shorten_link_command(client, message):
    try:

        await message.edit("Shorting...")
        if message.reply_to_message:
            link = message.reply_to_message.text
        else:
            try:
                link = message.command[1]
            except IndexError:
                return await message.delete()
        api_key = "985cc63aaf6d4ac5f0d06bcb2d9c1d5b7a379"
        url = link
        api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
        data = requests.get(api_url).json()["url"]
        if data["status"] == 7:
            shortened_url = data["shortLink"]
            await message.edit(f"Short URL: {shortened_url}")
    except Exception as err:
        print(err)

module_list['ShortURL'] = f'{prefix}short [Reply | link]'
file_list['ShortURL'] = 'short.py'
