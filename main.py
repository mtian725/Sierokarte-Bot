# Python libraries
import json
import asyncio
# Discord libraries
import discord
from discord.ext import commands
# Our libraries
from resources import exceptions
from resources import messages
from resources import uncap
import calculator
#Add mode modules as we add more

uncap_targets = {}
global_teams = {}

with open("config.json", "r") as read_file:
    env = json.load(read_file)

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def wiki(ctx, *args):
    if not args:
        await ctx.send(messages.wiki)
    else:
        return

@client.command(aliases=['ca'])
async def calcarcarum(ctx, *args):
    if not args:
        await asyncio.sleep(0.5)
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
                or m.content.startswith('!')))

            summon = await client.wait_for('message', timeout=30.0,check=check)
            exceptions.comm_cancel(summon.content)
            await asyncio.sleep(1.25)
            await sent.delete()

            sent = await ctx.send(embed=messages.arc_calc_2)

            def check(m):
                return (m.channel == channel and m.author == author and
                (m.content == '0' or m.content == '1'
                or m.content == '2' or m.content == '3' or m.content == '4' or
                m.content == '5' or m.content == '6' or m.content == '7' or
                m.content == '8' or m.content == '9' or m.content == '10'
                or m.content == '11' or m.content == 'c'
                or m.content.startswith('!')))

            start = await client.wait_for('message', timeout=30.0,check=check)
            exceptions.comm_cancel(start.content)
            await asyncio.sleep(1.25)
            await sent.delete()

            sent = await ctx.send(embed=messages.arc_calc_3)
            end = await client.wait_for('message', timeout=30.0,check=check)
            exceptions.comm_cancel(end.content)
            await asyncio.sleep(1.25)
            await sent.delete()

            def check(m):
                return (m.channel == channel and m.author == author and
                (m.content == '0' or m.content == '1' or m.content == 'c'
                or m.content.startswith('!')))

            sent = await ctx.send(embed=messages.arc_calc_4)
            toggle = await client.wait_for('message',timeout=30.0,check=check)
            exceptions.comm_cancel(toggle.content)
            await asyncio.sleep(0.5)
            await sent.delete()

        except asyncio.TimeoutError:
            await sent.delete()
            await ctx.send('Timed out')

        except exceptions.Cancel:
            await ctx.send('Command Cancelled')

        except exceptions.Override:
            await ctx.send('Cancelled previous command')

        else:
            summon = int(summon.content)
            start = int(start.content)
            end = int(end.content) + 1
            toggle = int(toggle.content)

            title = 'Total Materials Needed : '+str(author)+'\n'
            title = title+uncap.steps[start]+' to '+uncap.steps[end]
            materials = discord.Embed(
                title = title,
                description = calculator.arcarum(summon,start,end,toggle),
                color = discord.Color.orange()
            )
            thumbnail = messages.arc_thumbnails[uncap.arcarum_summon[summon]]
            materials.set_thumbnail(url=thumbnail)
            await ctx.send(embed=materials)
    else:
        return

@client.command(aliases=['e'])
async def eternals(ctx, *args):
    if not args:
        try:
            await asyncio.sleep(0.5)
            channel = ctx.channel
            author = ctx.author
            sent = await ctx.send(embed=messages.eternals_1)

            def check(m):
                return (m.channel == channel and m.author == author and
                (m.content == '0' or m.content == '1' or m.content == 'c'
                or m.content.startswith('!')))

            option = await client.wait_for('message',timeout=30.0,check=check)
            exceptions.comm_cancel(option.content)
            await asyncio.sleep(0.5)
            await sent.delete()

        except asyncio.TimeoutError:
            await sent.delete()
            await ctx.send('Timed out')

        except exceptions.Cancel:
            await ctx.send('Command Cancelled')

        except exceptions.Override:
            await ctx.send('Cancelled previous command')

        else:
            if option.content == '0':
                temp = discord.Embed(
                    title = 'Something',
                    description = 'Soemthing',
                    color = discord.Color.blue(),
                )
                sent = await ctx.send(embed=temp)
                await asyncio.sleep(1)
                await ctx.send('filler\nfiller\nfilller')
                temp = discord.Embed(
                    title = 'new',
                    description = 'new',
                    color = discord.Color.blue(),
                )
                await sent.edit(embed=temp)
            else:
                await ctx.send('Slected 1')
    else:
        return

