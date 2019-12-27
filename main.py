import discord
import calculator
import json
#Add mode modules as we add more

#testing purposes
number = {}
strings = {}

with open("config.json", "r") as read_file:
    env = json.load(read_file)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$hello': #eventually remove
        await message.channel.send('Hello!')

    if message.content == '$wiki': #basic
        await message.channel.send('https://gbf.wiki/Main_Page')

    if message.content == '$me': #testing user stuff
        await message.channel.send(message.author)

    if message.content == '$inc':
        if message.author in number:
            number[message.author] += 1
            await message.channel.send(data[message.author])
        else:
            number[message.author] = 0
            await message.channel.send(data[message.author])

    if message.content.startswith('$add '):
        if message.author in strings:
            strings[message.author].append(message.content[5:])
            await message.channel.send(strings[message.author])
        else:
            strings[message.author] = []
            strings[message.author].append(message.content[5:])
            await message.channel.send(strings[message.author])

    if message.content == '$clear':
        strings[message.author] = []
        await message.channel.send('Cleared')

    if message.content == '$list':
        await message.channel.send(strings[message.author])

    #if message.content.startswith('$calculator'):
    #    await message.channel.send(calc)

# Actual bot ID do NOT change
client.run(env['token'])
