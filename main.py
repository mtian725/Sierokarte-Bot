# Python libraries
#import json
import asyncio
from datetime import datetime
from pytz import timezone
import pytz
import os
import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
# Google library
from googlesearch import search
# Discord libraries
import discord
from discord.ext import commands
# Our libraries
from resources import (exceptions, messages, uncap, imagelinks, traits)
import calculator
import raidfinder, tweepy
#Add mode modules as we add more

jp_tz = timezone('Japan')

uncap_targets = {}
global_teams = {}
raid_listeners = {} # map of raids to users listening for those raids
rf = None
TWITTER_APP_KEY = 'ZDS57sqDWzSbZQoVDyqc0t6EN'
TWITTER_APP_SECRET = 'ZppyVjPedv7wzy2WnHlWWZ29GWYAH1fig0tJkInLPLNl6BUk6d'
TWITTER_KEY = '905698903734943745-vDZJR2vaaMoyNYmz1jIZMMAaJChaZ8U'
TWITTER_SECRET = 'zpJ3GI6nZlWYrc7qaUKfNfB9a8BwBHFhUSe5jCBGjWEjI'
auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)

# use if testing locally, current code uses heroku env config vars
#with open("config.json", "r") as read_file:
#   env = json.load(read_file)

client = commands.Bot(command_prefix='!')
client.remove_command('help')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(aliases=['asdf'])
async def bleh(ctx):
    if (ctx.author.id == 359348256775471106):
        while True:
            try:
                def check(m):
                    return ((m.author.id == 327928764535275542) and m.content == '🗡️')

                msg = await client.wait_for('message',timeout=30.0,check=check)
            except asyncio.TimeoutError:
                #do nothing
                pass
            else:
                await msg.delete()
    return

@client.command(aliases=['h'])
async def help(ctx, *args):
    # sends a private message to the author with the help embed
    if not args:
        await ctx.author.send(embed=messages.help)
    else:
        return

@client.command(aliases=['w'])
async def wiki(ctx, *args):
    if not args:
        await ctx.send('https://gbf.wiki/Main_Page')
    else:
        # using googlesearch module
        query = 'gbf.wiki ' + '/'.join(args)
        for j in search(query, tld='com', num=1, stop=1, pause=0.0):
            await ctx.send(j)

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
            sent = await ctx.send(embed=messages.eternals)

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
                embeds = messages.eternals_1
                sent = await ctx.send(embed=embeds[0])
                await sent.add_reaction('1️⃣')
                await sent.add_reaction('2️⃣')
                await sent.add_reaction('3️⃣')
                await sent.add_reaction('4️⃣')
                await sent.add_reaction('5️⃣')
                await sent.add_reaction('6️⃣')
                while True:
                  try:
                      def react_check(reaction, user):
                          return (user == author and reaction.message.id == sent.id and
                          (str(reaction.emoji) == '1️⃣' or str(reaction.emoji) == '2️⃣'
                          or str(reaction.emoji) == '3️⃣' or str(reaction.emoji) == '4️⃣'
                          or str(reaction.emoji) == '5️⃣' or str(reaction.emoji) == '6️⃣'))

                      reaction, user = await client.wait_for('reaction_add', timeout=25.0,check=react_check)
                  except asyncio.TimeoutError:
                      break
                  else:
                      if str(reaction.emoji) == '1️⃣':
                          pos = 0
                      elif str(reaction.emoji) == '2️⃣':
                          pos = 1
                      elif str(reaction.emoji) == '3️⃣':
                          pos = 2
                      elif str(reaction.emoji) == '4️⃣':
                          pos = 3
                      elif str(reaction.emoji) == '5️⃣':
                          pos = 4
                      else:
                          pos = 5
                      await sent.edit(embed=embeds[pos])
            if option.content == '1':
                embeds = messages.eternals_2
                sent = await ctx.send(embed=embeds[0])
                await sent.add_reaction('1️⃣')
                await sent.add_reaction('2️⃣')
                await sent.add_reaction('3️⃣')
                await sent.add_reaction('4️⃣')
                await sent.add_reaction('5️⃣')
                await sent.add_reaction('6️⃣')
                await sent.add_reaction('7️⃣')
                await sent.add_reaction('8️⃣')
                await sent.add_reaction('9️⃣')
                while True:
                  try:
                      def react_check(reaction, user):
                          return (user == author and reaction.message.id == sent.id and
                          (str(reaction.emoji) == '1️⃣' or str(reaction.emoji) == '2️⃣'
                          or str(reaction.emoji) == '3️⃣' or str(reaction.emoji) == '4️⃣'
                          or str(reaction.emoji) == '5️⃣' or str(reaction.emoji) == '6️⃣'
                          or str(reaction.emoji) == '7️⃣' or str(reaction.emoji) == '8️⃣'
                          or str(reaction.emoji) == '9️⃣'))

                      reaction, user = await client.wait_for('reaction_add', timeout=25.0,check=react_check)
                  except asyncio.TimeoutError:
                      break
                  else:
                      if str(reaction.emoji) == '1️⃣':
                          pos = 0
                      elif str(reaction.emoji) == '2️⃣':
                          pos = 1
                      elif str(reaction.emoji) == '3️⃣':
                          pos = 2
                      elif str(reaction.emoji) == '4️⃣':
                          pos = 3
                      elif str(reaction.emoji) == '5️⃣':
                          pos = 4
                      elif str(reaction.emoji) == '6️⃣':
                          pos = 5
                      elif str(reaction.emoji) == '7️⃣':
                          pos = 6
                      elif str(reaction.emoji) == '8️⃣':
                          pos = 7
                      else:
                          pos = 8
                      await sent.edit(embed=embeds[pos])
    else:
        return

