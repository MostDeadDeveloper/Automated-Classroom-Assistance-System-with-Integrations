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
    async def recent_announcements(self, ctx):
        await ctx.send('Recent Announcements')
        date = ["June 25", "July 3", "July 5", "July 6", "July 17"]

        login_data = fetch_login_data(ctx.author.id)
        announcements = ["ERD Graded Exercise", "Art App Assumptions of Art", "DAA Final paper", "DAA Final presentation", "OS Final Project"]

        await ctx.send("\n".join("{} - {}".format(x, y) for x, y in zip(date, announcements)))

    @tasks.loop(seconds=5.0)
    async def test_print(self):
        print(self.index)
        self.index += 1

    @commands.command()
    async def create_announcement(self,ctx):

