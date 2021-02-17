
import discord
from pathlib import Path
import time
import sys, traceback
import logging
import datetime
import json
import os.path
from discord.ext import commands
from collections.abc import Sequence
import asyncio

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.


bot = commands.Bot(command_prefix=".", owner_id=475304536920031232,intents=intents)




logging.basicConfig(level=logging.INFO)

initial = ["cogs.level","cogs.suggest","cogs.gatekeeper","cogs.help","cogs.fun", "cogs.roles", "jishaku", "cogs.peep", "cogs.events", "cogs.mod", "cogs.veri", "cogs.custom", "cogs.staff","cogs.profiles"]

if __name__ == "__main__":
    for extent in initial:
        try:
            bot.load_extension(extent)
        except Exception as e:
            print(f'Failed to load extension {extent}.', file=sys.stderr)
            traceback.print_exc()




#--------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
#--------------------------------------------------
@bot.command()
@commands.is_owner()
async def leave(ctx):
    server = bot.get_guild(ctx.guild.id)
    await server.leave()

@bot.command()
@commands.is_owner()
async def avs(ctx, number):
    with open(f"/home/shadbot/pfps/peep_{number}.jpg", "rb") as fp:
        await bot.user.edit(avatar=fp.read())
    embed = discord.Embed(title="New Profile For {} Bot".format(bot.user.name))
    pfp = bot.user.avatar_url
    embed.set_image(url=str(pfp))
    await ctx.send(embed=embed)

@commands.cooldown(1, 5.0, type=commands.BucketType.default)
@bot.command()
@commands.is_owner()
async def game(ctx, *, game: str):
    await bot.change_presence(activity=discord.Game(name=game, type=1))

@commands.cooldown(1, 5.0, type=commands.BucketType.default)
@bot.command()
@commands.is_owner()
async def rename(ctx, *, name: str):
    await bot.user.edit(username=name)



























@bot.command()
async def Ping(ctx):
    await ctx.send('Pong!')



bot.run("NTMwOTQ1ODMwMDA2MjkyNDgw.D0l0HA.paZNBNSvNc7tOs_s3NRnmMvR630")