@client.command(aliases=['t'])
async def time(ctx, *args):
    if not args:
        # current time in japan
        jp_dt = datetime.now(jp_tz)
        hour = jp_dt.hour
        minute = jp_dt.minute
        cycle = 'AM'
        reset_hr = 29 - hour
        reset_min = 60 - minute

        # have to add a 0 because if you don't format the string :05 will be :5
        if jp_dt.minute < 10:
            minutes_str = '0' + str(jp_dt.minute)
        else:
            minutes_str = str(jp_dt.minute)

        msg1 = ('`' + str(hour) + ':' + minutes_str + '` JST (24 Hour Clock)')
        if (hour > 12):
            hour = hour - 12
            cycle = 'PM'
        msg2 = ('`' + str(hour) + ':' + minutes_str + '` ' + cycle +
                        ' JST (12 Hour Clock)')
        if reset_hr == 24:
            reset_hr = 0
        if reset_min == 60:
            reset_min = 0
        else:
            reset_hr = reset_hr - 1
        msg3 = ('**' + str(reset_hr) + '** hours and **' + str(reset_min) +
                        '** minutes before next daily reset')
        await ctx.send(msg1 + '\n' + msg2 + '\n' + msg3)


    else:
        return

@client.command(aliases=['a'])
async def art(ctx, *args):
    if not args:
        await ctx.send('Syntax: **!art <character name>**')
    else:
        name = ' '.join(args).lower()

        if name == 'random':
            chara = imagelinks.names[int(random.random() * len(imagelinks.names))]
        else:
            chara = process.extractOne(name, imagelinks.names)[0]

        name = chara
        num_images = len(imagelinks.images[name])
        pos = 0

        # the embed
        display = discord.Embed(
            title = name.upper(),
            color = imagelinks.images[name][0][0]
        )
        display.set_image(url = imagelinks.images[name][0][1])
        display.set_footer(text = 'click image for large display')
        sent = await ctx.send(embed=display)

        await sent.add_reaction('⬅️')
        await sent.add_reaction('➡️')

        author = ctx.author

        while True:
            try:
                # if a user clicks on a react then the image changes
                def react_check(reaction, user):
                    return (user == author and reaction.message.id == sent.id and
                    (str(reaction.emoji) == '⬅️' or str(reaction.emoji) == '➡️'))

                reaction, user = await client.wait_for('reaction_add', timeout=25.0,check=react_check)
            except asyncio.TimeoutError:
                break
            else:
                if str(reaction.emoji) == '⬅️':
                    pos = pos - 1
                if str(reaction.emoji) == '➡️':
                    pos = pos + 1

                display.set_image(url = imagelinks.images[name][pos % num_images][1])
                display.color = imagelinks.images[name][pos % num_images][0]
                await sent.edit(embed=display)

        return

@client.command(aliases=['f'])
async def find(ctx, *args):
    if not args:
        await ctx.send('Syntax: **!filter <trait1> <trait2> ...**')
    else:
        matches = {}
        msg = 'Characters that are : '
        for i in args:
            lw = i.lower()

            if not lw in traits.tags:
                await ctx.send('**' + lw.upper() + '** is not a registered tag.'
                                + '**!help** has the registered tags.')
                return

            if matches == {}:
                matches = traits.tags[lw]
            else:
                matches = matches & traits.tags[lw]

            msg = msg + '**' + lw.upper() + '** '

        # the embed
        display = discord.Embed(
            title = msg,
            color = discord.Color.red()
        )

        matches = list(matches)
        matches.sort()
        num_matches = len(matches)
        page = 0

        text = ''
        if num_matches < 15:
            for i in matches:
                text = text + i + '\n'

            display.description = text
            await ctx.send(embed=display)
            return
        else:
            for i in range(15):
                text = text + matches[i] + '\n'

            display.description = text
            sent = await ctx.send(embed=display)

            await sent.add_reaction('⬅️')
            await sent.add_reaction('➡️')

            author = ctx.author

            max_pages = int(num_matches/15)

            while True:
                try:
                    # if a user clicks on a react then the image changes
                    def react_check(reaction, user):
                        return (user == author and reaction.message.id == sent.id and
                        (str(reaction.emoji) == '⬅️' or str(reaction.emoji) == '➡️'))

                    reaction, user = await client.wait_for('reaction_add', timeout=25.0,check=react_check)
                except asyncio.TimeoutError:
                    break
                else:
                    if str(reaction.emoji) == '⬅️':
                        page = page - 1
                    if str(reaction.emoji) == '➡️':
                        page = page + 1

                    if (page > max_pages):
                        page = 0
                    if (page < 0):
                        page = max_pages

                    text = ''
                    for i in range((page*15),((page+1)*15)):
                        if (i < num_matches):
                            text = text + matches[i] + '\n'

                    display.description = text

                    await sent.edit(embed=display)

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

