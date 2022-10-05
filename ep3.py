import datetime
import discord
from discord.ext import commands

with open('token.txt', 'r') as f:
    token = f.read()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)


@bot.event
async def on_ready():
    print(f'{bot.user.name}#{bot.user.discriminator} is ready.')
    print(f'{bot.user.id}')


@bot.command()
async def profile(ctx: commands.Context, member: discord.Member = None):
    if member is None: member = ctx.author
    global embed
    embed = discord.Embed(title='profile', description=f'profile command by {ctx.author.mention}',
                          timestamp=datetime.datetime.now(), color=discord.Color.random())
    stringstatus = str(member.status)
    embed.add_field(name='**name: **', value=f'`{member.name}`')
    embed.add_field(name='**id: **', value=f'`{member.id}`')
    embed.add_field(name='**is bot: **', value=f'`{member.bot}`')
    embed.add_field(name='**top role: **', value=f'`{member.top_role}`')
    stringtimeout = str(member.is_timed_out())
    if stringtimeout == 'True':
        embed.add_field(name='**is timed out: **', value=f'`True`')
        embed.add_field(name='**time out end in: **', value=f'`{member.timed_out_until}`')
    if stringstatus == 'dnd':
        embed.add_field(name='**status: **', value=f'`do_not_disturb`')
    else:
        embed.add_field(name='**status: **', value=f'`{member.status}`')
    embed.add_field(name='**full name: **', value=f'`{member.name}#{member.discriminator}`')
    embed.add_field(name='**roles: **',
                    value=f'`{member.name} have {len(member.roles)} roles in server {ctx.guild.name}\n{member.roles}`')
    embed.add_field(name='**is administrator: **', value=f'`{member.guild_permissions.administrator}`')
    try:
        embed.set_footer(text=f'{member.name}#{member.discriminator}', icon_url=member.avatar.url)
    except:
        pass
    try:
        embed.set_author(name='', icon_url=member.avatar.url)
    except:
        pass
    try:
        embed.set_image(url=member.avatar.url)
    except:
        pass
    global msg
    msg = await ctx.send(embed=embed)


@bot.command()
async def editemb(ctx: commands.Context):
    try:
        embed.clear_fields()
        await msg.edit(embed=embed)
    except:
        await ctx.send('you dont have embed yet!')


bot.run(token)
