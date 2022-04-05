from index import *

async def userCommands(message, command, args): 
	
	if command == 'version':
		await message.channel.send(f'Skybot {version}')
	
	if command == 'status':
		statusEmbed = discord.Embed(title=(f'Skybot {version}'), url=botInfo['githubLink'], description=botInfo['description'], color=0x87CEEB)
		statusEmbed.set_thumbnail(url=botInfo['profilePic'])
		
		await message.channel.send(embed=statusEmbed)
	
async def japeCommands(message, command, args):
	if command == 'ping':
		await message.channel.send('Pong!')
	
	if command == 'rolljonycube':
		jonyEmbed = discord.Embed(title=botInfo['jonyCube']['title'], description=botInfo['jonyCube']['description'], color=0x3c2821)
		jonyEmbed.set_thumbnail(url=botInfo['jonyCube']['gif'])
		await message.channel.send(embed=jonyEmbed)
	
	if command == 'echo':
		response = message.content.replace((botInfo['commandChar']+'echo '),'').replace('spoopy', 'spooky')
		if '@everyone' in message.content.lower():
			response = 'Nice Try.'
		await message.reply(response)
		
	if command == 'marco':
		await message.channel.send(r.choice(botInfo['marcos']))

async def guildSettingsCommands(message, messageGuildSettings):
	args = message.content.replace(botInfo['commandChar'], "").split(' ')
	
	if(args[0].lower() != 'settings'):
		return
	
	# settings embed
	if len(args)==1:
		messageEmbed = discord.Embed(title=(f'Server Settings for {message.channel.guild}'))
		
		for setting in messageGuildSettings:
			messageEmbed.add_field(
			name=(f'{setting}: {messageGuildSettings[setting]}'),
			value=(f'{settingDescriptions[setting]}'),
			inline=False)
		
		await message.channel.send(embed=messageEmbed)
		return
		
	# Change settings commands
	if args[1] in messageGuildSettings:
		if len(args)==2:
			await message.channel.send(f'{args[1]}: {messageGuildSettings[args[1]]}')
			return
		else:
			if args[2].lower() == 'true':
				messageGuildSettings[args[1]] = True
				changeGuildSettings(message, messageGuildSettings)
				await message.channel.send(f'{args[1]} set to True')
			if args[2].lower() == 'false':
				messageGuildSettings[args[1]] = False
				changeGuildSettings(message, messageGuildSettings)
				await message.channel.send(f'{args[1]} set to False')
	else:
		await message.channel.send('Setting not found')
	
async def messageResponses(message):
	if 'spoopy' in message.content.lower():
		await message.add_reaction(botInfo['reactions']['no'])
		
	if 'skybot' in message.content.lower():
		await message.add_reaction(botInfo['reactions']['wave'])
