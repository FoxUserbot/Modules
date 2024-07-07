from random import randint , choice
from time import sleep

from pyrogram import Client, filters

from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix

@Client.on_message(filters.command("stream", prefixes=my_prefix()) & filters.me)
async def stream_kangel(cilent,message):
	actions = ['💵 Получаем донат!','🛍 Делаем обзор...','💻 Играем в игру','🍰 Кушаем...','💊 Принимаем Эмбиан...']
	try:
		await message.edit('💅 Перевоплощаемся!')
		sleep(2)
		await message.edit('⌨️ Запускаем стрим...')
		for _ in range(2):
			sleep(2)
			c = choice(actions)
			await message.edit(c)
			actions.remove(c)
		num_subs = randint(100,1000)
		await message.edit('❤️ Отключаем стрим и прощаемся с отаку...')
		sleep(2)
		await message.edit(f'''
			👋 Стрим окончен!
			Вы получили {num_subs} новых подписчиков.
			''')
	except Exception as e:
		await cilent.send_message(message.chat.id,f'❌ Случилась ошибка! | {e}')

module_list['Stream'] = f'{my_prefix()}stream'
file_list['Strea'] = 'stream.py'
