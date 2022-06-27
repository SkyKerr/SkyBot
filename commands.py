from index import *

# User commands, called from ./__main__.py
async def userCommands(message, command, args, settings): 
	
	# shows the current bot version
	if command == 'version':
		await message.channel.send(f'Skybot {version}')
	
	# Echos the user input, and tags the message author
	if command == 'echo':
		author = message.author.id
		
		# Discord syntax for message author tag
		authorTag = (f'<@{author}>')
		echoResponse = message.content.replace((settings['commandChar']+'echo'),'').replace('spoopy', 'spooky').replace('@','@​')
		response = authorTag + echoResponse
		
		await message.channel.send(response)
	
	# Link to github for README
	if command == 'help':
		await message.channel.send(f'see the README at <{botInfo["githubLink"]}>')
	
	# $send <channel> "<message>"
	if command == 'send':
		# Check permission
		if not message.author.guild_permissions.manage_messages:
			await message.channel.send('Error: Insufficient Permissions')
			return
		
		# Check number of required parameters
		if len(args) < 2:
			await message.channel.send('Error: Missing required parameters')
			return
	
		try: 
			# get_channel() returns None if channel is not found
			sendChan = client.get_channel(int(args[0].replace('<#','').replace('>','')))
		except: 
			# Catch an Int conversion error
			sendChan = None
		
		# Handle exception
		if sendChan == None:
			await message.channel.send('Error: Channel not found')
			return
		
		# send the message to the channel	
		await sendChan.send(args[1])
	
	# $reply <channel> <message ID> "<message>" [ping True/False]	
	if command == 'reply':
		# check permission
		if not message.author.guild_permissions.manage_messages:
			await message.channel.send('Erorr: Insufficient Permissions')
			return
		
		# number of required parameters
		if len(args) < 3: 
			await message.channel.send('Error: Missing required parameters')
			return
		
		# param 0, channel (taken from $send)
		try: 
			# get_channel() returns None if channel isn't found
			sendChan = client.get_channel(int(args[0].replace('<#','').replace('>','')))
		except: 
			# Catch int conversion error
			sendChan = None
			
		# Handle exception
		if sendChan == None:
			await message.channel.send('Error: Channel not found')
			return
		
		# Param 1, Message ID	
		try:
			# fetch_message() returns None if message can't be found
			replyTo = await sendChan.fetch_message(int(args[1]))
		except:
			# Int conversion error
			replyTo = None
		
		if replyTo == None:
			await message.channel.send('Error: Message not found')
			
		# Param 3, Ping true/false, optional
		if len(args) == 3:
			# if there is no arg given, set to false
			ping = False
		elif args[3] == 'true':
			# set to true
			ping = True
		else:
			# if anything else is passed for this arg, set to false
			ping = False
		
		# Final message send
		await replyTo.reply(args[2], mention_author=ping)
	
# Jape commands, called from ./__main__.py	
async def japeCommands(message, command, args, settings):
	# pong!
	if command == 'ping':
		await message.channel.send('Pong!')
	
	# roll the jonycube
	if command == 'rolljonycube':
		# create the Embed from botInfo
		await message.channel.send(embed=discord.Embed(title=botInfo['jonyCube']['title'], description=botInfo['jonyCube']['description'], color=0x3c2821).set_thumbnail(url=botInfo['jonyCube']['gif']))

	# Send a random quip
	if command == 'quip':
		res = get("https://4fjqh2uxrwehpglicenre7qrny0sduge.lambda-url.us-west-2.on.aws")
		await message.channel.send(res.text)

	# Chickenify function
	def chickenify(string):
		# im a tryhard ok deal with it -- Justin Hamilton
		return ''.join([string[i].upper() if i%2 == 1 else string[i].lower() for i in range(len(string))])
	
	
	if command == 'chickenify':
		# chickenify the message
		response = chickenify(message.content.replace((settings['commandChar']+'chickenify '),''))
		await message.reply(response, mention_author=False)
		
	if command == 'marco':
		# responds with a random marco (Credit: Whatsie)
		await message.channel.send(r.choice(botInfo['marcos']))
	
# Unprompted message responses, called from ./__main__.py
async def messageResponses(message):
	# The bot does not like spoopy
	if 'spoopy' in message.content.lower():
		await message.add_reaction(botInfo['reactions']['no'])
		
	if 'skybot' in message.content.lower():
		await message.add_reaction(botInfo['reactions']['wave'])

	if message.content.lower() == 'some':
		await message.reply("BODY", mention_author=False)
		
	# Triggers if the bot is pinged (in message or reply)
	if client.user in message.mentions:
		await message.channel.send(botInfo['reactions']['eyes'])
	
	# when a user sends `/tableflip`
	if botInfo['flippedTable'] in message.content.lower():
		unflip = botInfo['unflippedTable']
		# Pick a random response
		response = r.choice(botInfo['tableResponses'])
		await message.reply(f'{unflip}\n{response}')
	
	# il mondo ha bisogno di più api
	if 'API' in message.content:
		await message.add_reaction(botInfo['reactions']['bee'])
	
