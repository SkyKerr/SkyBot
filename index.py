import discord
import json
with open('config.json') as f:
    config = json.load(f)
with open('botSettings.json') as f:
    botSettings = json.load(f)

statusMessage = (f'Skybot Version {botSettings["currentVersion"]} build {botSettings["currentBuild"]}')
print(f'Starting up: {statusMessage}')

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message): # Message content responses
    if message.author == client.user:
        return

    if 'spoopy' in message.content.lower():
        await message.add_reaction('🚫')

@client.event
async def on_message(message): # User Command Responses
    if message.author == client.user:
        return

    command = ""
    if message.content.startswith(botSettings['commandChar']):
        command = message.content.replace(botSettings['commandChar'], "").lower()

    if command == 'ping':
        await message.channel.send('Pong!')

    if command == 'version':
        await message.channel.send(statusMessage)

client.run(config['token'])
