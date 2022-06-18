from index import *
# get Descriptions
with open('guildSettings/descriptions.json') as f:
	settingDescriptions = json.load(f)	

# (Note: the API calls a "Guild" what most people call a "Server" in discord)

# Function to load, reload, and update settings
def guildSettings(message):
	# create filepath with Guild ID
	guildID = message.channel.guild.id
	filePath = (f'guildSettings/guilds/{guildID}.json')
	templateFilePath = ('guildSettings/template.json')
	
	# if the guildsettings file for the guild does not exist, create it
	if (not exists(filePath)):
		sh.copy('guildSettings/template.json', filePath)
	
	# load the settings and the template settings
	with open(templateFilePath) as f:
		templateSettings = json.load(f)
	with open(filePath) as f:
		settings = json.load(f)
	
	# SETTINGS UPDATES: make sure that each template setting is also seen in the settings file. If its not, re-load the settings file. 
	for setting in templateSettings:
		if setting not in settings:
			sh.copy(templateFilePath, filePath)
			with open(filePath) as f:
				settings = json.load(f)
			break
	
	# return the settings
	return settings

# $settings and $status commands
async def settingsCommands(message, settings):
	# Check for command character
	if not message.content.startswith(settings['commandChar']):
		return
	# Strip off command character, split into args
	args = message.content.lstrip(settings['commandChar']).split(' ')

	# Status command
	if args[0] == 'status':
		# Create status embed
		statusEmbed = discord.Embed(title=(f'Skybot {version}'), url=botInfo['githubLink'], description=botInfo['description'], color=0x87CEEB)
		# If the enableBot setting is False, add a warning
		if settings['enableBot'] == False:
			statusEmbed.add_field(name='Caution', value='The bot is currently disabled. To re-enable, type `$settings enableBot True` with moderator permissions')
		
		# Add skybot's profile pic as the thumbnail
		statusEmbed.set_thumbnail(url=botInfo['profilePic'])
		
		# Send embed
		await message.channel.send(embed=statusEmbed)

	# $settings [setting] [True/False]
	if(args[0].lower() == 'settings'):
		# No setting given: show setting embed 
		if len(args)==1:
			# Create embed
			messageEmbed = discord.Embed(title=(f'Server Settings for {message.channel.guild}'))
		
			# for each setting in the list, create a new field
			for setting in settings:
				messageEmbed.add_field(
				name=(f'{setting}'),
				value=(f'{settingDescriptions[setting]["description"]}\n**Value:** {settings[setting]}\n**Type:** {settingDescriptions[setting]["type"]}'),
				inline=False)
			
			# send embed and return
			await message.channel.send(embed=messageEmbed)
			return
		
		# If a setting is given that doesn't exist:
		if args[1] not in settings:
			await message.channel.send('Setting not found')
			return
		
		# Give current value of the given setting
		if len(args)==2:
			await message.channel.send(f'{args[1]}: {settings[args[1]]}')
			return
			
		# Change setting
		if len(args)==3: 
			setting = args[1]
			input = args[2].lower()
			
			# Check permissions
			if not message.author.guild_permissions.manage_messages:
				await message.channel.send('You do not have the permissions to change the settings')
				return
				
			# Test for correct input type and typecast
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
			# Handle exception
			except ValueError as error:
				await message.channel.send(f'ValueError: {error}')
				return
			
			# set the setting to the value
			settings[setting] = input
			# Write the change to the settings file
			with open((f'guildSettings/guilds/{message.channel.guild.id}.json'), 'w') as f:
				f.write(json.dumps(settings))
			await message.channel.send(f'{setting} set to {input}')
			
			