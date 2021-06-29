from dotenv import load_dotenv
import os
import random
import logging

import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

## Main Logger for Discord
## https://discordpy.readthedocs.io/en/latest/logging.html
# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

client = discord.Client()
BOT_MODE = True
SELECTED_CHANNEL_INDEX = 0
SELECTED_CHANNEL = None

@client.event
async def on_ready():
    print(
        'we have logged in as {0.user}'.format(client)
    )
    # print('available channels: {}'.format(client.guilds[0].channels[-1]))

    print("available guilds: ")
    for index, guild in enumerate(client.guilds):
        print("[{}] - {}".format(index , guild))

    selected_index = int(input("input your selected guild to implant bot."))

    print("available channels")
    for index, channel in enumerate(client.guilds[selected_index].channels):
        print("[{}] - {}".format(index , channel))

    selected_channel_index = int(input("input your selected channel to implant bot."))

    selected_channel = client.guilds[selected_index].channels[selected_channel_index]
    await client.guilds[0].channels[-2].send("discord bot online.")

    print(selected_channel)

client.run(TOKEN)

