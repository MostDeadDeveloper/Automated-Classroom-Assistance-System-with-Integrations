import os
import logging
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

from discord.ext import commands
import discord

from cogs import Announcements
from utils import fetch_login_data

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
        a = i['subject']
        b = i['start_time'] + " - " + i['end_time']
        subjlist.append("```\n{}: {}```".format(a, b))
    await ctx.send("```SUBJECTS AND SCHEDULE```" + ''.join(subjlist))

@client.command()
async def list_all_subjects_today(ctx):
    try:
        response = requests.get('http://superepicguysuper.pythonanywhere.com/api/subjects/student/1/today', timeout=5)
        response.raise_for_status()
        login_data = fetch_login_data(ctx.author.id)
        await ctx.send(login_data)

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
        a = i['subject']
        b = i['start_time'] + " - " + i['end_time']
        subjlist.append("```{}: {}```".format(a, b))
    await ctx.send("```SUBJECTS AND SCHEDULE For Today```" + ''.join(subjlist))

# register the registrations cog
client.add_cog(Announcements(client))

@client.command()
async def enlist_my_notes(ctx):
    await ctx.send('Type the name of the subject:')
    subjectName = await client.wait_for('message')
    strsubjectName = subjectName.content

    await ctx.send('Type your notes for {}:'.format(strsubjectName))
    notes = await client.wait_for('message')
    date = datetime.now()
    strnotes = notes.content

    await ctx.send('Notes for {} saved!'.format(strsubjectName))
    print(strsubjectName)
    print(strnotes)
    print(date)

    data = {'subject': strsubjectName,
            'notes': strnotes,
            'date_created':date}

    response = requests.post("URL", data)
    print(response.text)

@client.command()
async def list_all_notes_recent (ctx, arg):

    login_data = fetch_login_data(ctx.author.id)

    schedule = login_data.json()
    sched_str = json.dumps(schedule)
    data = json.loads(sched_str)

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
        c = i['subject_id']
        a = i['subject']
        b = i['start_time'] + " - " + i['end_time']
        subjlist.append("```\n{} - {}: {}```".format(c ,a, b))
    await ctx.send("```SUBJECTS AND SCHEDULE```" + ''.join(subjlist))

    # await ctx.send('Type the id of the subject:')
    subjectName = await client.wait_for('message')
    subj_id = subjectName.content
    print(subj_id)

    url = 'http://superepicguysuper.pythonanywhere.com/api/announcements/notes/list/{}/subject/{}/count/{}'.format(
        data['account_id'],
        subj_id,
        arg,
    )
    print (url)

    data_response = requests.get(url)
    json_response = json.dumps(data_response.json())
    notes_data = json.loads(json_response)

    values = []
    for value in notes_data:
        values.append('{} - {}'.format(value['created_time'], value['content']))

    await ctx.send('\n'.join(values))


client.run(TOKEN)
