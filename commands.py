from index import *


async def userCommands(message, command, args, settings):

    if command == "version":
        await message.channel.send(f"Skybot {version}")

    if command == "echo":
        author = message.author.id

        authorTag = f"<@{author}>"
        echoResponse = (
            message.content.replace((settings["commandChar"] + "echo"), "")
            .replace("spoopy", "spooky")
            .replace("@", "@​")
        )
        response = authorTag + echoResponse

        await message.channel.send(response)

    if command == "help":
        await message.channel.send(f'see the README at <{botInfo["githubLink"]}>')

    if command == "send":
        if not message.author.guild_permissions.manage_messages:
            await message.channel.send("Error: Insufficient Permissions")
            return

        if len(args) < 2:
            return

        try:
            sendChan = client.get_channel(
                int(args[0].replace("<#", "").replace(">", ""))
            )
        except:
            sendChan = None

        if sendChan == None:
            await message.channel.send("Error: Channel not found")
            return

        await sendChan.send(args[1])

    if command == "reply":
        if not message.author.guild_permissions.manage_messages:
            await message.channel.send("Erorr: Insufficient Permissions")
            return

        if len(args) < 3:
            await message.channel.send("Error: Missing required parameters")
            return

        # param 0, channel
        try:
            sendChan = client.get_channel(
                int(args[0].replace("<#", "").replace(">", ""))
            )
        except:
            sendChan = None

        if sendChan == None:
            await message.channel.send("Error: Channel not found")
            return

        # Param 1, Message ID
        try:
            replyTo = await sendChan.fetch_message(int(args[1]))
        except:
            replyTo = None

        if replyTo == None:
            await message.channel.send("Error: Message not found")

        # Param 3, Ping true/false, optional
        if len(args) == 3:
            ping = False
        elif args[3] == "true":
            ping = True
        else:
            ping = False

        # Final message send
        await replyTo.reply(args[2], mention_author=ping)


async def japeCommands(message, command, args, settings):
    if command == "ping":
        await message.channel.send("Pong!")

    if command == "rolljonycube":
        jonyEmbed = discord.Embed(
            title=botInfo["jonyCube"]["title"],
            description=botInfo["jonyCube"]["description"],
            color=0x3C2821,
        )
        jonyEmbed.set_thumbnail(url=botInfo["jonyCube"]["gif"])
        await message.channel.send(embed=jonyEmbed)

    if command == "quip":
        res = get(
            "https://4fjqh2uxrwehpglicenre7qrny0sduge.lambda-url.us-west-2.on.aws"
        )
        await message.channel.send(res.text)

    def chickenify(string):
        # im a tryhard ok deal with it -- Justin Hamilton
        return "".join(
            [
                string[i].upper() if i % 2 == 1 else string[i].lower()
                for i in range(len(string))
            ]
        )

    if command == "chickenify":
        response = chickenify(
            message.content.replace((botInfo["commandChar"] + "chickenify "), "")
        )
        await message.reply(response, mention_author=False)

    if command == "marco":
        await message.channel.send(r.choice(botInfo["marcos"]))


async def messageResponses(message):
    if "spoopy" in message.content.lower():
        await message.add_reaction(botInfo["reactions"]["no"])

    if "skybot" in message.content.lower():
        await message.add_reaction(botInfo["reactions"]["wave"])

    if message.content.lower() == "some":
        await message.reply("BODY", mention_author=False)

    if client.user in message.mentions:
        await message.channel.send(botInfo["reactions"]["eyes"])

    if botInfo["flippedTable"] in message.content.lower():
        unflip = botInfo["unflippedTable"]
        response = r.choice(botInfo["tableResponses"])
        await message.reply(unflip + "\n" + response)

    if "API" in message.content:
        await message.add_reaction(botInfo["reactions"]["bee"])

    match = re.match(
        "^i(['‘’]?)m(( (\S)+){1,5})$",
        message.content.lower().replace("*", "").replace("_", ""),
    )
    if not (match == None):
        await message.reply(
            "hi " + match.group(2)[1:] + " i'm dad", mention_author=False
        )
