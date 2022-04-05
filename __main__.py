from index import *
from commands import *

print(f'Starting up: Skybot {version}')

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(version))
    print('logged in as {0.user}\n\n'.format(client))

@client.event
async def on_message(message): 
    messageGuildSettings = guildSettings(message)
    
    if message.author == client.user:
        return
    
    await guildSettingsCommands(message, messageGuildSettings)
    if (not messageGuildSettings['enableBot']):
        return
    
    if messageGuildSettings['allowMessageResponses']:
        await messageResponses(message)

    if message.content.startswith(botInfo['commandChar']):
        args = shlex.split(message.content.lower().replace(botInfo['commandChar'],''))
        command = args.pop(0)
        
        await userCommands(message, command, args)
        if messageGuildSettings['allowJapeCommands']:
            await japeCommands(message, command, args)

client.run(config['token'])
