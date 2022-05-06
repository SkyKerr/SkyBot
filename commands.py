from index import *

async def userCommands(message, command, args): 
	
	if command == 'version':
		await message.channel.send(f'Skybot {version}')
		
	if command == 'echo':
		author = message.author.id
		
		authorTag = (f'<@{author}>')
		echoResponse = message.content.replace((settings['commandChar']+'echo'),'').replace('spoopy', 'spooky').replace('@','@​')
		response = authorTag + echoResponse
		
		await message.channel.send(response)
	
async def japeCommands(message, command, args):
	if command == 'ping':
		await message.channel.send('Pong!')
	
	if command == 'rolljonycube':
		jonyEmbed = discord.Embed(title=botInfo['jonyCube']['title'], description=botInfo['jonyCube']['description'], color=0x3c2821)
		jonyEmbed.set_thumbnail(url=botInfo['jonyCube']['gif'])
		await message.channel.send(embed=jonyEmbed)

	if command == 'quip':
		res = get("https://4fjqh2uxrwehpglicenre7qrny0sduge.lambda-url.us-west-2.on.aws")
		await message.channel.send(res.text)

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