
import logging

import os.path
import discord
from discord.ext import commands

import asyncio
import random
import typing
import os
import discord
from pathlib import Path
from discord.ext import commands
import time
import sys, traceback
from discord.ext import tasks
import mysql.connector


def pull(*args):
    
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="shad",
                    passwd="shadii",
                    database="finesse",)

    dbcursor = mydb.cursor(buffered=True)
    dbcursor.execute(*args)
    
    results = dbcursor.fetchall()
    mydb.commit()
    dbcursor.close
    return results

def push(*args):
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="shad",
                    passwd="shadii",
                    database="finesse",
                    )
    dbcursor = mydb.cursor(buffered=False)
    dbcursor.execute(*args)
    
   
    mydb.commit()
    dbcursor.close()
    mydb.close()
    return None





class bobross(commands.Cog):

    def __init__(self, bot):
        
        self.bot = bot
     

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id != 534050853477285888:
            return
        channel_list = pull("SELECT * FROM notext") # SQL Query to get all channel ids that are in the blacklist
        for cid in channel_list: 
            if str(message.channel.id) == cid[0]:
                if len(message.attachments) == 0:
                    await message.delete()
                    resp_embed = discord.Embed(title="Finesse Automoderator",
                                            description=f"You Cant Post Messages In {message.channel.mention}. Sorry For Any Inconvenience. <3",
                                            timestamp=message.created_at,
                                            color=discord.Color.red())
                    await message.author.send(embed=resp_embed)
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def channeladd(self, ctx, channel_id: int):
        channel_list = [x.id for x in ctx.guild.channels] # Gets all channel ids in the guild where the command came from
        if channel_id not in channel_list:
            resp_embed = discord.Embed(title="Finesse Error",
                                    description=f"this is not a channel ID from {ctx.guild.name}, please retry again.",
                                    timestamp=ctx.message.created_at,
                                    color=discord.Color.red())
            await ctx.author.send(embed=resp_embed)
            
            return
        push(f"INSERT INTO notext VALUES({str(channel_id)})")
        resp_embed = discord.Embed(title="Finesse Error",
                                description=f"<#{channel_id}> has been added to the blacklist database, thank you for your contribution.",
                                timestamp=ctx.message.created_at,
                                color=discord.Color.teal())
        await ctx.author.send(embed=resp_embed)
       

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def channelremove(self, ctx, channel_id: int):
        cidlist = []
        chan_list = pull("select * from notext")
        for cid in chan_list:
            cidlist.append(cid[0])
        if str(channel_id) not in cidlist: # If the channel isnt in the database
            resp_embed = discord.Embed(title="Finesse Error",
                                    description=f"this is not a channel ID from {ctx.guild.name}, please retry again.",
                                    timestamp=ctx.message.created_at,
                                    color=discord.Color.red())
            await ctx.author.send(embed=resp_embed)
            return
        push(f"DELETE FROM notext WHERE channelid = '{str(channel_id)}'") # pushes a SQL query to delete the channel id from the database
        resp_embed = discord.Embed(title="Finesse Error",
                                description=f"<#{channel_id}> has been removed from the blacklist database.",
                                timestamp=ctx.message.created_at,
                                color=discord.Color.teal())
        await ctx.author.send(embed=resp_embed)
       





def setup(bot):
    print("Loading Base File Commands!")
    bot.add_cog(bobross(bot))
    print("Base Commands Have Been Loaded!")