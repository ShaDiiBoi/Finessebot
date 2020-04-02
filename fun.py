import logging
import datetime
import random
import os
import re

from imgurpython import ImgurClient
import json
import discord
from pathlib import Path
from discord.ext import commands
import asyncio
from urllib.parse import urlparse
import praw
from imgurpython import ImgurClient
import mysql.connector

#LISTS OF IMGUR LINKS
hugl = ["https://i.imgur.com/giviAg7.gif", "https://i.imgur.com/H1hlvmb.gif", "https://i.imgur.com/S1DU3yp.gif", "https://i.imgur.com/yZyAVaW.gif", "https://i.imgur.com/kDziQNd.gif"]
glarel = ["https://i.imgur.com/2sACMZv.gif", "https://i.imgur.com/6YIeVUK.gif", "https://i.imgur.com/M3jCjto.gif", "https://i.imgur.com/ONnowrC.gif", "https://i.imgur.com/JHomlBX.gif"]
kissl = ["https://i.imgur.com/aoQrLRr.gif", "https://i.imgur.com/zL0XgwL.gif", "https://i.imgur.com/weNVhpq.gif", "https://i.imgur.com/il9qcWa.gif", "https://i.imgur.com/gpOWmDE.gif"]
cryl = ["https://i.imgur.com/5xb4ZVK.gif", "https://i.imgur.com/VqLiiPO.gif", "https://i.imgur.com/VdKZMZ5.gif"]
slapl = ["https://i.imgur.com/5QfFc46.gif", "https://i.imgur.com/SX6svrx.gif", "https://i.imgur.com/Jq85Zc1.gif","https://i.imgur.com/CjMqNOf.gif", "https://i.imgur.com/PrPU5eD.gif"]
pokel = ["https://i.imgur.com/pVdaMtV.gif", "https://i.imgur.com/bYwm552.gif", "https://i.imgur.com/gDCdhyp.gif","https://i.imgur.com/bFbDXB6.gif", "https://i.imgur.com/SIiFYwI.gif"]
noml = ["https://i.imgur.com/moYr1hd.gif", "https://i.imgur.com/6dI67Rj.gif", "https://i.imgur.com/ro1KfL5.gif"]
lovel = ["https://i.imgur.com/tYoVoaJ.gif", "https://i.imgur.com/ZLq8t3L.gif", "https://i.imgur.com/Waw9ai5.gif","https://i.imgur.com/0KGgL6o.gif", "https://i.imgur.com/4V7sKcm.gif"]
patl = ["https://i.imgur.com/QaEfr4H.gif", "https://i.imgur.com/zAI1IAK.gif", "https://i.imgur.com/DbYGUDY.gif","https://i.imgur.com/KMG5Q5i.gif", "https://i.imgur.com/1NfP16i.gif"]
blushl = ["https://i.imgur.com/DlLi7n8.gif", "https://i.imgur.com/6E4TPsv.gif", "https://i.imgur.com/KIsAA2E.gif","https://i.imgur.com/3HATOJf.gif", "https://i.imgur.com/OAWHgLW.gif"]
shrugl = ["https://i.imgur.com/s2CXkE2.gif", "https://i.imgur.com/BKlpoIX.gif", "https://i.imgur.com/ViRItNY.gif","https://i.imgur.com/sZ1EjRp.gif"]
smirkl = ["https://i.imgur.com/bqkCkVB.gif", "https://i.imgur.com/v8Z4UJ0.gif", "https://i.imgur.com/hIQbKkz.gif"]
lickl = ["https://i.imgur.com/PCd0rHX.gif", "https://i.imgur.com/iLrRnUc.gif", "https://i.imgur.com/OLKrL4c.gif","https://i.imgur.com/4N2PW05.gif", "https://i.imgur.com/og8BN4E.gif"]
squeezel = ["https://i.imgur.com/u6mI401.gif", "https://i.imgur.com/b31zHVS.gif", "https://i.imgur.com/1g1Jgd5.gif","https://i.imgur.com/c5YW9sT.gif", "https://i.imgur.com/2g1aaDn.gif"]
cuddlel = ["https://i.imgur.com/peWNwqI.gif", "https://i.imgur.com/szsF3Sx.gif", "https://i.imgur.com/5E25Nl2.gif","https://i.imgur.com/RX1PHOm.gif", "https://i.imgur.com/HrwQacz.gif"]
bitel = ["https://i.imgur.com/OYR3zZk.gif", "https://i.imgur.com/jcquQEp.gif", "https://i.imgur.com/gP4Uy3r.gif", "https://i.imgur.com/dR5LWdN.gif", "https://i.imgur.com/IBGQc4p.gif"]


