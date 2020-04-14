import discord
from pathlib import Path
import time
import sys, traceback
import logging
import datetime
import json
import mysql.connector
import os.path
from typing import Union
from discord.ext import tasks
from discord.ext import commands
from collections.abc import Sequence
import asyncio
import re

class elite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.banned_words = ["hitler","nigger","n!gger","niggas","nibbas","dating","underage","rape","cracker"]
        if not os.path.exists("/home/shadbot/custom_roles.json"):
            with open("/home/shadbot/custom_roles.json","w+") as f:
                info = {"13574677": {"owner": "12356364736346","role_id": "1234567"}}
                json.dump(info,f)

        self.finesse = self.bot.get_guild(534050853477285888) 
        self.elite = self.finesse.get_role(548846050056863756)
        self.color_embed = discord.Embed(title="Color Picking!",description="Hello, Please Pick A Hex Code For Your Role Color from The Following Site:(Or A Site Of Your Choice) And Reply With The Code")
        self.error_embed = discord.Embed(title="Error Occured!",description="A error occured during the command, dm the owner for assistance!")
        self.title_embed = discord.Embed(title="Pick A Name!",description="Please Pick A Name For Your Custom Role")
        

    
    @commands.command()
    @commands.has_role(548846050056863756)
    async def custom_create(self, ctx, *rolename):
        if len(rolename) > 30: 
            await ctx.send("Your Role Name Is Too Long")
            return
        
        await ctx.send("Check Your Dms!")
        if ctx.author.id in data.keys():
            await ctx.author.send("you have already created a role!, try again")
            return
        for x in range(3):
            if x == 3:
                await ctx.author.send("You Have Exceeded Your Allowed Number Of Retries, Please Restart The Command If You Wish To Try Again")
                return
            await ctx.author.send(content="https://htmlcolorcodes.com/color-picker/",embed=self.color_embed)
            def check(m):
                return isinstance(m.channel, discord.abc.PrivateChannel) and m.author == ctx.author
            hex_color = await self.bot.wait_for("message",check=check,timeout=300)
            try:

                hex_code = await commands.ColourConverter().convert(ctx,hex_color.content)
            except Exception as e:
                print(e)
                await ctx.author.send("This Is Not A Hex, Please Try Again(Make Sure To Only Send The Hex In The Reply)")
                continue
            break
        
        role1 = await self.finesse.create_role(name=f"{rolename}",colour=hex_code,hoist=True,reason=f"Created by {ctx.author.name} through the elite system")
        
        await asyncio.sleep(2)
        if role1 is None:
            print("Role Could Not Be Found")
            await ctx.author.send(embed=self.error_embed)
            return
        print("role name is ",end=" ")
        elite_role = self.finesse.get_role(548846050056863756)
        pos = elite_role.position + 1
        print("position = " + str(pos))
        await role1.edit(position=pos)
        with open("/home/shadbot/custom_roles.json","r+") as f:
            data = json.load(f)
            data[f"{ctx.author.id}"] = {}
            data[f"{ctx.author.id}"]["owner"] = str(ctx.author.id)
            data[f"{ctx.author.id}"]["role_id"] = role1.id
            f.seek(0)
            json.dump(data,f)
            f.truncate()
        member = ctx.guild.get_member(int(ctx.author.id))
        await member.add_roles(role1)
        await ctx.author.send("Your Role Has Been Created And Given To You")


    @commands.command()
    @commands.has_role(548846050056863756)
    async def custom_name(self, ctx):
        for x in range(3):
            if x == 3:
                await ctx.author.send("You Have Exceeded Your Allowed Number Of Retries, Please Restart The Command If You Wish To Try Again")
                return
            await ctx.author.send(embed=self.title_embed)
            def check(m):
                return isinstance(m.channel, discord.abc.PrivateChannel) and m.author == ctx.author
            title = await self.bot.wait_for("message",check=check,timeout=300)
            wordList = re.sub("[^\w]", " ",  title.content).split()
            for word in wordList:
                if word in self.banned_words:
                    await ctx.author.send("There Is A Banned Word In This, Retry")
                    continue
            if len(title.content) > 60:
                await ctx.send("This Role Name Is Way Too Long, Retry Again")
                return
            break
        
        with open("/home/shadbot/custom_roles.json","r+") as f:
            info = json.load(f)
        role_id = info[f"{ctx.author.id}"]["role_id"]
        user_role = discord.utils.get(self.finesse.roles,id=role_id)
        if user_role is None:
            print("Role Could Not Be Found")
            await ctx.author.send(embed=self.error_embed)
            return
        await user_role.edit(name=title.content)
        await ctx.author.send("Your Role Has Been Changed")

    @commands.command()
    @commands.has_role(548846050056863756)
    async def custom_color(self, ctx):
        with open("/home/shadbot/custom_roles.json","r+") as f:
            info = json.load(f)
        if ctx.author.id not in info.keys(): 
            await ctx.send("You Have Not Made A Role, Run The Command `.custom_create` First")
            return
        for x in range(3):
            if x == 3:
                await ctx.author.send("You Have Exceeded Your Allowed Number Of Retries, Please Restart The Command If You Wish To Try Again")
                return
            await ctx.author.send(content="https://htmlcolorcodes.com/color-picker/",embed=self.color_embed)
            def check(m):
                return isinstance(m.channel, discord.abc.PrivateChannel) and m.author == ctx.author
            hex_color = await self.bot.wait_for("message",check=check,timeout=300)
            try:

                hex_code = await commands.ColourConverter().convert(ctx,hex_color.content)
            except Exception as e:
                print(e)
                await ctx.author.send("This Is Not A Hex, Please Try Again(Make Sure To Only Send The Hex In The Reply)")
                continue
            break
        with open("/home/shadbot/custom_roles.json","r+") as f:
            info = json.load(f)
        role_id = info[f"{ctx.author.id}"]["role_id"]
        user_role = discord.utils.get(self.finesse.roles,id=role_id)
        if user_role is None:
            print("Role Could Not Be Found")
            await ctx.author.send(embed=self.error_embed)
            return
        await user_role.edit(colour=hex_code)
        await ctx.author.send("Your Role Has Been Changed")
    
    @commands.command()
    @commands.has_role(548846050056863756)
    async def custom_delete(self, ctx):
        with open("/home/shadbot/custom_roles.json","r+") as f:
            data = json.load(f)
        try:
            role_id = data[f"{ctx.author.id}"]["role_id"]
        except KeyError as key:
            await ctx.author.send("you dont  have a custom role, create one please")
            return
        user_role = discord.utils.get(self.finesse.roles,id=role_id)
        await user_role.delete()
        with open("/home/shadbot/custom_roles.json","r+") as f:
            data = json.load(f)
            try :
                data.pop([f"{ctx.author.id}"],None)
            except Exception as e:
                print(e)
                await ctx.author.send("You Dont Have A Vc, Retry When You Create One")
                return
            f.seek(0)
            json.dump(data,f)
            f.truncate()
        await ctx.send("Your Vc Has Been Deleted")
def setup(bot):
    print("Loading custom command System!")
    bot.add_cog(elite(bot))
    print("custom command sys loaded")