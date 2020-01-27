import logging
import datetime
import random
import os
import json
import discord
from pathlib import Path
from discord.ext import commands
import sys
import time





class peep(commands.Cog):
    def __init__(self, bot):
        self.bot = bot






    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    async def peep(self, ctx):
        imgur_img_ids = (
            "6d0hbvg", "xQOH7KD", "THNk0Q9", "iXoRWTi", "hONMul7", "pUG8T51", "iHooa87", "n3NLoNA", "iq9O8L1",
            "pGbXrKU",
            "Y3JKEwM", "")
        imgur_img_id = random.choice(imgur_img_ids)
        imgur_url = 'https://i.imgur.com/{}.jpg'.format(imgur_img_id)
        embed = discord.Embed(title="ShaDBoT", description="LiL Bo PeeP")
        embed.set_image(url=imgur_url)
        embed.set_footer(text="Made By ShaD!")
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    async def peepgif(self, ctx):
        imgoat_gif_ids = (
            "dcb88e0137/187131", "dcb88e0137/187132", "dcb88e0137/187133", "dcb88e0137/187134", "dcb88e0137/187135",
            "dcb88e0137/187136", "dcb88e0137/187136", "dcb88e0137/187137", "dcb88e0137/187138", "dcb88e0137/187139",
            "dcb88e0137/187140", "dcb88e0137/187141", "dcb88e0137/187141", "dcb88e0137/187142", "dcb88e0137/187142",
            "dcb88e0137/187143", "dcb88e0137/187143", "dcb88e0137/187143", "dcb88e0137/187144", "dcb88e0137/187143",
            "dcb88e0137/187143", "dcb88e0137/187145", "dcb88e0137/187146", "dcb88e0137/187147", "dcb88e0137/187148",
            "dcb88e0137/187149", "dcb88e0137/187150", "dcb88e0137/187151", "dcb88e0137/187152", "dcb88e0137/187153",
            "dcb88e0137/187154", "dcb88e0137/187155", "dcb88e0137/187156", "dcb88e0137/187157", "dcb88e0137/187158",
            "dcb88e0137/187159", "dcb88e0137/187160", "dcb88e0137/187161", "dcb88e0137/187162", "dcb88e0137/187163",
            "dcb88e0137/187164", "dcb88e0137/187165", "dcb88e0137/187166", "dcb88e0137/187167", "dcb88e0137/187168",
            "dcb88e0137/187169", "dcb88e0137/187170", "dcb88e0137/187171", "dcb88e0137/187172", "dcb88e0137/187173")
        imgoat_gif_id = random.choice(imgoat_gif_ids)
        goat_url = 'https://imgoat.com/uploads/{}.gif'.format(imgoat_gif_id)
        embed = discord.Embed(title="ShaDBoT", description="LiL Bo PeeP")
        embed.set_image(url=goat_url)
        embed.set_footer(text="Made By ShaD!")
        await ctx.send(embed=embed)

def setup(bot):
    print("Loading Peep Commands!")
    bot.add_cog(peep(bot))
    print("Peep Commands Have Been Loaded")



