import discord
from discord.ext import commands
import asyncio
import time
import calculator
import messages
import json
#Add mode modules as we add more

uncap_targets = {}

with open("config.json", "r") as read_file:
    env = json.load(read_file)

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def wiki(ctx):
    await ctx.send(messages.wiki)

@client.command()
async def calcarcarum(ctx):
    channel = ctx.channel
    author = ctx.author
    sent = await ctx.send(embed=messages.arc_calc_1)

    def check(m):
        return (m.channel == channel and m.author == author and
        (m.content == '0' or m.content == '1'
        or m.content == '2' or m.content == '3' or m.content == '4' or
        m.content == '5' or m.content == '6' or m.content == '7' or
        m.content == '8' or m.content == '9'))

    summon = await client.wait_for('message',check=check)
    await sent.delete()
    await summon.delete()
    sent = await ctx.send(embed=messages.arc_calc_2)

    def check(m):
        return (m.channel == channel and m.author == author and
        (m.content == '0' or m.content == '1'
        or m.content == '2' or m.content == '3' or m.content == '4' or
        m.content == '5' or m.content == '6' or m.content == '7' or
        m.content == '8' or m.content == '9' or m.content == '10'
        or m.content == '11'))

    start = await client.wait_for('message',check=check)
    await sent.delete()
    await start.delete()
    sent = await ctx.send(embed=messages.arc_calc_3)
    end = await client.wait_for('message',check=check)
    await sent.delete()
    await end.delete()

    summon = int(summon.content)
    start = int(start.content)
    end = int(end.content) + 1

    materials = discord.Embed(
        title = 'Total Materials Needed',
        description = calculator.arcarum(summon,start,end),
        color = discord.Color.orange()
    )
    await ctx.send(embed=materials)

# Actual bot ID do NOT change
client.run(env['token'])