cmdlist = ["bite", "hug", "kiss", "slap", "blush", "cuddle", "lick", "squeeze", "shrug", "blush", "pat", "nom", "love", "cry" "glare", "smirk", "poke"]






def pull(*args):
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="shad",
                    passwd="shadii",
                    database="finesse")
    dbcursor = mydb.cursor(buffered=True)
    dbcursor.execute(*args)
    results = dbcursor.fetchall()
    mydb.commit()
    mydb.close()
    return results






class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.finesse = self.bot.get_guild(534050853477285888)
        self.error_channel = bot.get_channel(596509055376162831)
        self.client_id = "0c30e0ce68c6213"
        self.secret = "e61ca8a36d88c6c9bbc6d47757bedcd7a5cffafca7de86699b36fe3bd06cbcf7"
        self.banned_words = ["faggot","nigger","n1gger","niggers","n1ggers","fags","chinky","chinkys","horny","masturbate","cum"]
        





    @commands.command()
    @commands.cooldown(1,30)
    async def impeep(self, ctx):
        client = ImgurClient(self.client_id,self.secret)
        images = list(client.get_album_images("FtqelOd"))
        ranimg = random.choice(images)
        embed = discord.Embed(colour=discord.Colour.gold())
        embed.set_image(url=ranimg.link)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1,30)
    async def meme(self, ctx):
        client = ImgurClient(self.client_id,self.secret)
        images = list(client.get_album_images("Z4Qdo0i"))
        ranimg = random.choice(images)
        embed = discord.Embed(colour=discord.Colour.gold())
        embed.set_image(url=ranimg.link)
        await ctx.send(embed=embed)

    #-------------------------------------------------------------------------------------------------------------------------------

    @commands.command()
    @commands.has_any_role(547780757251424258, 547784731157200927, 547784768981434395)
    async def add(self, ctx):
        def check(m):
            return m.author.id == ctx.author.id
        await ctx.send("What Command Are You Uploading A Image/Gif To?(use full command name only, eg 'bite', 'cuddle')")
        command_name = await self.bot.wait_for("message", check=check)
        if command_name.content not in cmdlist:
            await ctx.send("thats not a command")
            return
        await ctx.send("What Image/Gif Are You Uploading?(Use Imgur If Possible And Include The Entire Link )")
        link = await self.bot.wait_for("message", check=check)

        url = urlparse(link.content)
        if url.scheme == "":
            link = f"https://{link.content}"
        if url.scheme == "" and url.netloc == "":
            await ctx.send("That Isnt A Link!")
            return
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)
        if "bite" in command_name.content:
            info["bitel"].append(link.content)
        if "glare" in command_name.content:
            info["glarel"].append(link.content)
        if "cuddle" in command_name.content:
            info["cuddlel"].append(link.content)
        if "squeeze" in command_name.content:
            info["squeezel"].append(link.content)
        if "lick" in command_name.content:
            info["lickl"].append(link.content)
        if "smirk" in command_name.content:
            info["smirkl"].append(link.content)
        if "shrug" in command_name.content:
            info["shrugl"].append(link.content)
        if "slap" in command_name.content:
            info["slapl"].append(link.content)
        if "cry" in command_name.content:
            info["cryl"].append(link.content)
        if "pat" in command_name.content:
            info["patl"].append(link.content)
        if "kiss" in command_name.content:
            info["kissl"].append(link.content)
        if "hug" in command_name.content:
            info["hugl"].append(link.content)
        if "love" in command_name.content:
            info["lovel"].append(link.content)
        if "nom" in command_name.content:#
            info["noml"].append(link.content)
        if "poke" in command_name.content:
            info["pokel"].append(link.content)
        if "blush" in command_name.content:
            info["blushl"].append(link.content)
        with open("/home/shadbot/funurl.json","w+") as f:
            json.dump(info,f)
        await ctx.send("Link Added!")
        

        


    



    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.command()
    async def slap(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has slapped {user}. Ouch.. <a:Slap:638367329612202004>", color=0x8ffff8)
            picked = random.choice(info["slapl"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has slapped someone. Ouch..", color=0x8ffff8)
            picked = random.choice(info["slapl"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has slapped {user.mention}. Ouch..", color=0x8ffff8)
        picked = random.choice(info["slapl"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)
    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def poke(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f) 
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has poked {user}. Notice me? <a:poke:638367331495444510>", color=0x8ffff8)
            picked = random.choice(info["pokel"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has poked someone. Notice me? <a:poke:638367331495444510>", color=0x8ffff8)
            poss = ["https://i.imgur.com/pVdaMtV.gif", "https://i.imgur.com/bYwm552.gif", "https://i.imgur.com/gDCdhyp.gif","https://i.imgur.com/bFbDXB6.gif", "https://i.imgur.com/SIiFYwI.gif"]
            picked = random.choice(poss)
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has poked {user.mention}. Notice me? <a:poke:638367331495444510>", color=0x8ffff8)
        poss = ["https://i.imgur.com/pVdaMtV.gif", "https://i.imgur.com/bYwm552.gif", "https://i.imgur.com/gDCdhyp.gif","https://i.imgur.com/bFbDXB6.gif", "https://i.imgur.com/SIiFYwI.gif"]
        picked = random.choice(poss)
        embed.set_image(url=picked)
        await ctx.send(embed=embed)
    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def nom(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)       
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has nommed {user}. I bet they taste good <a:Nom:638367328748306452>", color=0x8ffff8)
            picked = random.choice(info["noml"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has nommed someone. I bet they taste good <a:Nom:638367328748306452>", color=0x8ffff8)

            picked = random.choice(info["noml"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has nommed {user.mention}. I bet they taste good <a:Nom:638367328748306452>", color=0x8ffff8)
        picked = random.choice(info["noml"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)
    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def love(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)      
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"<a:Love1:638367330283290624> {ctx.author.mention} loves {user} with all their heart <a:Love2:638367328169361408>💕", color=0x8ffff8)            
            picked = random.choice(info["lovel"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"<a:Love1:638367330283290624> {ctx.author.mention} loves someone with all their heart <a:Love2:638367328169361408>💕", color=0x8ffff8)  
            picked = random.choice(info["lovel"])          
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Finesse", description=f"<a:Love1:638367330283290624> {ctx.author.mention} loves {user.mention} with all their heart <a:Love2:638367328169361408>💕", color=0x8ffff8)
        picked = random.choice(info["lovel"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)
    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def cry(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)     
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} Cries Their Eyes Out....<:Cry:638367329486635009>", color=0x8ffff8)
        picked = random.choice(info["cryl"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)

    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def blush(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)   
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} is blushing. I wonder why…<a:Blush:638367331130540062>", color=0x8ffff8)
        picked = random.choice(info["blushl"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)

    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def pat(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has patted {user}. How cute! <:Pat:638367328828129290>", color=0x8ffff8)
            picked = random.choice(info["patl"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has patted someone. How cute! <:Pat:638367328828129290>", color=0x8ffff8)
            picked = random.choice(info["patl"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has patted {user.mention}. How cute! <:Pat:638367328828129290>", color=0x8ffff8)
        picked = random.choice(info["patl"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)

    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def shrug(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)       
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has shrugged. Welp <:Shrug:638367329125662761>", color=0x8ffff8)
        picked = random.choice(info["shrugl"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)

    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def smirk(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} smirks. Are they onto something? <:Smirk:638367330820423696>", color=0x8ffff8)
        picked = random.choice(info["smirkl"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)

    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def squeeze(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} squeezed the cheeks of {user}. So cute! <a:Squeeze:638367331327803393>", color=0x8ffff8)
            picked = random.choice(info["squeezel"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} squeezed the cheeks of someone. So cute! <a:Squeeze:638367331327803393>", color=0x8ffff8)
            picked = random.choice(info["squeezel"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} squeezed the cheeks of {user.mention}. So cute! <a:Squeeze:638367331327803393>", color=0x8ffff8)
        picked = random.choice(info["squeezel"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)

    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def lick(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has licked {user}. I bet they taste good <a:Lick:638367328987250698>", color=0x8ffff8)
            picked = random.choice(info["lickl"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has licked someone. I bet they taste good <a:Lick:638367328987250698>", color=0x8ffff8)
            picked = random.choice(info["lickl"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has licked {user.mention}. I bet they taste good <a:Lick:638367328987250698>", color=0x8ffff8)
        picked = random.choice(info["lickl"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)

    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def kiss(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f) 
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has kissed {user}. Smooch <:KissLeft:638367329004159003> <:KissRight:638367329196965897>", color=0x8ffff8)
            picked = random.choice(info["kissl"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has kissed Someone. Smooch  <:KissLeft:638367329004159003> <:KissRight:638367329196965897>", color=0x8ffff8)
            picked = random.choice(info["kissl"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return

            

        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has kissed {user.mention}. Smooch  <:KissLeft:638367329004159003> <:KissRight:638367329196965897>", color=0x8ffff8)
        picked = random.choice(info["kissl"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)
 
    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def glare(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has given {user.mention} The Glare <a:Glare:638367333467029564>", color=0x8ffff8)
        picked = random.choice(info["glarel"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has given {user} The Glare <a:Glare:638367333467029564>", color=0x8ffff8)
            picked = random.choice(info["glarel"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is None:
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has given Someone... The Glare <a:Glare:638367333467029564>", color=0x8ffff8)
            picked = random.choice(info["glarel"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return

    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def hug(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"<:HugLeft:638367328773341185> {ctx.author.mention} has hugged {user}. I bet they liked it <:HugRight:638367329175994379>", color=0x8ffff8)
            picked = random.choice(info["hugl"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has hugged someone. I bet they liked it {emoji[0]}", color=0x8ffff8)
            picked = random.choice(info["hugl"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} has hugged {user.mention}. I bet they liked it {emoji[0]}", color=0x8ffff8)
        picked = random.choice(info["hugl"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)

    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)

    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.command()
    async def cuddle(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"{user} has been cuddled by {ctx.author.mention}. So adorable! <:Cuddle:638367329255817227>", color=0x8ffff8)
            picked = random.choice(info["cuddlel"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"someone has been cuddled by {ctx.author.mention}. So adorable! <:Cuddle:638367329255817227>", color=0x8ffff8)
            picked = random.choice(info["cuddlel"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Finesse", description=f"{user.mention} has been cuddled by {ctx.author.mention}. So adorable! <:Cuddle:638367329255817227>", color=0x8ffff8)
        picked = random.choice(info["cuddlel"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)

    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    @commands.cooldown(2, 10.00, type=commands.BucketType.member)
    @commands.command()
    async def bite(self, ctx, user=None):
        with open("/home/shadbot/funurl.json","r+") as f:
            info = json.load(f)
        if user is not discord.Member:
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} Has Bitten {user}, Did It Hurt? 😱", color=0x8ffff8)
            picked = random.choice(info["bitel"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        if user is "":
            embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} Has Bitten someone, Did It Hurt? 😱", color=0x8ffff8)
            picked = random.choice(info["bitel"])
            embed.set_image(url=picked)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Finesse", description=f"{ctx.author.mention} Has Bitten {user.mention}, Did It Hurt? 😱", color=0x8ffff8)
        picked = random.choice(info["bitel"])
        embed.set_image(url=picked)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(3, 10.00, type=commands.BucketType.channel)
    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    async def ene(self, ctx):

        emoji = []
        for emojis in self.finesse.emojis:
            if emojis.id == 625983337663561749:
                emoji.append(emojis)

        embed = discord.Embed(title=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", description=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", color=0x8ffff8)
        embed.add_field(name=f"ene is best owner owo", value=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}")
        embed.add_field(name=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", value=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}")
        embed.add_field(name=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", value=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}")
        embed.add_field(name=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", value=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}")
        embed.add_field(name=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", value=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", inline=True)
        embed.add_field(name=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", value=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", inline=True)
        embed.add_field(name=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", value=f"{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}{emoji[0]}", inline=True)
        embed.set_footer(text=f"ene")
        embed.set_image(url="https://i.imgur.com/JRzJ5L0.png")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_any_role(642811907417309186,642811877008736303,642811876975050791,642811871233048629642811874983018536,642811874039169045,548846050056863756,586494766359904257,534098929617207326,547784768981434395,547780757251424258)
    async def welcome(self, ctx, member: discord.Member):
        
        appends = []
        for emoji in ctx.guild.emojis:
            ids = [614465427753664522, 622064373741125673, 614465426893701176]
            if emoji.id in ids:
                appends.append(emoji)
        embed = discord.Embed(color=0x8ffff8)
        #appends[0] IS OWOSNEAKY
        #appends[1] IS self.finesseLOGO
        #appends[2] IS SPARKLING HEARTS
        #
        embed.set_image(url="https://cdn.discordapp.com/attachments/566523946934075393/624931522708766742/ezgif-4-7e2de666a8dd.gif")
        embed.add_field(name="<:zzzfinesse:622064373741125673> ", value=f"{appends[1]} Hi {member.mention} ♡, welcome to Finesse! Make sure you pick some roles in <#566514394612105216> We hope you enjoy your stay here {appends[0]} {appends[2]}  {appends[1]} ")
        embed.set_footer(icon_url="https://i.imgur.com/CKQU6PX.png")
        await ctx.send(embed=embed)



    @welcome.error
    async def welcome_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send("You Are Missing The Required Roles To Use This Command Silly :)")


    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.has_permissions(administrator=True)
    async def promote(self, ctx, member: discord.Member = None):
        role1 = ctx.guild.get_role(534098929617207326)
        role2 = ctx.guild.get_role(547784768981434395)
        if  role1 not in member.roles:
            await member.add_roles(role1)
        elif role2 not in member.roles:
            await member.add_roles(role2)
        embed = discord.Embed(title='ShaDBot', description=(f"{member.mention} has been Promoted!"))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.has_permissions(administrator=True)
    async def demote(self, ctx, member: discord.Member = None):
        role1 = ctx.guild.get_role(534098929617207326)
        role2 = ctx.guild.get_role(547784768981434395)
        if role1 in member.roles:
            await member.remove_roles(role1)
        elif role2 in member.roles:
            await member.remove_roles(role2)
        
        embed = discord.Embed(title='ShaDBot', description=(f"{member.mention} has been demoted!"))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 2.0, type=commands.BucketType.default)
    @commands.guild_only()
    async def shadlove(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("Specify Someone PlOx")
        else:
            possibles = ("Shad gives you a big ol smooch xx", "Shad doesn't like you", "Shad thinks you smell",
                         "Shad starts frenching you", "Shad owo nuzzles your bulgy wulgy owo")
            list = random.choice(possibles)
            await ctx.send(list)

    @commands.command()
    @commands.cooldown(1, 2.0, type=commands.BucketType.default)
    @commands.guild_only()
    async def Rei(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send(f"This Isn't A Person Is It {ctx.message.author.mention}")
        else:
            possibles = ("Reilly Thinks You Have Autism", "Reilly Will Fight You Cunt", "Reilly Thinks Your Weird",
                         "Reilly Licks Your Butt", "Reilly Trys To Call A Doctor For Your Stupidity")
            list2 = random.choice(possibles)
            await ctx.send(list2)

    @commands.command()
    @commands.cooldown(1, 2.0, type=commands.BucketType.default)
    async def Shad(self, ctx):
        embed = discord.Embed(title='ShaDBot', description=("shad lobes u :)"))
        embed.set_image(url='https://i.imgur.com/WV2Pv0h.png')
        await ctx.send(embed=embed)

    @commands.command()
    async def time(self, ctx):
        today = datetime.date.today()
        bday = datetime.date(2020, 12, 19)
        time_to_bday = bday - today
        await ctx.send(f"Time till Shad's Birthday is {time_to_bday.days} Days Away!")





    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    async def fight(self, ctx, member: discord.Member = None):
        posslist = [f"{member.mention} Sliced {ctx.author.mention} Up!",
                    f"{ctx.author.mention} Beat {member.mention} to death",
                    f"{member.mention} Just Destroyed {ctx.author.mention}",
                    f"{member.mention} Has Shot {ctx.author.mention} Dead!",
                    f"{ctx.author.mention} Broke {member.mention}'s Body And Heart <3",
                    F"{ctx.author.mention} Destroyed {member.mention}'s Soul",
                    f"{ctx.author.mention} Murdered {member.mention} In Cold Blood"]
        donelist = random.choice(posslist)
        await ctx.send(donelist)

    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.has_permissions(kick_members=True)
    async def bean(self, ctx, member: discord.Member = None):
        embed = discord.Embed(title="ShaDBoT", description=(
            f"{member.mention} Will Be Banned In A Few Seconds!Type Cancel To Cancel This Action!"))
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)
    
    
    @commands.command()
    async def tea(self, ctx, member: discord.Member): 
        responselist = [f"Tea Startings Going Off On {member.mention}",
                        f"Tea Loves {member.mention} so much omg MWAHHH", 
                        f"Tea Calls {member.mention} Toxiccc", 
                        f"Tea Steals {member.mention} Memes!", 
                        f"Tea Fights {member.mention}"]
        picked = random.choice(responselist)
        await ctx.send(picked)

    def blacklisted():
        async def predicate(ctx):
            x = pull("select * from blacklist")
            return ctx.author.id not in x
        return commands.check(predicate)
        

    @commands.command()
    @blacklisted()
    @commands.dm_only()
    @commands.cooldown(2,300,commands.BucketType.user)
    async def confess(self,ctx):
        string = "Before You Confess, Please Remember To Follow The Confession Rules\n " \
        "**1.** Do Not Confess Anything That Breaks Discord TOS Or Finesse's Rules! \n" \
        "**2** Do Not Abuse The System Or You Will Be Blacklisted\n" \
        "Moving On, Please Reply What You Want To Confess Today!" 
        menu_embed = discord.Embed(title="Welcome To The Finesse Confession System",description=string,color=discord.Color.teal())
        await ctx.send(embed=menu_embed)
        def check1(m):
            return m.channel == ctx.channel and m.author.id == ctx.author.id
        confession = await self.bot.wait_for("message", check=check1)
        wordList = re.sub("[^\w]", " ",  confession.content).split()
        x = [mes for mes in wordList if mes in self.banned_words]
        if len(x) > 0:
            await self.bot.get_channel(663143750046056507).send(f"<@{ctx.author.id}> Has Just Used A Banned Word In There Confession, The Word Was `{x[0]}`")
            blacklisted = pull("INSERT INTO blacklist VALUES (%s,%s)",(ctx.author.id,"Violated The Confession System Word Filter"))
            await ctx.author.send("You Have Been Blacklisted From The Confession System")

        
        confessChannel = self.bot.get_channel(570045064990949376)
        embed = discord.Embed(title=f"Finesse Confession!",description=f"*{confession.content}*",color=discord.Colour.teal())
        embed.set_author(name="All Confessions Are Anonymous Unless They Are Filtered By The Word Filter")
        await confessChannel.send(embed=embed)
        fin_embed = discord.Embed(title="Confession Sent",description="Your Confession Has Been Sent To <#570045064990949376>!",color=discord.Colour.teal())
        await ctx.send(embed=fin_embed)
        shad = self.bot.get_user(236802606352039938)
        await shad.send(content=f"{ctx.author.mention}",embed=embed)
def setup(bot):
    print("Loading Fun Commands!")
    bot.add_cog(fun(bot))
    print("Fun Commands Have Loaded!")
