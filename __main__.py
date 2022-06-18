from index import *
from commands import *
from guildSettings.guildSettings import *

print(f'Starting up: Skybot {version}')

@client.event
# Function called automatically after client.run() is called
async def on_ready():
    # Set bot status ("presence") as a type of game
    await client.change_presence(activity=discord.Game(f'({version}) {botInfo["statusMessage"]}'))
    # Print the username of the client the bot is logged into
    print(f'logged in as {client.user}\n\n')

@client.event
# Function called by the discord library any time a message is sent
async def on_message(message):
    # Load the guild settings (./guildSettings/guildSettings.py)
    settings = guildSettings(message)
    
    # Ignore the message if it comes from the bot itself (Skynet Prevention)
    if message.author == client.user:
        return
    
    # All commands referring to settings (./guildSettings/guildSettings.py)
    await settingsCommands(message, settings)
    
    # Return if the bot is disabled
    if (not settings['enableBot']):
        return
    
    # Automated message responses not prompted by a command (./commands.py)
    if settings['allowMessageResponses']:
        await messageResponses(message)

    # All messages that start with the command character:
    if message.content.startswith(settings['commandChar']):
        # Splits the message into pieces ("arguments") and pops out the first of these as the command
        args = shlex.split(message.content.lower().replace(settings['commandChar'],''))
        command = args.pop(0)
        
        # (./commands.py)
        await userCommands(message, command, args, settings)
        if settings['allowJapeCommands']:
            await japeCommands(message, command, args, settings)

# Discord login:
client.run(config['token'])
