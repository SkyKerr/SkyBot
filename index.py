import discord
import json
with open('config.json') as f:
	config = json.load(f)
with open('botInfo.json') as f:
	botInfo = json.load(f)
	
import random as r

statusMessage = (f'Skybot Version {botInfo["currentVersion"]}')
version = (f'v{botInfo["currentVersion"]}')
