import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def nauka(ctx):
    message = "Чтобы сберечь природу надо иметь мусор!\n\n"
    message += "- Используйте многоразовые товары, такие как многоразовые пакеты, стаканчики и столовые приборы.\n"
    message += "- Переходите на цифровые форматы, чтобы избежать использования бумаги и пластиковых носителей информации.\n"
    message += "- Разделяйте отходы на перерабатываемые и неперерабатываемые материалы и утилизируйте их соответствующим образом.\n"
    message += "- Покупайте продукты с минимальным количеством упаковки и выбирайте упаковки, которые можно переработать или разложить.\n"
    message += "- Участвуйте в акциях по очистке окружающей среды и сознательно выбирайте места для отдыха, чтобы не загрязнять природу."
    print(message)
    await ctx.send(message)
    
    

bot.run("MTE1Mjk2MDkxMzc3MTYwMjAwMQ.GcINRb.kSNEQDpcDu9g5Q-5DgjPO_nqLzfV5lNwlEOqM0")