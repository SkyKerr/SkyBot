currentVersion = "0.0"
currentBuild = "21w14a"

import discord
import json
with open('config.json') as f:
    config = json.load(f)

print(f'Starting up: Skybot Version {currentVersion} build {currentBuild}')

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
    if message.content.startswith(config['commandChar']):
        command = message.content.replace(config['commandChar'], "").lower()

    if command == 'ping':
        message.channel.send('Pong!')

    if command == 'version':
        message.channel.send(f'Version {currentVersion}, Build {currentBuild}')

client.run(config['token'])
