from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import asyncio
import random

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("hack", prefix) & filters.me)
async def hack(client, message):
    perc = 0
    while perc < 100:
        text = "👮 Взлом пентагона в процессе ..." + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 3)
        await asyncio.sleep(0.1)
    text = "✅ Пентагон успешно взломан!"
    await message.edit(str(text))
    await asyncio.sleep(3)
    perc = 0
    while perc < 100:
        text = "⬇️ Скачивание данных ..." + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 5)
        await asyncio.sleep(0.15)
    await asyncio.sleep(1)
    text = "🐓Нашли файлы что ты петух!"
    await message.edit(text)


@Client.on_message(filters.command("jopa", prefix) & filters.me)
async def jopa(client, message):
    perc = 0
    while perc < 100:
        text = "🍑 Взлом жопы в процессе ..." + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 3)
        await asyncio.sleep(0.1)
    text = "✅ Жопа взломана"
    await message.edit(str(text))
    await asyncio.sleep(3)
    text = "🔍 Поиск Сливов ..."
    await message.edit(str(text))
    perc = 0
    await asyncio.sleep(3)
    while perc < 100:
        text = "⬇️ Скачивание сливов ..." + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 4)
        await asyncio.sleep(0.15)
    text = "✅ Сливы были найдены"
    await message.edit(str(text))
    perc = 0
    await asyncio.sleep(5)
    while perc < 100:
        text = "⬆️ Продажа сливов барыге..." + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 5)
        await asyncio.sleep(0.15)
    text = "✅ Проданно"
    await message.edit(str(text))
    await asyncio.sleep(2)
    rand = random.randint(100, 5000)
    bal = rand
    text = "💸 Вы заработали " + str(bal) + " ₽"
    await message.edit(text)


@Client.on_message(filters.command("drugs", prefix) & filters.me)
async def drugs(client, message):
    perc = 0
    result = 0
    while perc < 100:
        text = "🍁Поиск запрещённых препаратов " + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 3)
        await asyncio.sleep(0.1)
    text = "Найдено 3 кг шпекса🍪💨"
    await message.edit(str(text))
    await asyncio.sleep(3)
    text = "Оформляем вкид 🌿⚗️"
    await message.edit(str(text))
    await asyncio.sleep(5)
    drugsss = ['🔥😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты 😳🔥',
               '🥴Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид🥴',
               '😖Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз😖',
               '😌Вы оформили вкид, Вам понравилось)😌']
    drug = random.choice(drugsss)
    await message.edit(drug)


@Client.on_message(filters.command("mum", prefix) & filters.me)
async def mum(client, message):
    text = "🔍 Поиск твоей мамки начался..."
    await message.edit(str(text))
    await asyncio.sleep(3.0)
    perc = 0
    while perc < 100:
        text = "🔍 Ищем твою мамашу на Авито... " + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 3)
        await asyncio.sleep(0.75)
    text = "❌ Мамаша не найденна"
    await message.edit(str(text))
    await asyncio.sleep(3.0)
    perc = 0
    while perc < 100:
        text = "🔍 Поиск твоей мамаши на свалке... " + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 5)
        await asyncio.sleep(0.75)
    text = "❌ Мамаша не найденна"
    await message.edit(str(text))

    perc = 0
    while perc < 100:
        text = "🔍 Поиск твоей мамки в канаве... " + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 5)
        await asyncio.sleep(0.75)
    text = "✅ Мамка найдена... Она в канаве"
    await message.edit(str(text))


@Client.on_message(filters.command("policya", prefix) & filters.me)
async def policya(client, message):
    red_blue = "🔴🔴🔴⬜⬜⬜🔵🔵🔵"
    blue_red = "🔵🔵🔵⬜⬜⬜🔴🔴🔴"
    duration = 0
    try:
        need_duration = int(message.command[1])
    except:
        need_duration = 3
    while need_duration != duration:
        await message.edit(f"{red_blue}\n" * 3)
        await asyncio.sleep(0.4)
        await message.edit(f"{blue_red}\n" * 3)
        await asyncio.sleep(0.4)
        duration += 1
    await message.edit("**Никому ни с места!**\nПрибыла **🚨 Полиция 🚨**...\nГотовь вещички, **сынок**.")


@Client.on_message(filters.command("loveyou", prefix) & filters.me)
async def loveyou(client, message):
    numbers = 4
    hearth = """
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🖤🖤🤍🖤🖤🤍🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
"""

    await message.edit(("🤍" * 9 + "\n") * 9)
    await asyncio.sleep(0.5)

    redhearth = hearth.replace("🖤", "❤️")
    await message.edit(redhearth)
    list_color = ["🧡", "💛", "💚", "💙", "💜", "❤️"]
    for returns in range(3):
        for i in list_color:
            await message.edit(hearth.replace("🖤", i))
    try:
        while True:
            numbers += 2
            Str = redhearth
            l = len(Str)
            await message.edit(Str[:l - numbers])
            await asyncio.sleep(0.01)
    except Exception as f:
        print(f)
    await message.edit("🤍 🪄🪄🪄")
    await asyncio.sleep(1)
    await message.edit("❤️ 🪄🪄🪄")
    await asyncio.sleep(0.4)
    await message.edit("❤️ I")
    await asyncio.sleep(0.4)
    await message.edit("❤️ I love")
    await asyncio.sleep(0.4)
    await message.edit("❤️ I love you")
    await asyncio.sleep(1)
    await message.edit("❤️ I love you <3")



# Переменные с кастомом
end_message = 'l l let me die'
messages_per_second = 7
sleep_time_ghoul = 0.1


@Client.on_message(filters.command("я гуль", prefixes=prefix) & filters.me)
async def ghoul_spam_handler(client, message):
    i = 1000
    while i > 0:
        try:
            await client.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except FloodWait as e:
            await asyncio.sleep(e.x)

        i -= 7
        await asyncio.sleep(1/messages_per_second)

    if end_message != '':
        await client.send_message(message.chat.id, end_message)


module_list['Troll'] = f'{prefix}hack | {prefix}jopa | {prefix}drugs | {prefix}mum | {prefix}policya | {prefix}loveyou | {prefix}Я гуль'
file_list['Troll'] = 'troll.py'
