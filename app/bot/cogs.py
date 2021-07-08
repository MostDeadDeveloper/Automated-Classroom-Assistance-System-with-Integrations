import os
import logging
import requests
import json
from dotenv import load_dotenv

from discord.ext import commands, tasks
import discord

from utils import fetch_login_data

class Announcements(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.last_member = None

        self.index = 0
        self.test_print.start()

    def cog_unload(self):
        self.test_print.cancel()

    @commands.command()
    async def recent_announcements(self, ctx, arg):
        login_data = fetch_login_data(ctx.author.id)

        schedule = login_data.json()
        sched_str = json.dumps(schedule)
        data = json.loads(sched_str)

        url = 'http://superepicguysuper.pythonanywhere.com/api/announcements/list/account/{}/count/{}'.format(
            data['account_id'],
            arg,
        )
        print(url)

        response = requests.get(url, timeout=5)

        schedule = response.json()
        sched_str = json.dumps(schedule)
        data = json.loads(sched_str)

        values = []
        for value in data:
            values.append('{} - {}'.format(value['scheduled_date'], value['content']))

        await ctx.send('Recent Announcements Posted:\n'.join(values))

    @tasks.loop(seconds=5.0)
    async def test_print(self):
        print(self.index)
        self.index += 1

    # @commands.command()
    # async def create_announcement(self,ctx):

