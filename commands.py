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
		await message.reply(response, mention_author=False)
	
	def chickenify(string):
		# im a tryhard ok deal with it -- Justin Hamilton
		return ''.join([string[i].upper() if i%2 == 1 else string[i].lower() for i in range(len(string))])
	
	if command == 'chickenify':
		response = chickenify(message.content.replace((botInfo['commandChar']+'chickenify '),''))
		await message.reply(response, mention_author=False)
		
	if command == 'marco':
		await message.channel.send(r.choice(botInfo['marcos']))
	
async def messageResponses(message):
	if 'spoopy' in message.content.lower():
		await message.add_reaction(botInfo['reactions']['no'])
		
	if 'skybot' in message.content.lower():
		await message.add_reaction(botInfo['reactions']['wave'])

	if message.content.lower() == 'some':
		await message.reply("BODY", mention_author=False)