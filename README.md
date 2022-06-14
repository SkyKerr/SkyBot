The SkyBot is a free and open source discord bot. The main repository ("repo") is owned by Skyler Kerr and can be found at [github.com/SkyKerr/SkyBot](http://github.com/SkyKerr/SkyBot). Contributions are welcome and can be made there.

Use of the bot using the code from the repo requires the creation of a configuration file 'config.json' containing the private key of a discord bot, which can be created at the Discord Developer Portal ([https://discord.com/developers/docs/intro](https://discord.com/developers/docs/intro)). Run using `python .`

A Changelog for all versions can be found at ~/changelog.md .




# Commands:
*all commands preceeded by the set command character, defaults to $*

Syntax: `<required parameter>`, `[optional parameter]`

`$status` : Shows the bot version and github link

`$settings` : shows the list of guild settings

`$settings [setting]` : Shows the current value of the given setting

`$settings [setting] [value]` : sets the setting to the given value. Manage messages Permissions required. Passed value must follow the given type for the setting: bool, string, int, or char.

`$version` : shows the current bot version

`$echo <message...>` : replys with the same message and pings the author

`$help` : gives the link to the github

`$send <channel> "<message>"` : Sends the message to the given channel. Manage messages permission required.

`$reply <channel> <message ID> "<message>" [ping true/false]` : Replies to the given message. Ping defaults to false.


## All Below are "Jape Command" and can be disabled by setting `allowJapeCommands` to false

`$ping` : pong

`$rolljonycube` : Rolls the jony cube. Added by Justin Hamilton.

`$quip` : sends a quip from the Jackbox game "Quiplash"

`$chickenify <string...>` : tUrNs ThE sTRiNg InTo cHiCkEn TeXt

`$marco` : Polo! or Arment! or one of many many marcos




# Message Responses: Can be disabled by setting `allowMessageResponses` to false

- Responds to 'Spoopy' with 🚫
- Responds to ‘Skybot’ with 👋
- Responds to ‘some’ with ‘BODY’
- Responds with 👀 if Skybot is pinged in the message
- Unflips flipped tables
- Responds to API with a 🐝

