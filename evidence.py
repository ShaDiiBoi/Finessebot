import discord
import time
import sys, traceback
import logging
import datetime
import json
import random

import os.path
from typing import Union
from discord.ext import tasks
from discord.ext import commands

import asyncio
import re

class evidence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.finesse = self.bot.get_guild(534050853477285888)
        self.evidence_reg = self.bot.get_channel(617164886144974848)
        self.regpath = "/home/shadbot/evidence.json"
        self.staff_id_list = [547784768981434395,547780757251424258,534583040454688781,534098929617207326]
        
        if not os.path.exists(self.regpath):
            with open(self.regpath, "w+") as f:
                data = {"1234": {"punisher": "1334568686","punished": "135367578","reason": "banned lol imagine","evidence": "linkhere.com"}}
                json.dump(data,f)
    @classmethod
    def id_gen(self):
        
        unique = False
        while unique is False:
            idx = ""
            for x in range(15):
                num = random.randint(0,9)
                idx = idx + str(num)
            with open("/home/shadbot/evidence.json","r+") as f:
                data = json.load(f)
            keys = data.keys()
            if str(idx) not in keys:
                break
            
        return idx

        
    
    
        print("INvoked")
       
        
       
        
       
        
        

    @commands.Cog.listener()
    async def on_message(self, message):
        mystr = message.content.lower()
        wordList = re.sub("[^\w]", " ",  mystr).split()
        if mystr.startswith("!"):
            if len(wordList) <= 1: return
            if "ban" == wordList[0]:
                print("possible ban command")
                if message.guild.id == 534050853477285888:
                    print("right guild")
                    member = message.guild.get_member(message.author.id)
                    rolelist = [x.id for x in member.roles if x.id in self.staff_id_list]
                    if len(rolelist) == 0: 
                        print("not a staff")
                        return
                    print("made it to ctx")
                    ctx = await self.bot.get_context(message)
                    print("context got")
                    if not ctx.valid: return
                    print("context is valid")
                    abc = [str(x) for x in range(10)]
                    mentions = message.mentions 
                    if wordList[1] in mentions or isinstance(wordList[1],int) or wordList[1][0] in abc:
                        ban_command = True

                    if not ban_command:
                        print("not a ban command sorry to say") 
                        return

                    await message.author.send(f"What Is Your Evidence/Who Is Your Witness For The Ban On {member.mention}(you have 300 seconds to reply)")
                    def check(m):
                        return m.author.id == message.author.id and isinstance(m.channel,discord.abc.PrivateChannel)

       
                    try:#waits for evidence and if none is given, sets as None
                        evidence = await self.bot.wait_for("message",timeout=300,check=check)
                    except asyncio.TimeoutError as e:
                        print(e)
                        evidence = "None Given"
                    if evidence == "None Given": 
                        try:
                            evidence = wordList[2:]
                        except Exception as e: pass
                    try:
                        ban_reason = await self.finesse.fetch_ban(member).reason
                    except discord.NotFound as e:
                        print(f"Ban Not Found For User {member.name}")
                        return
                    
                    punishid = self.id_gen()
                    evi_embed = discord.Embed(title=f"evidence num {punishid}")
                    evi_embed.add_field(name="Punisher",value=f"<@{message.author.id}>")
                    evi_embed.add_field(name="Punished",value=f"<@{member.id}>")
                    evi_embed.add_field(name="Evidence",value=f"{evidence}")
                    evi_embed.add_field(name="Reason",value=f"{ban_reason}")
                    await self.evidence_reg.send(embed=evi_embed)
                    await message.author.send("Your Punishment Has Been Sent In")

                    

                
                









def setup(bot):
    print("Loading Suggestion System!")
    bot.add_cog(evidence(bot))
    print("Suggestion System  Has Loaded!")
