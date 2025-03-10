import discord
from discord.ext import commands
import random
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Загружаем нецензурные ответы из отдельного файла
def load_rude_responses():
    with open('rude_responses.json', 'r', encoding='utf-8') as file:
        responses = json.load(file)
    return responses

# Загружаем токен из конфиг-файла
def load_config():
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    return config

config = load_config()
rude_responses = load_rude_responses()

# Автоответы на определённые слова
keywords_responses = {
    "админ": "Админов нет, иди лесом!",
    "вайп": "Вайп каждый вторник и пятницу в 15:00 по МСК!",
    "модер": "Модеров тут не ждут, проваливай!",
    "софт": "Софт скачай себе на голову! Пиши /report",
    "аим": "Аимщики идут лесом! А ты пиши /report",
    "читер": "Читеры тут не живут, вали отсюда! Пиши в игре /report",
    "промокод": "Промокод проси у мамки! Есть только 4FUNWIPE"
}

@bot.event
async def on_ready():
    print(f'Залогинился как {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user or message.channel.name != "💬чат":
        return

    message_content_lower = message.content.lower()

    for keyword, reply in keywords_responses.items():
        if keyword in message_content_lower:
            await message.channel.send(reply)
            return

    response = random.choice(rude_responses)
    await message.channel.send(response)

bot.run(config['token'])
