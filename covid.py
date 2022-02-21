from pyrogram import Client, filters
from covid import Covid
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("covid_en", prefixes=prefix) & filters.me)
async def covid_local(client, message):
    region = " ".join(message.command[1:])
    await message.edit("<code>Data retrieval...</code>")
    covid = Covid(source="worldometers")
    try:
        local_status = covid.get_status_by_country_name(region)
        await message.edit(
            "<b>=======🦠 COVID-19 STATUS 🦠=======</b>\n"
            + f"<b>Region</b>: <code>{local_status['country']}</code>\n"
            + "<b>====================================</b>\n"
            + f"<b>🤧 New cases</b>: <code>{local_status['new_cases']}</code>\n"
            + f"<b>😷 New deaths</b>: <code>{local_status['new_deaths']}</code>\n"
            + "<b>====================================</b>\n"
            + f"<b>😷 Сonfirmed</b>: <code>{local_status['confirmed']}</code>\n"
            + f"<b>❗️ Active:</b> <code>{local_status['active']}</code>\n"
            + f"<b>⚠️ Critical</b>: <code>{local_status['critical']}</code>\n"
            + f"<b>💀 Deaths</b>: <code>{local_status['deaths']}</code>\n"
            + f"<b>🚑 Recovered</b>: <code>{local_status['recovered']}</code>\n"
        )
    except ValueError:
        await message.edit(f'<code>There is no region called "{region}"</code>')


@Client.on_message(filters.command("covid_ru", prefixes=prefix) & filters.me)
async def covid_local(client, message):
    region = " ".join(message.command[1:])
    await message.edit("<code>Получение данных...</code>")
    covid = Covid(source="worldometers")
    try:
        local_status = covid.get_status_by_country_name(region)
        await message.edit(
            "<b>=====🦠 Статистика COVID-19 🦠=====</b>\n"
            + f"<b>Страна</b>: <code>{local_status['country']}</code>\n"
            + "<b>==================================</b>\n"
            + f"<b>🤧 Новые заражения</b>: <code>{local_status['new_cases']}</code>\n"
            + f"<b>😷 Новые смерти</b>: <code>{local_status['new_deaths']}</code>\n"
            + "<b>==================================</b>\n"
            + f"<b>😷 Подтвержденные</b>: <code>{local_status['confirmed']}</code>\n"
            + f"<b>❗️ Болеют:</b> <code>{local_status['active']}</code>\n"
            + f"<b>⚠️ В тяжелом состоянии</b>: <code>{local_status['critical']}</code>\n"
            + f"<b>💀 Всего смертей</b>: <code>{local_status['deaths']}</code>\n"
            + f"<b>🚑 Всего выздоровели</b>: <code>{local_status['recovered']}</code>\n"
        )
    except ValueError:
        await message.edit(f'<code>Нет такой страны с названием  "{region}"</code>')


module_list['StatisticsCovid19'] = f'{prefix}covid_[en|ru] [region]'
file_list['StatisticsCovid19'] = 'covid.py'
