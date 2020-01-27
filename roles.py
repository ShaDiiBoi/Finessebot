import logging
import datetime
import random
import os
import json
import discord
from pathlib import Path
from discord.ext import commands
import time
from typing import Union

 

class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    

    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def remove(self, ctx, member: discord.Member = None, reason: str = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(555829259902386176)
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=("Bear's Role Has Been Removed!"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)



    


    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def watch(self, ctx, member: discord.Member = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = discord.utils.get(ctx.guild.roles, name="Special Starers")
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=(f"{member.mention} Has Become one of shad's Special Starers. Given By {ctx.author.mention}"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def lilpeep(self, ctx, member: discord.Member = None, reason: str = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = discord.utils.get(ctx.guild.roles, name="♡~ℓιℓ ρєєρ~♡")
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=(f"Peep's Role Has Been Given By {ctx.author.mention}"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)

    @lilpeep.error
    async def lilpeep_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title="Finesse Bot", description="You Are Not Allowed To Do This....")
            embed.set_footer(text="Made By ShaD")
            await ctx.send(embed=embed)

    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def givepm(self, ctx, member: discord.Member):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description=f"Please Specify A Member {ctx.author.mention}")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = discord.utils.get(ctx.guild.roles, id=547858928239902726)
        await member.add_roles(role)

    

    @commands.command()
    @commands.is_owner()
    @commands.guild_only()
    async def active(self, ctx):
        active = ctx.guild.get_role(547858798644166667)
        await active.edit(mentionable=True)
        await ctx.send(f"{active.mention} *** S O C I A L I Z E  E V E R Y O N E***")
        await active.edit(mentionable=False)
        print("letsgetactive Done")


#PRIVATE ROLES


    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(651150468604624898)
    async def deleder(self, ctx, member: discord.Member = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(651149653475328009)
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=f"eder Has Removed His Role From {member.mention}!")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)



    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(651150468604624898)
    async def edernotoksik(self, ctx, member: discord.Member , reason: str=None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(651149653475328009)
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=(f"eder has given his role to {member.mention}!"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)


#REILLY------------------------------------------------------------

    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(605813970208817153)
    async def Normal(self, ctx, member: discord.Member = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(612029582236712975)
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=f"You were made normal {member.mention}!")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)


    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(605813970208817153)
    async def Challenged(self, ctx, member: discord.Member , reason: str=None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(612029582236712975)
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=(f"You were made mentally Challenged {member.mention}!"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)



#CASSIES ROLES ----------------------------------------------------

    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(657540616422424646)
    async def deletecass(self, ctx, member: discord.Member = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(657540616422424646)
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=f"cassrole has been deleted. {member.mention}!")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)


    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(657540616422424646)
    async def givecass(self, ctx, member: discord.Member , reason: str=None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(657540616422424646)
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=(f" cassrole has been given. {member.mention}!"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)

#ACES ROLES ----------------------------------------------------
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(645014560646103080)
    async def takesoul(self, ctx, member: discord.Member , reason: str=None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(657548942900330498)
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=(f"Ace Has Taken Your Soul!  ♦️ ♠️ ♥️ ♣️ {member.mention}!"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)
    
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(645014560646103080)
    async def returnsoul(self, ctx, member: discord.Member = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(657548942900330498)
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=f"Ace Has Given You Your Soul Back! ♦️ ♠️ ♥️ ♣️. {member.mention}!")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)

    # @commands.command()
    # @commands.has_any_role(625750524263661578)
    # async def sky(self, ctx, user: Union[int, discord.Member]):
    #     chan = ctx.guild.get_channel(625751324776202268)
    #     if isinstance(user, int):
    #         try:
    #             user = ctx.guild.get_member(user)
    #         except Exception as e:
    #             print(e)
    #             await ctx.send("ERROR HAPPENED, SEND TO SHADII << ```{} ```".format(e))
    #     await chan.set_permissions(user, connect=True)
    #     await ctx.send(f"{user.mention} Has Gained  Access To Skylars VC!, Requested by {ctx.author.mention}!")
    #     return
    
    # @commands.command()
    # @commands.has_any_role(625750524263661578)
    # async def skyrem(self, ctx, user: Union[int, discord.Member]):
    #     chan = ctx.guild.get_channel(625751324776202268)
    #     if isinstance(user, int):
    #         try:
    #             user = ctx.guild.get_member(user)
    #         except Exception as e:
    #             print(e)
    #             await ctx.send("ERROR HAPPENED, SEND TO SHADII << ```{} ```".format(e))
    #     await chan.set_permissions(user, connect=False)
    #     await ctx.send(f"{user.mention} Has Lost Access To Skylars VC!, Requested by {ctx.author.mention}!")
    #     return

def setup(bot):
    print("Role Commands Loading")
    bot.add_cog(roles(bot))
    print("Role Commands Have Been Loaded")