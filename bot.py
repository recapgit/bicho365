from datetime import timezone, datetime
import discord
from discord import Embed
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='r!', intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')
    
saldos = {} # armazenamento dos saldos
    
@bot.command()
async def receber(ctx):
    user = ctx.author
    
    chance = random.randint(1, 100) # RNG

    if chance <= 70:
        ganhos = random.randint(1, 50)         # 70% de chance
    elif chance <= 95:
        ganhos = random.randint(51, 100)       # 25% de chance
    else:
        ganhos = random.randint(101, 150)      # 5% de chance
        
    saldo_atual = saldos.get(user.id, 0)
    novo_saldo = saldo_atual + ganhos
    saldos[user.id] = novo_saldo
    msg = f"+{ganhos} moedas! Seu saldo agora é de: {novo_saldo}"
    if ganhos <= 50:
        await ctx.send(f"{msg}")
    elif ganhos <= 100:
        await ctx.send(f"Boa 💰 {msg}")
    else:
        await ctx.send(f"O tigrinho soltou a carta 🐯, {msg}")
        
@bot.command()
async def saldo(ctx):
    user = ctx.author
    saldo = saldos.get(user.id, 0)
    await ctx.send(f"Você tem {saldo} moedas")
        
@bot.command()
async def exemplo(ctx):
    embed = Embed(
        title="Lista dos bichos para apostar",
        description="Avestruz(1) 🪶\n01 - 02 - 03 - 04\n...\nVaca(25) 🐮\n97 - 98 - 99 - 00",
        color=0xFF0000  # Vermelho
    )
    await ctx.send(embed=embed)

        
bot.run(token, log_handler=handler, log_level=logging.DEBUG)