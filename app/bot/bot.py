from dotenv import load_dotenv
import os
import random
import logging

import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USERID = os.getenv('DISCORD_USER')

## Main Logger for Discord
## https://discordpy.readthedocs.io/en/latest/logging.html
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()
BOT_MODE = True
SELECTED_CHANNEL_INDEX = 0
SELECTED_CHANNEL = None


client.run(TOKEN)

