import constants

async def message_sent(client, message):
    # Avoid bot replying to itself
    if message.author == client.user:
        return

    if message.author.id == constants.MY_ID:
        await message.channel.send("You sent a message")
    else:
        await message.channel.send("Received a message")