#removeall will skip because dynamic size evaluation for lists pepega
@client.command()
async def removeall(ctx):
    await asyncio.sleep(1)
    try:
        channel = ctx.channel
        author = ctx.author

        sent1 = await ctx.send(embed=messages.remove_1)
        def check(m):
            return ((m.content == '!removeall') or (m.content == 'c') or not(m.content.startswith('!')))
        start = await client.wait_for('message', timeout=20.0,check=check)
        await asyncio.sleep(0.5)
        await sent1.delete()

        if start.content == '!removeall':
            raise exceptions.Override()
        if start.content == 'c':
            raise exceptions.Cancel()

        for i in range (0, 3):
            arr = global_teams[author][i]
            j = 0
            while (j < len(arr)):
                if (arr[j] == start.content):
                    arr.pop(j)
                else:
                    j = j + 1

        for i in range (0, 3):
            if (len(global_teams[author][i]) == 0):
                global_teams[author][i] = [None]

    except asyncio.TimeoutError:
        await sent.delete()
        await ctx.send('Timed out. Do **!removeall** to try again.')

    except exceptions.Cancel:
        await ctx.send('Command Cancelled')

    except exceptions.Override:
        await ctx.send('Canceling previous command...')

@client.command()
async def remove(ctx):
    await asyncio.sleep(1)
    try:
        channel = ctx.channel
        author = ctx.author

        sent1 = await ctx.send(embed=messages.remove_1)
        def check(m):
            return ((m.content == '!removeall') or (m.content == 'c') or not(m.content.startswith('!')))
        start = await client.wait_for('message', timeout=20.0, check=check)
        await asyncio.sleep(0.5)
        await sent1.delete()

        if start.content == '!remove':
            raise exceptions.Override()
        if start.content == 'c':
            raise exceptions.Cancel()

        sent2 = await ctx.send(embed=messages.remove_2)
        def check2(m):
            return (m.content == '1' or m.content == '2' or m.content == '3'
            or m.content == '4' or m.content == '5' or m.content == '6' or m.content == '7'
            or m.content == '8' or m.content == '9' or m.content == '10' or m.content == 'c'
            or m.content == '!remove')

        start2 = await client.wait_for('message', timeout=20.0, check=check)
        await asyncio.sleep(0.5)
        await sent2.delete()

        if start2.content == '!remove':
            raise exceptions.Override()
        if start2.content == 'c':
            raise exceptions.Cancel()

        count = start2
        for i in range (0, 3):
            arr = global_teams[author][i]
            j = 0
            while (j < len(arr)):
                if (count <= 0):
                    break
                if (arr[j] == start.content):
                    arr.pop(j)
                    count = count - 1
                else:
                    j = j + 1

        for i in range (0, 3):
            if (len(global_teams[author][i]) == 0):
                global_teams[author][i] = [None]

    except asyncio.TimeoutError:
        await sent.delete()
        await ctx.send('Timed out. Do **!remove** to try again.')

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

#raidfinder stuff
@client.command(aliases=['r'])
async def raid(ctx, *args):
    if not args:
        await ctx.send('Syntax: **!r <boss name> <number of raids (does not work yet)>**')
    else:
        raid_name = ' '.join(args)
        if raid_name not in raid_listeners:
            raid_listeners[raid_name] = []
        raid_listeners[raid_name].append(ctx.author)
        await ctx.send('added ' + str(ctx.author) + ' to ' + raid_name + ' list')
        for listener in raid_listeners:
            print(listener, raid_listeners[listener])
        await get_rf(ctx)

async def get_rf(ctx):
    global rf
    global raid_listeners
    if rf is None:
        rf = raidfinder.Raidfinder(api, ctx, raid_listeners, asyncio.get_event_loop())
    return rf

@client.command(aliases=['rr'])
async def removeraid(ctx, *args):
    if not args:
        await ctx.send('Syntax: **!rr <boss name to unsubscribe from>')
    else:
        raid_name = ' '.join(args)
        if raid_name not in raid_listeners:
            await ctx.send('**' + raid_name + '** is either invalid or has no current subscribers.')
        elif ctx.author not in raid_listeners[raid_name]:
            await ctx.send(str(ctx.author) + ' is already unsubscribed from **' + raid_name + '**!')
        else:
            raid_listeners[raid_name].remove(ctx.author)
            if len(raid_listeners[raid_name]) == 0:
                del raid_listeners[raid_name]
            await ctx.send(str(ctx.author) + ' has been unsubscribed from **' + raid_name + '**.')

# Actual bot ID do NOT change
client.run(os.environ['token'])
#client.run(env['token'])
