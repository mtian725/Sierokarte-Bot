import discord
import json
#Add mode modules as we add more

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

# Actual bot ID do NOT change
client.run(env['token'])
