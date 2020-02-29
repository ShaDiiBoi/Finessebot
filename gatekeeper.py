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
from discord.ext.commands import BucketType
class gatekeeper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.finesse = self.bot.get_guild(534050853477285888)
        self.agree_channel = self.bot.get_channel(594101487806971904)
        self.agree_role = self.finesse.get_role(593200687706275870)
        self.member_role = self.finesse.get_role(534052271265284096)
        self.lobby = self.bot.get_channel(566473203921321984)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.add_roles(self.agree_role)
        word1 = f"``` ```\n <:zzzfinesse:622064373741125673> » Welcome {member.mention} to Finesse! « <:zzzfinesse:622064373741125673>\n" 
        word2 = "*You’re more than welcome but in order to start socializing…*\n"
        word3 = "**Complete your <#566514394612105216>** 💕\n"
        word4 = "**Are you above the age of 13 and agree to our Community Guidelines?** (<#566523946934075393>)\n"
        word5 = "Type:\n"
        word6 = "``.agree`` \n"
        word = word1 + word2 + word3 + word4+ word5 + word6
        await self.agree_channel.send(word)
        
    @commands.command()
    async def fix_agree(self,ctx):
        if ctx.channel.id != 594101487806971904:
            await ctx.send("You Cant Type This Here, do it in <#594101487806971904>")
            return
        
    @commands.cooldown(3,5,type=BucketType.channel)
    @commands.command()
    async def agree(self, ctx):
        if ctx.channel.id != 594101487806971904:
            await ctx.send("You Cant Type This Here, do it in <#594101487806971904>")
            return
        guild = self.bot.get_guild(534050853477285888)
        member = guild.get_member(ctx.author.id)
        print(member.name)
        if self.agree_role not in member.roles and self.member_role in member.roles:
            await ctx.author.send("You Already have access to finesse ,if you do not, then dm Shadii The Owner")
            return
        print(member.roles)
        if self.agree_role in member.roles and self.member_role not in member.roles:
            await member.remove_roles(self.agree_role)
            await member.add_roles(self.member_role)
            await ctx.message.delete()
            await self.lobby.send(f"{member.mention} Just joined ** Finesse! ** ! <:sparkles_pink:548483031560880148> <:zzzfinesse:622064373741125673>")
    @agree.error
    async def agree_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send(f"{ctx.author.mention} ⚠ **You will need to complete the following required** <#566514394612105216> **to enter Finesse**: Gender, Location, DM Status\n **Once you completed your roles confirm you’re 13 by typing: `.agree`**")
        else:
            print(error)
            await ctx.send(f"Error Happened, Send This To The Owner ``` {error}```")
    @commands.command()
    @commands.has_any_role(547784768981434395, 534583040454688781,534098929617207326)
    async def access(self, ctx, user: discord.Member):
        try:
            await user.remove_roles(self.agree_role)
            await user.add_roles(self.member_role)
        except Exception as e:
            await ctx.send("Error occured, try again")
            return
    @agree.error
    async def agree_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This Command Is On Cooldown, Please Wait {round(error.retry_after)}")
        else: print(error)
            
def setup(bot):
    print("gatekeeper system Loading")
    bot.add_cog(gatekeeper(bot))
    print("gatekeeper system Has Been Loaded")