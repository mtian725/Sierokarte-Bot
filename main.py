import discord
import calculator
import json
#Add mode modules as we add more

uncap_targets = {}

with open("config.json", "r") as read_file:
    env = json.load(read_file)

client = discord.Client()
#bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == '$wiki': #basic
        await message.channel.send('https://gbf.wiki/Main_Page')

    elif message.content == '$init resource calc':
        uncap_targets[message.author] = []
        await message.channel.send('```Calculator initialized\n$add [item]    -> add an item\n$remove [item] -> remove an item\n$calc list     -> show all items\n$total         -> show total sum\n$end calc      -> turn off calculator```')

    elif message.content.startswith('$add '):
        if message.author in uncap_targets:
            uncap_targets[message.author].append(message.content[5:])
            await message.channel.send('not implemented completely')
        else:
            await message.channel.send('Calculator not initialized')

    elif message.content.startswith('$remove '):
        if message.author in uncap_targets:
            await message.channel.send('not implemented')
        else:
            await message.channel.send('Calculator not initialized')

    elif message.content == '$calc list':
        if message.author in uncap_targets:
            list = '```\n'
            for item in uncap_targets[message.author]:
                list += item
                list += '\n'
            list += '```'
            await message.channel.send(list)
        else:
            await message.channel.send('Calculator not initialized')

    elif message.content == '$total':
        if message.author in uncap_targets:
            await message.channel.send('not implemented')
        else:
            await message.channel.send('Calculator not initialized')

    elif message.content == '$end calc':
        if message.author in uncap_targets:
            del uncap_targets[message.author]
            await message.channel.send('Calculator turned off')
        else:
            await message.channel.send('Calculator already turned off')

    else:
        return

    #if message.content.startswith('$add '):
    #    if message.author in strings:
    #        strings[message.author].append(message.content[5:])
    #        await message.channel.send(strings[message.author])
    #   else:
    #        strings[message.author] = []
    #        strings[message.author].append(message.content[5:])
    #        await message.channel.send(strings[message.author])

    #if message.content == '$clear':
    #    strings[message.author] = []
    #    await message.channel.send('Cleared')

    #if message.content == '$list':
    #    await message.channel.send(strings[message.author])

    #if message.content.startswith('$calculator'):
    #    await message.channel.send(calc)

# Actual bot ID do NOT change
client.run(env['token'])
