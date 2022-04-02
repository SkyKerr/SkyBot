import discord
import json
with open('config.json') as f:
	config = json.load(f)
with open('botInfo.json') as f:
	botInfo = json.load(f)
	
import random as r

version = (f'v{botInfo["currentVersion"]}')
if config['isDev'] :
	version += '-dev'

profilePic = 'https://cdn.discordapp.com/attachments/958949821308366879/959661099672809482/profilePicture.png'