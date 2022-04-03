from index import *

async def userCommands(message, command, args): 
	
	if command == 'ping':
		await message.channel.send('Pong!')
		
	if command == 'version':
		await message.channel.send(f'Skybot {version}')
	
	if command == 'rolljonycube':
		 await message.channel.send('You rolled the Jony Cube, and it came up as: Jony')
		 
	if command == 'echo':
		response = message.content.replace((botInfo['commandChar']+'echo '),'').replace('spoopy', 'spooky')
		await message.channel.send(response)
		
	if command == 'status':
		statusEmbed = discord.Embed(title=(f'Skybot {version}'), url='https://github.com/SkyKerr/SkyBot', description='A japes-based open-source discord bot built in Python', color=0x87CEEB)
		statusEmbed.set_thumbnail(url=profilePic)
		
		await message.channel.send(embed=statusEmbed)
			
		 

async def messageResponses(message):
	if 'spoopy' in message.content.lower():
		await message.add_reaction('🚫')
		
	if 'skybot' in message.content.lower():
		await message.add_reaction('👋')