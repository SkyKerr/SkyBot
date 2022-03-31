import discord
import json
with open('botSettings.json') as f:
	botSettings = json.load(f)

async def userCommands(message, command, args): 
	
	if command == 'ping':
		await message.channel.send('Pong!')
		
	if command == 'version':
		await message.channel.send(f'Skybot Version {botSettings["currentVersion"]} build {botSettings["currentBuild"]}')
	
	if command == 'rolljonycube':
		 await message.channel.send('You rolled the Jony Cube, and it came up as: Jony')
		 
	if command == 'echo':
		await message.channel.send(' '.join(args))
		 

async def messageResponses(message):
	if 'spoopy' in message.content.lower():
		await message.add_reaction('🚫')