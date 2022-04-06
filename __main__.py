from index import *
from commands import *
from guildSettings.guildSettings import *

print(f'Starting up: Skybot {version}')

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(version))
    print('logged in as {0.user}\n\n'.format(client))

@client.event
async def on_message(message): 
    settings = guildSettings(message)
    
    if message.author == client.user:
        return
    
    await settingsCommands(message, settings)
    if (not settings['enableBot']):
        return
    
    if settings['allowMessageResponses']:
        await messageResponses(message)

    if message.content.startswith(botInfo['commandChar']):
        args = shlex.split(message.content.lower().replace(botInfo['commandChar'],''))
        command = args.pop(0)
        
        await userCommands(message, command, args)
        if settings['allowJapeCommands']:
            await japeCommands(message, command, args)

client.run(config['token'])
