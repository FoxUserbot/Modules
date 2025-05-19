from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix

import requests
import re
import random

proxylist = []
result = []

def get_proxy():
    if proxylist:
        return proxylist
    else:
        temp_proxy = []
        try:
            url = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&proxy_format=ipport&format=text&timeout=3000"
            response = requests.get(url, timeout=2)
            proxies_text = response.text
            temp_proxies_list = [x.strip() for x in proxies_text.split("\n") if x.strip()]
            for _ in temp_proxies_list:
                temp_proxy.append(_)
        except:
            pass
        
        
        try:
            url = "http://rootjazz.com/proxies/proxies.txt"
            response = requests.get(url, timeout=4)
            proxies_text = response.text
            temp_proxies_list = [x.strip() for x in proxies_text.split("\n") if x.strip()]
            for _ in temp_proxies_list:
                temp_proxy.append(_)
        except:
            pass
        
        proxies_list = temp_proxy[:200]
        proxylist.extend(proxies_list)
        return proxies_list


def get_picture(tegs):
    tags = (tegs).replace(" ", "%20")
    url = f"http://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tags}"
    try:
        print("[DEBUG] No proxy")
        response = requests.get(url, timeout=5)
        text_data = response.text
        
        file_urls = re.findall(r'(file_url="([^"]+)")', text_data)
        for file_url in file_urls:
            result.append(file_url[1])
            
        try:
            if result is None:
                raise RuntimeError
            if len(result) == 0:
                raise RuntimeError
        except:
            raise RuntimeError
    except:
        while len(result) == 0:
            try:
                print("[DEBUG] Start proxy")
                proxies = get_proxy()
                proxy_host = proxies[0]

                response = requests.get(url, proxies={"http": proxy_host}, timeout=1)
                text_data = response.text
                print("[DEBUG] TEXT YEA")
                
                file_urls = re.findall(r'(file_url="([^"]+)")', text_data)
                for file_url in file_urls:
                    result.append(file_url[1])
                    

                if result is None:
                    raise RuntimeError

                if len(result) == 0:
                    raise RuntimeError
            except Exception as fff:
                print(f"ERROR: {fff}")
                print(f"[DEBUG] FUCK {proxy_host}")
                print(f"[DEBUG] I have {len(proxies)} proxy")
                if proxy_host in proxylist:
                    proxylist.remove(proxy_host)

    print("GO!")
    print(result)
    result_random = random.choice(result)
    return str(result_random)


@Client.on_message(filters.command("rule34", prefixes=my_prefix()) & filters.me)
async def rule34(client, message):
    result.clear()
    # await message.edit("Neko tyan..~")
    # try:
    #     resp = requests.get("https://nekos.best/api/v2/neko")
    #     data = resp.json()
    #     url = data["results"][0]["url"]
    #     await client.send_photo(message.chat.id, photo=str(url))
    #     await message.delete()
    # except Exception as f:
    #     await message.edit(f"Oops..~\n{f}")
    
    await message.edit("Search. The module may be slow, nya~, due to limitations of your fucking ISP 😡~")
    orig_text = ' '.join(message.text.split()[1:])
    get_pic = get_picture(orig_text)
    await message.edit("I'm sending it, nya...~")
    
    try:
        await client.send_photo(message.chat.id, photo=get_pic, caption=f"Tags: {orig_text}")
        await message.delete()
    except:
        await message.edit(f"Fucking telegram, nya..~\nTags: {orig_text}\nLink: {get_pic}")
    

module_list['Rule34'] = f'{my_prefix()}rule34'
file_list['Rule34'] = 'rule34.py'
