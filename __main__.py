from index import *
from commands import *
from guildSettings.guildSettings import *

print(f'Starting up: Skybot {version}')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(f'({version}) {botInfo["statusMessage"]}'))
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
        await messageResponses(message, client)

    if message.content.startswith(settings['commandChar']):
        args = shlex.split(message.content.lower().replace(settings['commandChar'],''))
        command = args.pop(0)
        
        await userCommands(message, command, args, settings)
        if settings['allowJapeCommands']:
            await japeCommands(message, command, args, settings)


client.run(config['token'])
