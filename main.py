import discord
#Add mode modules as we add more

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
client.run('NjU5NjA5NjA1MTE4MzYxNjA1.XgQzxw.xkp_RnIr9mR-LTkqx9ULQfmHxAU')
