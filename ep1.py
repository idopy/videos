import discord
from discord.ext import commands
import datetime
client = commands.Bot(command_prefix='!',help_command=None,intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.command()
async def help(ctx):
    await ctx.reply('commands is \n**ping_send**\n**ping_reply**\n**say_hello**\nprefix is **!**')

@client.command()
async def ping_send(ctx):
    await ctx.send('Pong')

@client.command()
async def ping_reply(ctx):
    await ctx.reply('Pong')

@client.command()
async def say_hello(ctx):
    await ctx.reply(f'Hello {ctx.author}')

@client.command()
async def time(ctx):
    timern = datetime.datetime.now()
    await ctx.send(f'Time right now {timern}')

client.run('token')
