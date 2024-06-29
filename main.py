# from dotenv import load_dotenv
import os
import discord


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


if __name__ == '__main__':
    print(os.getenv("TOKEN"))

client.run(os.getenv("TOKEN"))