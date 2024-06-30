import discord
import constants

status_messages = { 
    discord.status.online: "Run...",
    discord.status.offline: "The coast is clear",
    discord.status.idle: "Jim is idle",
    discord.status.dnd: "Jim is busy",
    discord.status.invisible: "Be wary of your surroundings",
}

async def the_alarm(before, after):
    if before.status != after.status and after.id == constants.JIM_ID:
        channel = discord.utils.get(after.guild.channels, name='general')
        if channel is not None and after.status in status_messages:
            await channel.send(status_messages[after.status])
        
        