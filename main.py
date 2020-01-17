import discord
from discord.ext import commands
import asyncio
import exceptions
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
    await asyncio.sleep(1)
    try:
        channel = ctx.channel
        author = ctx.author
        sent = await ctx.send(embed=messages.arc_calc_1)

        def check(m):
            return (m.channel == channel and m.author == author and
            (m.content == '0' or m.content == '1'
            or m.content == '2' or m.content == '3' or m.content == '4' or
            m.content == '5' or m.content == '6' or m.content == '7' or
            m.content == '8' or m.content == '9' or m.content == 'c'
            or m.content == '$calcarcarum'))

        summon = await client.wait_for('message', timeout=45.0,check=check)
        await asyncio.sleep(0.5)
        await sent.delete()
        await summon.delete()
        if summon.content == 'c':
            raise exceptions.Cancel()

        if summon.content == '$calcarcarum':
            raise exceptions.Override()

        sent = await ctx.send(embed=messages.arc_calc_2)

        def check(m):
            return (m.channel == channel and m.author == author and
            (m.content == '0' or m.content == '1'
            or m.content == '2' or m.content == '3' or m.content == '4' or
            m.content == '5' or m.content == '6' or m.content == '7' or
            m.content == '8' or m.content == '9' or m.content == '10'
            or m.content == '11' or m.content == 'c'
            or m.content == '$calcarcarum'))

        start = await client.wait_for('message', timeout=45.0,check=check)
        await asyncio.sleep(0.5)
        await sent.delete()
        await start.delete()
        if start.content == 'c':
            raise exceptions.Cancel()

        if start.content == '$calcarcarum':
            raise exceptions.Override()

        sent = await ctx.send(embed=messages.arc_calc_3)
        end = await client.wait_for('message', timeout=45.0,check=check)
        await asyncio.sleep(0.5)
        await sent.delete()
        await end.delete()
        if end.content == 'c':
            await ctx.send('Command Cancelled')

        if end.content == '$calcarcarum':
            raise exceptions.Override()

    except asyncio.TimeoutError:
        await sent.delete()
        await ctx.send('Timed out. Do **$calcarcarum** to try again.')

    except exceptions.Cancel:
        await ctx.send('Command Cancelled')

    except exceptions.Override:
        await ctx.send('Overriding previous command...')

    else:
        summon = int(summon.content)
        start = int(start.content)
        end = int(end.content) + 1

        materials = discord.Embed(
            title = 'Total Materials Needed',
            description = calculator.arcarum(summon,start,end),
            color = discord.Color.orange()
        )
        await ctx.send(embed=materials)

@client.command()
async def editteam(ctx):
    await asyncio.sleep(1)
    try:
        team = [[None],[None],[None]]
        channel = ctx.channel
        author = ctx.author
        sent = await ctx.send(team)

        def check(m):
            return (m.channel == channel and m.author == author and
            (m.content == '0' or m.content == '1'
            or m.content == '2' or m.content == '3' or m.content == '4' or
            m.content == '5' or m.content == '6' or m.content == '7' or
            m.content == '8' or m.content == '9' or m.content == 'c'
            or m.content == '$calcarcarum'))

        summon = await client.wait_for('message', timeout=45.0,check=check)
        await asyncio.sleep(0.5)
        await sent.delete()
        await summon.delete()
        if summon.content == 'c':
            raise exceptions.Cancel()

        if summon.content == '$editteam':
            ctx.send("Resetting...")
            raise exceptions.Override()

        sent = await ctx.send(embed=messages.arc_calc_2)

        def check(m):
            return (m.channel == channel and m.author == author and
            (m.content == '0' or m.content == '1'
            or m.content == '2' or m.content == '3' or m.content == '4' or
            m.content == '5' or m.content == '6' or m.content == '7' or
            m.content == '8' or m.content == '9' or m.content == '10'
            or m.content == '11' or m.content == 'c'
            or m.content == '$calcarcarum'))

        start = await client.wait_for('message', timeout=45.0,check=check)
        await asyncio.sleep(0.5)
        await sent.delete()
        await start.delete()
        if start.content == 'c':
            raise exceptions.Cancel()

        if start.content == '$calcarcarum':
            raise exceptions.Override()

        sent = await ctx.send(embed=messages.arc_calc_3)
        end = await client.wait_for('message', timeout=45.0,check=check)
        await asyncio.sleep(0.5)
        await sent.delete()
        await end.delete()
        if end.content == 'c':
            await ctx.send('Command Cancelled')

        if end.content == '$calcarcarum':
            raise exceptions.Override()

    except asyncio.TimeoutError:
        await sent.delete()
        await ctx.send('Timed out. Do **$calcarcarum** to try again.')

    except exceptions.Cancel:
        await ctx.send('Command Cancelled')

    except exceptions.Override:
        await ctx.send('Overriding previous command...')

    else:
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
