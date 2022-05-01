from index import *
with open('guildSettings/descriptions.json') as f:
	settingDescriptions = json.load(f)	

def guildSettings(message):
	guildID = message.channel.guild.id
	filePath = (f'guildSettings/guilds/{guildID}.json')
	
	if (not exists(filePath)):
		sh.copy('guildSettings/template.json', filePath)
		
	with open(filePath) as f:
		return json.load(f)
		
def setSetting(message, settings):
	guildID = message.channel.guild.id
	filePath = (f'guildSettings/guilds/{guildID}.json')
	
	with open(filePath, 'w') as f:
		f.write(json.dumps(settings))


async def settingsCommands(message, settings):
	if not message.content.startswith(botInfo['commandChar']):
		return
	args = message.content.replace(botInfo['commandChar'], "").split(' ')

	# Status command
	if args[0] == 'status':
		statusEmbed = discord.Embed(title=(f'Skybot {version}'), url=botInfo['githubLink'], description=botInfo['description'], color=0x87CEEB)
		if settings['enableBot'] == False:
			statusEmbed.add_field(name='Caution', value='The bot is currently disabled. To re-enable, a user with moderator powers must run `$settings enableBot True`')
		
		statusEmbed.set_thumbnail(url=botInfo['profilePic'])
		
		await message.channel.send(embed=statusEmbed)

	# All settings options below
	if(args[0].lower() == 'settings'):
		# settings embed
		if len(args)==1:
			messageEmbed = discord.Embed(title=(f'Server Settings for {message.channel.guild}'))
		
			for setting in settings:
				messageEmbed.add_field(
				name=(f'{setting}: {settings[setting]}'),
				value=(f'{settingDescriptions[setting]}'),
				inline=False)
		
			await message.channel.send(embed=messageEmbed)
			return
		
		# Change settings commands
		if args[1] in settings:
			if len(args)==2:
				await message.channel.send(f'{args[1]}: {settings[args[1]]}')
				return
			else:
				if not message.author.guild_permissions.manage_messages:
					await message.channel.send('You do not have the permissions to change the settings')
					return
				
				if args[2].lower() == 'true':
					settings[args[1]] = True
					setSetting(message, settings)
					await message.channel.send(f'{args[1]} set to True')
				if args[2].lower() == 'false':
					settings[args[1]] = False
					setSetting(message, settings)
					await message.channel.send(f'{args[1]} set to False')
		else:
			await message.channel.send('Setting not found')


	