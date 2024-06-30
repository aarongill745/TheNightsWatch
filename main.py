import discord
import constants

from events.on_message import message_sent
from events.on_presence_update import the_alarm

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True

class DiscordBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def on_ready(self):
        print("Ready")
    
    async def on_message(self, message):
        await message_sent.message_sent(self, message) 
        
    async def on_presence_update(self, before, after):
        await the_alarm.the_alarm(before, after)

client = DiscordBot(intents=intents)
client.run(constants.TOKEN)
