import discord
import constants

async def on_presence_update(before, after):
    if before.status != after.status and after.status == discord.Status.online and after.id == constants.JIM_ID:
        channel = discord.utils.get(after.guild.channels, name='general')
        if channel is not None:
            await channel.send("Winter is coming")
    if before.status != after.status and after.status == discord.Status.offline and after.id == constants.JIM_ID:
        channel = discord.utils.get(after.guild.channels, name='general')
        if channel is not None:
            await channel.send("The coast is clear")