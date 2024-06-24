# -*- coding: utf-8 -*-
from utils.client import BotPool

pool = BotPool()

pool.setup()

import discord
from discord.ext import commands
client = discord.Client

@client.event
async def on_ready():
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.listening, name='To Music'))
print('We have logged in as {0.user}'.format(client)) 
