from dotenv import load_dotenv
import os
import random
import logging
from discord.ext import commands

import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USERID = os.getenv('DISCORD_USER')

## Main Logger for Discord
## https://discordpy.readthedocs.io/en/latest/logging.html
#logger = logging.getLogger('discord')
#logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename='discord.txt', encoding='utf-8', mode='w')
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)

client = discord.Client()
client = commands.Bot(command_prefix = '!')
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

@client.command()
async def list_all_subjects(ctx):
    await ctx.send('Subjects and Schedule')
    schedule = ["T/F 11:30AM-01:30PM/10:30AM-01:30PM", "T/F 07:30AM-10:30AM/07:30AM-09:30AM", "W 03:00PM-06:00PM", "W 09:00AM-12:00PM", "S 10:00AM-12:00PM"]
    subjects = ["Information Management", "Operating Systems", "CS Free Elective 2", "Art Appreciation", "Team Sports"]

    await ctx.send("\n".join("{} - {}".format(x, y) for x, y in zip(schedule, subjects)))

client.run('ODU4MzAxNDUxODc1Nzc4NTgy.YNcJhA.Xb1rM6mSyzjdQR1UqDWb3oyFtFQ')