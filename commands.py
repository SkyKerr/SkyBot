from index import *

async def userCommands(message, command, args): 
	
	if command == 'version':
		await message.channel.send(f'Skybot {version}')
	
	if command == 'status':
		statusEmbed = discord.Embed(title=(f'Skybot {version}'), url='https://github.com/SkyKerr/SkyBot', description='A japes-based open-source discord bot built in Python', color=0x87CEEB)
		statusEmbed.set_thumbnail(url=profilePic)
		
		await message.channel.send(embed=statusEmbed)
	
async def japeCommands(message, command, args):
	if command == 'ping':
		await message.channel.send('Pong!')
	
	if command == 'rolljonycube':
		await message.channel.send('You rolled the Jony Cube, and it came up as: Jony')
	
	if command == 'echo':
		response = message.content.replace((botInfo['commandChar']+'echo '),'').replace('spoopy', 'spooky')
		await message.channel.send(response)

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
		await message.add_reaction('🚫')
		
	if 'skybot' in message.content.lower():
		await message.add_reaction('👋')