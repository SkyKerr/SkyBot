from index import *
from commands import userCommands, messageResponses

print(f'Starting up: {statusMessage}')

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

    if message.content.startswith(botInfo['commandChar']):
        args = message.content.replace(botInfo['commandChar'], "").split(' ')
        command = args.pop(0)
        
        await userCommands(message, command, args)

client.run(config['token'])