@client.command()
async def team(ctx):
    await asyncio.sleep(1)
    channel = ctx.channel
    author = ctx.author

    if not(author in global_teams):
        global_teams[author]=[[None],[None],[None]]

    await ctx.send(global_teams[author])
#Note: with this implementation, the hashmap will permamently have an object for each author, or something like that

#To Add: emote to show successfully added something
@client.command()
async def add(ctx):
    await asyncio.sleep(1)
    try:
        channel = ctx.channel
        author = ctx.author

        sent1 = await ctx.send(embed=messages.add_1)
        def check1(m):
                return (m.channel == channel and m.author == author and
                (m.content == '0' or m.content == '1'
                or m.content == '2' or m.content == 'c' or (m.content == '$add')))
        start = await client.wait_for('message', timeout=20.0,check=check1)
        await asyncio.sleep(0.5)
        await sent1.delete()

        if start.content == '$add':
            raise exceptions.Override()
        if start.content == 'c':
            raise exceptions.Cancel()

        sent2 = await ctx.send(embed=messages.add_2)
        def check2(m):
            return not(m.content == '$add')
        toaddname = await client.wait_for('message', timeout=30.0, check=check2)
        await asyncio.sleep(0.5)
        await sent2.delete()
        if toaddname.content == 'c':
            raise exceptions.Cancel()

        if start.content == '0':
            if (len(global_teams[author][0]) >= 6):
                await ctx.send(embed=messages.add_3)
                raise exceptions.TooMany
            else:
                if(global_teams[author][0][0] == None):
                    global_teams[author][0] = [toaddname.content]
                else:
                    global_teams[author][0].append(toaddname.content)

        if start.content == '1':
            #the cap of 10 does NOt account for auxillary dual wielding
            if (len(global_teams[author][1]) >= 10):
                await ctx.send(embed=messages.add_4)
                raise exceptions.TooMany
            else:
                if(global_teams[author][1][0] == None):
                    global_teams[author][1] = [toaddname.content]
                else:
                    global_teams[author][1].append(toaddname.content)

        if start.content == '2':
            if (len(global_teams[author][2]) >= 6):
                await ctx.send(embed=messages.add_4)
                raise exceptions.TooMany
            else:
                if(global_teams[author][2][0] == None):
                    global_teams[author][2] = [toaddname.content]
                else:
                    global_teams[author][2].append(toaddname.content)

    except asyncio.TimeoutError:
        await sent.delete()
        await ctx.send('Timed out. Do **$add** to try again.')

    except exceptions.Cancel:
        await ctx.send('Command Cancelled')

    except exceptions.Override:
        await ctx.send('Canceling previous command...')

#remove will skip because dynamic size evaluation for lists pepega
@client.command()
async def remove(ctx):
    await asyncio.sleep(1)
    try:
        channel = ctx.channel
        author = ctx.author

        sent1 = await ctx.send(embed=messages.remove_1)
        def check(m):
            return ((m.content == '$remove') or (m.content == 'c') or not(m.content.startswith('$')))
        start = await client.wait_for('message', timeout=20.0,check=check)
        await asyncio.sleep(0.5)
        await sent1.delete()

        if start.content == '$remove':
            raise exceptions.Override()
        if start.content == 'c':
            raise exceptions.Cancel()

        for i in range (0, 3):
            arr = global_teams[author][i]
            for j in range (0, len(arr)):
                if ((arr[-1 * j + len(arr) - 1]) == start.content):
                    arr.pop(-1 * j + len(arr) - 1)

        for i in range (0, 3):
            if (len(global_teams[author][i]) == 0):
                global_teams[author][i] = [None]

    except asyncio.TimeoutError:
        await sent.delete()
        await ctx.send('Timed out. Do **$add** to try again.')

    except exceptions.Cancel:
        await ctx.send('Command Cancelled')

    except exceptions.Override:
        await ctx.send('Canceling previous command...')

@client.command()
async def clearteam(ctx):
    channel = ctx.channel
    author = ctx.author
    global_teams[author] = [[None], [None], [None]]
    sent = await ctx.send("Cleared your team!")




# Actual bot ID do NOT change
client.run(env['token'])
