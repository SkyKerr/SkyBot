## 0.5
- Type-Specific Settings
	- Setting changes must conform to type
- $echo now a user command - all attempted pings now broken
- $status surpasses enableBot, and warns the user if enableBot is False
- guildSettings update automatically
- commandChar now a guildSetting


### 0.4.2
- Added Quiplash

### 0.4.1
- Status message now shows version

## 0.4
- Lots of info added to botInfo.json for consistency
- Guildsettings now responsive to mod permissions
- Jape commands:
	- Many many Marcos
	- Chickenify
	- Jonycube Embed
	- enhancements to $echo
- Bug Fixes


### 0.3.3: 
- Smash Mouth
- Reply commands do not ping user
- Dedicated settings commands file
- Settings responsive to mod permissions

### 0.3.2:
- Bug Fixes and Improvements
- Lots of Marcos (PRs 3 and 4)
- Jonycube Embed (PR 5)
- Chickenify (PR  7)
- Using shlex.split for command arguments
- Added info to botInfo for consistency

### 0.3.1:
- Bug Fixes:
	- $echo can no longer tag @everyone (issue #2)
	- $echo now replys directly to the sender
- Added Marco


## 0.3:
- Status Message embed
- Added Wave Response to 'skybot'
- Separated Regular and Jape Commands
- added guildSettings

### 0.2.2:
- $echo changed to replace 'spoopy'
- Bot waves whenever 'skybot' is seen in a message

### 0.2.1:
- Added status message
- Added Status command with embed

## Version 0.2:
- Added README, removed LICENSE
- Renamed index.py to main
- created index.py as a global file 

## Version 0.1:
- Contains builds 21w14a and 21w14b
- Changed Versioning Method (Strictly follows semantic versioning)

### Build 21w14b:
*Bumped 31 Mar 2022*
- added botInfo file (Not Ignored)
- pycache and .nova folders ignored
- jonycube and echo commands
- added Changelog.md
- moved all commands and responses to commands.py

### Build 21w14a:
*Bumped 30 Mar 2022*
- Bot commands
- config file (Ignored in Repo for security -- contains bot token)
- Message Reactions