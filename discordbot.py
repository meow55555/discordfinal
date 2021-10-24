#導入 Discord.py
import discord

from discord.ext import commands
from config import bot_token, user_token
import flask
import requests






bot = commands.Bot(command_prefix='/')
#client 是我們與 Discord 連結的橋樑
client = discord.Client()

@bot.command()
async def teststatus(ctx):
    await ctx.send(bot.latency)

@bot.command()
async def verbose_status(ctx):
    headers = {"auth": user_token}
    r = requests.get('http://127.0.0.1:8080/api/status?mode=verbose', headers=headers)
    bot.send(r.content)

@bot.command()
async def status(ctx):
    headers = {"auth": user_token}
    r = requests.get('http://127.0.0.1:8080/api/status', headers=headers)
    bot.send(r.content)


#調用 event 函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    print(">>Bot is online<<")
    print('目前登入身份：', bot.user)
    



bot.run(bot_token)

