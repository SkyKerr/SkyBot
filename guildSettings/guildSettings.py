from index import *
with open('guildSettings/descriptions.json') as f:
	settingDescriptions = json.load(f)	

# Note: As of v0.4.1 there is no way to add new settings to existing guilds. For testing in v0.5pre, guild settings *for the testing guild only* should be deleted so that they can be reloaded.
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
	args = message.content.lstrip(botInfo['commandChar']).split(' ')

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
				name=(f'{setting}'),
				value=(f'{settingDescriptions[setting]["description"]}\n**Value:** {settings[setting]}\n**Type:** {settingDescriptions[setting]["type"]}'),
				inline=False)
		
			await message.channel.send(embed=messageEmbed)
			return
		
		if args[1] not in settings:
			await message.channel.send('Setting not found')
			return
		
		# Change settings commands
		if len(args)==2:
			await message.channel.send(f'{args[1]}: {settings[args[1]]}')
			return
		else:
			if not goodType(args[1], args[2]):
				await message.channel.send('Error: Input does not match setting type')
				return
			
			if not message.author.guild_permissions.manage_messages:
				await message.channel.send('You do not have the permissions to change the settings')
				return
			
			if settingDescriptions[args[1]]['type'] == 'bool':
				if args[2].lower() == 'true':
					settings[args[1]] = True
				if args[2].lower() == 'false':
					settings[args[1]] = False
			if settingDescriptions[args[1]]['type'] == 'int':
				settings[args[1]] = int(args[2])
			else:
				settings[args[1]] = args[2]
			
			setSetting(message, settings)
			await message.channel.send(f'{args[1]} set to {args[2]}')

def goodType(setting, input):
	settingType = settingDescriptions[setting]['type']
	
	if settingType == 'bool':
		if input.lower() == ('true' or 'false'):
			return True
		else:
			return False
	
	if settingType == 'char':
		if len(input) != 1:
			return False
		if input in settingDescriptions['forbiddenCharacters']: # This is for all the amazing testers who do whatever they can to break my bot
			return False
		return True
	
	if settingType == 'str': 
		for char in input.split(''):
			if char in settingDescriptions['forbiddenCharacters']:
				return False
		return True
	
	if settingType == 'int':
		try:
			int(input)
		except ValueError:
			return False
		return True
		
	