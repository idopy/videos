import discord
import asyncio
import random
from discord.ext import commands

with open('token.txt', 'r') as f:
    token = f.read()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)


@bot.event
async def on_ready():
    print(f'Bot is online.\nBot name: {bot.user.name}')


@bot.command()
async def hello(ctx: commands.Context):
    await ctx.send(f'hi {ctx.author.mention}')


@bot.command()
async def math(ctx: commands.Context):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-'])
    if operator == '-':
        qus_in_str = f"**{ctx.author}** your math question is {num1} - {num2}       you have 10 seconds"
        anwser = num1 - num2
        only_qus = f"{num1} - {num2}"
    if operator == '+':
        qus_in_str = f"**{ctx.author}** your math question is {num1} + {num2}       you have 10 seconds"
        anwser = num1 + num2
        only_qus = f"{num1} + {num2}"
    await ctx.send(qus_in_str)

    def check(m: discord.Message):
        return m.author.id == ctx.author.id and m.channel.id == ctx.message.channel.id

    try:
        msg = await bot.wait_for('message', check=check, timeout=10)

    except asyncio.TimeoutError:
        await ctx.send(f"**{ctx.author.mention}**time out!\nthe anwser for {only_qus} is {anwser}")
        return
    else:
        if operator == '+':
            if anwser == int(msg.content):
                await ctx.send('nice')
            else:
                await ctx.send(f'wrong the anwser for {only_qus} is {anwser}')
        if operator == '-':
            if anwser == int(msg.content):
                await ctx.send('nice')
            else:
                await ctx.send(f'wrong the anwser for {only_qus} is {anwser}')


@bot.command()
async def reply(ctx: commands.Context):
    await ctx.reply('hey this is message reply')


@bot.command()
async def edit(ctx: commands.Context):
    msg = await ctx.send('hey this is a message before edit')
    await asyncio.sleep(3)
    await msg.edit(content='**this is a message after edit**')


@commands.has_permissions(administrator=True)
@bot.command()
async def delete(ctx: commands.Context, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.author.send(f'deleted {amount} messages in {ctx.message.channel.mention}')


bot.run(token)
