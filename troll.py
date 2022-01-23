from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
import asyncio
import random

from prefix import my_prefix
prefix = my_prefix()

app = Client
@app.on_message(filters.command("hack", prefix) & filters.me)
async def hack(client: Client, message: Message):
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
    text = "🐓Нашли файты что ты петух!"
    await message.edit(text)

# Команда Взлома жопы
@app.on_message(filters.command("jopa", prefix) & filters.me)
async def jopa(client: Client, message: Message):
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

# Наркота
@app.on_message(filters.command("drugs", prefix) & filters.me)
async def drugs(client: Client, message: Message):
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

# Оскорбление мамки
@app.on_message(filters.command("mum", prefix) & filters.me)
async def mum(client: Client, message: Message):
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


module_list['Troll'] = f'{prefix}hack | {prefix}jopa | {prefix}drugs | {prefix}mum'
file_list['Troll'] = 'troll.py'
