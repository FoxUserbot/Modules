from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix
from requirements_installer import install_library

install_library('openai') 
from openai import OpenAI , APIError

client_ai = OpenAI(base_url="https://openrouter.ai/api/v1",api_key="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")
modules = {
    "deepseek": "deepseek/deepseek-chat:free",
    "gemini": "google/gemini-2.0-flash-001",
}
@Client.on_message(filters.command("ai", prefixes=my_prefix()) & filters.me)
async def ai(client, message):
    try:
        module = message.text.split()[1].lower()
        model = modules[module] if module in ["deepseek", "gemini"] else "error"
        if model == "error":
            await message.edit("Неправильно указана модель!")
        else:
            try:
                await message.edit("🤖 Обработка запроса...")
                message_for_da = " ".join(message.text.split()[2:])
                result = client_ai.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": message_for_da}
                    ]
                ).choices[0].message.content
                await message.edit(f"""👤 Запрос: {message_for_da}
📔 Модель: {module}
🤖 Ответ: {result}
""")
            except APIError as e:
                await message.edit(f"❌ Ошибка API OpenRouter: {e}")
            except Exception as e:
                await message.edit(f"❌ Произошла непредвиденная ошибка: {e}")
            

    except IndexError:
        await message.edit("Не указаны данные!")

module_list['AI'] = f'{my_prefix()}AI [Gemini/DeepSeek] [Message]'
file_list['AI'] = 'ai.py'



