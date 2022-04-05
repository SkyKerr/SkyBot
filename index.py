import discord
import json
with open('config.json') as f:
	config = json.load(f)
with open('botInfo.json') as f:
	botInfo = json.load(f)

	
import random as r
import shutil as sh
import shlex
from os.path import exists

version = (f'v{botInfo["currentVersion"]}')
if config['isDev'] :
	version += '-dev'


with open('guildSettings/descriptions.json') as f:
	settingDescriptions = json.load(f)

def guildSettings(message):
	guildID = message.channel.guild.id
	filePath = (f'guildSettings/guilds/{guildID}.json')
	
	if (not exists(filePath)):
		sh.copy('guildSettings/template.json', filePath)
		
	with open(filePath) as f:
		return json.load(f)
		
def changeGuildSettings(message, messageGuildSettings):
	guildID = message.channel.guild.id
	filePath = (f'guildSettings/guilds/{guildID}.json')
	
	with open(filePath, 'w') as f:
		f.write(json.dumps(messageGuildSettings))
	