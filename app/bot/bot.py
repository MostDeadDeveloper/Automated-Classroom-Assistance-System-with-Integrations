import os
import logging
import requests
import json
from discord.ext import commands

from dotenv import load_dotenv
from discord.ext import commands
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

## Main Logger for Discord
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='app/logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix = '!')
BOT_MODE = True
SELECTED_CHANNEL_INDEX = 0
SELECTED_CHANNEL = None

@client.event
async def on_ready():
    print(
        'we have logged in as {0.user}'.format(client)
    )
    # # print('available channels: {}'.format(client.guilds[0].channels[-1]))
    
    # print("available guilds: ")
    # for index, guild in enumerate(client.guilds):
        # print("[{}] - {}".format(index , guild))

    # selected_index = int(input("input your selected guild to implant bot."))

    # print("available channels")
    # for index, channel in enumerate(client.guilds[selected_index].channels):
        # print("[{}] - {}".format(index , channel))

    # selected_channel_index = int(input("input your selected channel to implant bot."))

    # selected_channel = client.guilds[selected_index].channels[selected_channel_index]
    # await client.guilds[0].channels[-2].send("discord bot online.")

    # print(selected_channel)

@client.command()
async def list_all_subjects(ctx):
    try:
        response = requests.get('http://superepicguysuper.pythonanywhere.com/api/subjects/student/1', timeout=5)
        response.raise_for_status()
        print("Successful.")
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

    schedule = response.json()
    sched_str = json.dumps(schedule)
    sched_dict = json.loads(sched_str)

    subjlist = []
    for i in sched_dict: 
        a = i['name']
        b = i['schedules'][0]['start_time'] + " - " + i['schedules'][0]['end_time']
        subjlist.append("```{}: {}```".format(a, b))
    await ctx.send("```SUBJECTS AND SCHEDULE```" + ''.join(subjlist))

@client.command()
async def recent_announcements(ctx):
    await ctx.send('Recent Announcements')
    date = ["June 25", "July 3", "July 5", "July 6", "July 17"]
    announcements = ["ERD Graded Exercise", "Art App Assumptions of Art", "DAA Final paper", "DAA Final presentation", "OS Final Project"]

    await ctx.send("\n".join("{} - {}".format(x, y) for x, y in zip(date, announcements)))

client.run(TOKEN)
