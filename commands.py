import discord
import json
import random as r
with open('botInfo.json') as f:
	botInfo = json.load(f)

async def userCommands(message, command, args): 
	
	if command == 'ping':
		await message.channel.send('Pong!')
		
	if command == 'version':
		await message.channel.send(f'Skybot Version {botInfo["currentVersion"]} build {botInfo["currentBuild"]}')
	
	if command == 'rolljonycube':
		 await message.channel.send('You rolled the Jony Cube, and it came up as: Jony')
		 
	if command == 'echo':
		await message.channel.send(' '.join(args).replace('spoopy', 'spooky'))
			
		 

async def messageResponses(message):
	if 'spoopy' in message.content.lower():
		await message.add_reaction('🚫')