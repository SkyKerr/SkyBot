from index import *
with open('guildSettings/descriptions.json') as f:
	settingDescriptions = json.load(f)	

# Note: Before v0.5 there is no way to add new settings to existing guilds. For testing in v0.5pre, guild settings *for the testing guild only* should be deleted so that they can be reloaded.
def guildSettings(message):
	guildID = message.channel.guild.id
	filePath = (f'guildSettings/guilds/{guildID}.json')
	templateFilePath = (f'guildSettings/template.json')
	
	if (not exists(filePath)):
		sh.copy('guildSettings/template.json', filePath)
	
	with open(templateFilePath) as f:
		templateSettings = json.load(f)
	with open(filePath) as f:
		settings = json.load(f)
	
	for setting in templateSettings:
		if setting not in settings:
			sh.copy(templateFilePath, filePath)
			with open(filePath) as f:
				settings = json.load(f)
			break
	
	return settings

async def settingsCommands(message, settings):
	if not message.content.startswith(botInfo['commandChar']):
		return
	args = message.content.lstrip(botInfo['commandChar']).split(' ')

	# Status command
	if args[0] == 'status':
		statusEmbed = discord.Embed(title=(f'Skybot {version}'), url=botInfo['githubLink'], description=botInfo['description'], color=0x87CEEB)
		if settings['enableBot'] == False:
			statusEmbed.add_field(name='Caution', value='The bot is currently disabled. To re-enable, type `$settings enableBot True` with moderator permissions')
		
		statusEmbed.set_thumbnail(url=botInfo['profilePic'])
		
		await message.channel.send(embed=statusEmbed)

	# All settings options below
	if(args[0].lower() == 'settings'): # Call settings - Settings embed
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
		else: # There are 3 arguments given
			setting = args[1]
			input = args[2].lower()
			
			if not message.author.guild_permissions.manage_messages: # Non-moderator users
				await message.channel.send('You do not have the permissions to change the settings')
				return
				
			# Test for input type, typecasting
			try:
				settingType = settingDescriptions[setting]['type']
				if settingType == 'bool':
					if input == 'true':
						input = True
					elif input == 'false':
						input = False
					else:
						raise ValueError('input is not True or False')
				if settingType == 'char':
					if len(input) != 1:
						raise ValueError('input is not a single character')
				# No necessary test for string
				if settingType == 'int':
					input = int(input)
			except ValueError as error:
				await message.channel.send(f'ValueError: {error}')
				return
			
			# Checks passed
			settings[setting] = input
			# Write the change to the settings file
			with open((f'guildSettings/guilds/{message.channel.guild.id}.json'), 'w') as f:
				f.write(json.dumps(settings))
			await message.channel.send(f'{setting} set to {input}')
			
			