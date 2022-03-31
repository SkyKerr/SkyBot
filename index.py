import discord
import json
with open('config.json') as f:
    config = json.load(f)
with open('botSettings.json') as f:
    botSettings = json.load(f)
    
from commands import userCommands, messageResponses

print(f'Starting up: Skybot Version {botSettings["currentVersion"]} build {botSettings["currentBuild"]}')

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}\n\n'.format(client))
    
# Everything Else Here:

@client.event
async def on_message(message): 
    if message.author == client.user:
        return
    
    await messageResponses(message)

    if message.content.startswith(botSettings['commandChar']):
        args = message.content.replace(botSettings['commandChar'], "").split(' ')
        command = args.pop(0)
        
        await userCommands(message, command, args)

client.run(config['token'])
