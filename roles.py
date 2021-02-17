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
        role = ctx.guild.get_role(547858928239902726)
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
    @commands.has_permissions(administrator=True)
    async def thepurge(self, ctx, role: discord.Role):
    
        for member in role.members:
            await member.remove_roles(role)
        
        embed = discord.Embed(title="Finesse Bot", description=f"Everyone has been purged from <@&{role.id}>, {ctx.author.mention}!")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)









#STEAKS ROLES ----------------------------------------------------



    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(688748538968145995)
    async def misteak(self, ctx, member: discord.Member = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(688830864171204621)
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=f"Imagine getting removed kek. {member.mention}")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)


    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(688748538968145995)
    async def steak(self, ctx, member: discord.Member , reason: str=None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(688830864171204621)
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=(f" You made it. {member.mention}"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)

#Christyns ROLES ----------------------------------------------------

    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(714242332266070056)
    async def winner(self, ctx, member: discord.Member = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(696763875923853324)
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=f" {member.mention} has cheated to win against {ctx.author.mention}!")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)


    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(714242332266070056)
    async def loser(self, ctx, member: discord.Member , reason: str=None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(696763875923853324)
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=(f"{member.mention} lost against {ctx.author.mention}!"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)



#ASHLYNS ROLES ----------------------------------------------------

    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(705823948784402433)
    async def fuck(self, ctx, member: discord.Member = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(726205564496904203)
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=f"Ashlyn hates u!{member.mention}")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)


    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(705823948784402433)
    async def own(self, ctx, member: discord.Member , reason: str=None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(726205564496904203)
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=(f"you’re now ashlyns kiddo ❤️ {member.mention}!"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)

    # R O M S   R O L E S <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(729157567925715005)
    async def fire(self, ctx, member: discord.Member = None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(769529910800547890)
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=f"{member.mention} You've been removed from the warzone")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)


    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(729157567925715005)
    async def hire(self, ctx, member: discord.Member , reason: str=None):
        if not member:
            plz = discord.Embed(title="Finesse Bot", description="Please Specify A Member...")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(769529910800547890)
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse Bot", description=(f"{member.mention} Welcome to the warzone"),color=discord.Color.teal())
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)


def setup(bot):
    print("Role Commands Loading")
    bot.add_cog(roles(bot))
    print("Role Commands Have Been Loaded")