import constants
import discord

async def message_sent(client, message):
    # Avoid bot replying to itself
    if message.author == client.user:
        return

    if message.content.lower().startswith("is it safe"):
        if isJimOnline(message):
            await message.channel.send("There is nowhere to run, nowhere to hide!")
        else: 
            await message.channel.send("You are safe, for now...")

def isJimOnline(message):
    return message.guild.get_member(constants.JIM_ID).status != discord.Status.offline