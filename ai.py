from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix
from requirements_installer import install_library

import base64
import requests
import asyncio

install_library('openai') 
from openai import AsyncOpenAI, APIError

public_key = "c2stb3ItdjEtNjg1YzZiMDc2YjJhNDE4M2VkNTUzOWIyMTk3ZWY4MTk3YjkxYTE1ZDMxOTAxZjQ2YTQ5MTk0NTFjYzkxYzRmZQ=="

proxylist = ["127.0.0.1:2080"]

modules = {
    "deepseek": "deepseek/deepseek-chat:free",
    "gemini": "google/gemini-2.0-flash-exp:free",
    "qwen": "qwen/qwq-32b:free:free",
    
}

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

@Client.on_message(filters.command("ai", prefixes=my_prefix()) & filters.me)
async def ai(client, message):
    try:
        module = message.text.split()[1].lower()
        model = modules.get(module)
        
        if not model:
            await message.edit("❌ Incorrect model indicated!")
            return

        await message.edit("🤖 Processing request...")
        message_for_da = " ".join(message.text.split()[2:])
        
        result = ""
        retry_count = 1

        try:
            client_ai = AsyncOpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=str(base64.b64decode(public_key).decode('utf-8'))
            )
            
            response = await client_ai.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": message_for_da}]
            )
            result = response.choices[0].message.content
            if len(result) == 0:
                raise ValueError
        except:
            while len(result) == 0:
                try:
                    proxies = get_proxy()
                    proxy = proxies[0]

                    if not proxy:
                        await message.edit("❌ No working proxies available!")
                        return

                    await message.edit(f"⚠️ Trying proxy №{retry_count}")
                    async with httpx.AsyncClient(proxy=f"http://{proxy}", timeout=25.0) as session:
                        client_ai = AsyncOpenAI(
                            base_url="https://openrouter.ai/api/v1",
                            api_key=str(base64.b64decode(public_key).decode('utf-8')),
                            http_client=session
                        )
                        
                        response = await client_ai.chat.completions.create(
                            model=model,
                            messages=[{"role": "user", "content": message_for_da}]
                        )
                        result = response.choices[0].message.content
                except Exception as e:
                    print(f"ERROR: {e}")
                    print(f"[DEBUG] Proxy failed: {proxy}")
                    if proxy in proxylist:
                        proxylist.remove(proxy)
                    retry_count += 1
                    await asyncio.sleep(1)  

            if not result:
                await message.edit("❌ Failed to get response after retries!")
                return

        await message.edit(f"""👤 Prompt: {message_for_da}
📔 Model: {module}
🤖 Answer: {result}
""")

    except IndexError:
        await message.edit(f"❌ Не указаны данные! Используйте: {my_prefix()}ai <модель> <запрос>")
    except APIError as e:
        await message.edit(f"❌ Ошибка API OpenRouter: {e}")
    except Exception as e:
        await message.edit(f"❌ Произошла непредвиденная ошибка: {e}")

module_list['AI'] = f'{my_prefix()}AI [Gemini/DeepSeek/Qwen] [Message]'
file_list['AI'] = 'ai.py'
