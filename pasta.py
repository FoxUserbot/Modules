from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list

from prefix import my_prefix
from requirements_installer import install_library

from random import randint
from time import sleep

install_library('faker')
from faker import Faker


@Client.on_message(filters.command("doxx", prefixes=my_prefix()) & filters.me)
async def hack(client, message):
    fake = Faker('ru_RU')
    await message.edit('Доксим тя пидор')
    if randint(0, 1) == 0:
        name = 'Артур Ламаев'
    else:
        name = fake.name()
    pasta = f'''
Докс на тя:
- - - - - - 
ФИО : {name}
Адрес электронной почты : {fake.email()}
Телефон : {fake.phone_number()}
Адрес регистрации : {fake.street_address()}
Пароль к почте : {fake.password()}
Карта : {fake.credit_card_full()}
Паспорт: {fake.passport_number()}
- - - - - -
Жди докс бошеее
'''
    sleep(2)
    await message.edit(pasta)


module_list['Doxx'] = f'{my_prefix()}doxx'
file_list['Doxx'] = 'pasta.py'