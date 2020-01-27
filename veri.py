import logging
import datetime
import random
import os
import json
import discord
from pathlib import Path
import asyncio
from discord.ext import commands
import time
from collections.abc import Sequence



def make_sequence(seq):

    if seq is None:
        return ()
    if isinstance(seq, Sequence) and not isinstance(seq, str):
        return seq
    else:
        return (seq,)

def check1(m):
    return m.channel.id == 576829378638512158



def reaction_check(message=None, emoji=None, author=None, ignore_bot=True):
    message = make_sequence(message)
    message = tuple(m.id for m in message)
    emoji = make_sequence(emoji)
    author = make_sequence(author)
    def check(reaction, user):
        if ignore_bot and user.bot:
            return False
        if message and reaction.message.id not in message:
            return False
        if emoji and reaction.emoji not in emoji:
            return False
        if author and user not in author:
            return False
        return True
    return check

class veri(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        server = self.bot.get_guild(payload.guild_id) 
        if server.id == 523042374209765377:
            altera = self.bot.get_guild(523042374209765377)
            
            finesse = self.bot.get_guild(534050853477285888)
            channel = server.get_channel(payload.channel_id)
            judge = self.bot.get_user(payload.user_id)
            if judge.id == self.bot.user.id:
                return
            emoji = payload.emoji
            msg1 = await channel.fetch_message(payload.message_id)
            if channel.id == 617508555599380500:  

                    embed1 = msg1.embeds[0]
                    user = self.bot.get_user(int(embed1.title))
                    if judge.id == 597083595840159764:
                        return
                    member = finesse.get_member(int(embed1.title))
                    male = finesse.get_role(547823326689493012)
                    other = finesse.get_role(547851482045874178)

                    female = finesse.get_role(547923211699093532)
                    logchan = altera.get_channel(617515720779104256)
                    if str(emoji) == "✅":
                        await msg1.delete()
                        maleself = finesse.get_role(593699291722416129)
                        femaleself = finesse.get_role(593699295656542213)
                        otherself = finesse.get_role(593699293316120584)
                        if other in member.roles:
                            await member.add_roles(otherself,atomic=True)
                        if male in member.roles:
                            await member.add_roles(maleself,atomic=True) 
                        if female in member.roles:
                            await member.add_roles(femaleself, atomic=True)
                        embed = discord.Embed(title="Verification Log",description=f"{judge.mention} Has Accepted {member.mention}'s verification(Selfie Verified)")
                        await logchan.send(embed=embed)
                        await user.send("<:zzfinesse:547821095559102474> Congratulations, your verifications has been approved! <:zzfinesse:547821095559102474> \n Checkout <#566523946934075393> for your extra privileges! \n Questions? Do not hesitate to contact a staff member")

                    if str(emoji) == "🐶":
                        await msg1.delete()
                        embed = discord.Embed(title="Verification Log",description=f"{judge.mention} Has Denied {member.mention}'s verification(Face Not Shown At All Or Fully)")
                        await logchan.send(embed=embed)
                        await user.send("^^Check Above")
                        await user.send("<:zzfinesse:547821095559102474> Your verification has been denied! <:zzfinesse:547821095559102474> \n Reason: Face not fully/clearly visible and/or using of filters, please re-read the instructions \n Questions? Do not hesitate to contact a staff member.")
                        return

                    if str(emoji) == "📰":
                        await msg1.delete()
                        embed = discord.Embed(title="Verification Log",description=f"{judge.mention} Has Denied {member.mention}'s verification(Not Enough Information Shown)")
                        await logchan.send(embed=embed)
                        await user.send("^^Check Above")
                        await user.send(content="<:zzfinesse:547821095559102474> Your verification has been denied! <:zzfinesse:547821095559102474>  Reason: Incomplete/Incorrect information, please re-read the instructions! Questions? Do not hesitate to contact a staff member.", delete_after=15.00)
                        return
                    if str(emoji) == "⛔":
                        await msg1.delete()
                        embed = discord.Embed(title="Verification Log",description=f"{judge.mention} Has  Blacklisted {member.mention}'s verification(Banned)")
                        await logchan.send(embed=embed)
                        await user.send("You Have Been Found To Violate The Rules")
                        await finesse.ban(user=member, reason="Violated Verification Rules", delete_message_days=0)
                        return
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @commands.Cog.listener()
    async def on_message(self, message):
        user = self.bot.get_user(message.author.id)
        def check(m):
            return isinstance(m.channel, discord.abc.PrivateChannel) and m.author.id == person.id
        finesse = self.bot.get_guild(534050853477285888)
        person = self.bot.get_user(message.author.id)
        altera = self.bot.get_guild(523042374209765377)
        logchan = altera.get_channel(553627685683855390)
        if isinstance(message.channel, discord.abc.PrivateChannel):
            if message.attachments:
                await user.send("Is This The Image You Want To Submit As Verification?(Reply With yes or no) \n NOTE ***If you dont have a gender role this will not work***")
                wait = await self.bot.wait_for("message", check=check)
                if "no" in wait.content.lower():
                        await message.author.send("Sorry To Hear You Wont Be Verifying. Have A Nice Day!")
                        return
                if "yes" in wait.content.lower():
                    member = finesse.get_member(message.author.id)
                    proc = await user.send("Processing!")
                    male = finesse.get_role(547823326689493012)
                    other = finesse.get_role(547851482045874178)
                    female = finesse.get_role(547923211699093532)
                    print("female works")
                    member = finesse.get_member(message.author.id)
                    print("m works")
                    mesindex = message.attachments[0] 
                    mesurl = mesindex.url
                    print("roles gotten link works")
                    verchan = altera.get_channel(617508555599380500)
                    print("Channel Gotten")
                    gen = ""                
                    if male in member.roles:
                        gen = "Male"
                    elif female in member.roles:
                        gen = "Female"
                    elif other in member.roles:
                        await user.send("Please Reply With Your Gender")
                        gender_event = await self.bot.wait_for("message",check=check)
                        gen = gender_event.content
                    else:
                        await user.send("You Have No Gender Role, Please Get One In <#566514394612105216>")
                        return
                    embed = discord.Embed(title=f"{message.author.id}", description=(f"**Verification Photo By** {message.author.mention} \n **Gender :** {gen}"))
                    embed.set_image(url=str(mesurl))
                    msg = await verchan.send(embed=embed)
                    print(msg.id)
                    await msg.add_reaction("✅")
                    await msg.add_reaction("🐶")
                    await msg.add_reaction("📰")
                    await msg.add_reaction("⛔")
                    print("message sent")
                    await message.author.send("Your Image Has Been Sent To Be Verified, Please Wait")
                    print("reactions added")       

def setup(bot):
    print("Loading Verification System!")
    bot.add_cog(veri(bot))
    print("Verification System Have Loaded!")


                


