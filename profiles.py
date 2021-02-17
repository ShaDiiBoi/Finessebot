import logging
import datetime
import json
import os.path
import discord
from discord.ext import commands
import re
import time as tx
from collections.abc import Sequence
import asyncio
import mysql.connector
import gc





def profile_exists(uid):
    exist = os.path.exists(path= f"/home/shadbot/prof_data/{uid}.json")
    if exist: return True
    else: return False

def is_cooldown_finished(roles,user_time): #HASNT BEEN EDITED YET
    time_waited = int(tx.time()-user_time)
    print(time_waited)
    if 585530183717748752 in roles:
        x = 21600 # charmboost
        
        if time_waited > x: return True
        else: return False
    if 515567432799092737 in roles and 515567433453666304 not in roles and 568708508833415189 not in roles:#charm norm
        x = 28800# charm211747
        if time_waited > x: return True
        else: return False 
    if 515567433453666304 in roles and 515567432799092737 not in roles and 568708508833415189 not in roles: # charm plus
        x = 14400 #Charm +
        if time_waited > x: return True
        else: return False 
    if 568708508833415189 in roles and 515567433453666304 not in roles and 515567432799092737 not in roles:#charm plus plus
        x = 7200 #Charm ++
        if time_waited > x: return True
        else: return False 
    if 568708508833415189 not in roles and 515567433453666304 not in roles and 515567432799092737 not in roles:
        x = 172800
        if time_waited > x: return True
        else: return False

class profiles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
        memory_collect.start()
        self.banned_words = ["sexuality", "girlfriend","looking","status",
                        "boyfriend","relationship","single","taken",
                        "not looking","gay","straight","lesbian",
                        "asexual","transgender","heterosexual",
                        "bf","gf","homosexual","bisexual","dom","bdsm"] 
        self.colors = {
            "red": 0xff656d,
            "pink": 0xff656d,
            "green": 0xff656d,
            "purple": 0xff656d,
            "yellow": 0xff656d,
            "blue": 0xff656d,
            "gold": 0xff656d,
        
        }
        

    @tasks.loop(seconds=300)
    async def memory_collect(self):
        print(gc.get_count())
        print("collecting..")
        gc.collect()
        print(gc.get_count())
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        def make_sequence(seq):
            if seq is None:
                return ()
            if isinstance(seq, Sequence) and not isinstance(seq, str):
                return seq
            else:
                return (seq,)

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

        #variables
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        def check(m):
                return isinstance(m.channel, discord.abc.PrivateChannel) and m.author.id == user.id
        

    #Work
        if payload.channel_id == 615342434146058252:
            finesse = self.bot.get_guild(534050853477285888)
            
            guild = self.bot.get_guild(534050853477285888)
            member = guild.get_member(payload.user_id)
            user = self.bot.get_user(payload.user_id)
            path2 = f"/home/shadbot/bump_check/{user.id}.json"
            full = f"{user.name}#{user.discriminator}, <@{user.id}>"
            #R O L E S
            interest_roles = []
            for role in finesse.roles:
                if role.name.startswith("Likes"):
                    interest_roles.append(role)
                else:
                    continue
            user_interests = []
            [user_interests.append(role) for role in interest_roles if role in member.roles]
                
                    
            
            interests_names = [i.name[6:] for i in user_interests]
            interestString = " ,".join(interests_names)
            fver = finesse.get_role(593699295656542213)
            mver = finesse.get_role(593699291722416129)
            otherver = finesse.get_role(593699293316120584)
            # G E N D E R
            male = finesse.get_role(547823326689493012)#newchan = finesse.get_channel(566474557834395659)
            female = finesse.get_role(547923211699093532)
            other = finesse.get_role(547851482045874178)
            #C H A R M 
            finboost = finesse.get_role(586494766359904257)
            finesselite = finesse.get_role(548846050056863756)

            #C H A N N E L S
            newchan = finesse.get_channel(566474557834395659)
            if payload.emoji.id == 647803625988685834:
                #   BUMP F U N C T I O N 
                await message.remove_reaction(payload.emoji, member)
                
                path= f"/home/shadbot/prof_data/{member.id}.json"
                exist = os.path.exists(path)
                if not profile_exists(member.id):
                    error_embed = discord.Embed(
                        title="Error Occured!",
                        description="Sorry but you have not created a profile, please check <#629769781658124299> to create one",
                        color=discord.Color.teal(),
                        timestamp=datetime.datetime.now()
                    )
                    await user.send(embed=error_embed)
                    return

                with open(path2, "r+") as f:
                    data = json.load(f)
                    if data["cooled"] == "false":
                        await user.send("You Have not Finished Your Cooldown")
                        return
                    if data["cooled"] == "true":
                        await user.send("Starting Bump")
                with open(path, "r+") as info:
                    info = json.load(info)
                if finboost not in member.roles:
                    if finesselite in member.roles:
                        
                        await user.send("Choose a color from The following, Red: ff656d \nBlue: 8fd2ff \nGreen: 6aff8d (respond with Red or Blue or Green)")
                        color = await self.bot.wait_for("message",check=check)
                        if "red" in color.content.lower() or "ff656d" in color.content.lower():
                            normalembed = discord.Embed(title=f"Finesse Profile bot",description=f"**Discord User**:{full} **Gender:** {info['gender']} **Age:** {info['Age']}", color=0xff656d)
                            normalembed.set_author(name=f"{user.id}")
                            if "imageurl" in info:
                                
                                normalembed.set_thumbnail(url=str(info["imageurl"]))
                            if "imageurl" not in info:
                                normalembed.set_thumbnail(url=str(user.avatar_url))
                            if fver in member.roles or mver in member.roles or otherver in member.roles: normalembed.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                            else: normalembed.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                            normalembed.add_field(name="Age", value=info["Age"], inline=True)
                            normalembed.add_field(name="Gender", value=info["gender"], inline=True)
                            
                            #"field works")
                            normalembed.add_field(name="Interests",value=interestString, inline=False)
                            normalembed.add_field(name="Location", value=info["location"], inline=True)
                            
                            normalembed.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                            normalembed.add_field(name="About Me", value=info["bio"], inline=False)
                            
                            normalembed.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                        if "blue" in color.content.lower() or "8fd2ff" in color.content.lower():
                            normalembed = discord.Embed(title=f"Finesse Profile bot",description=f"**Discord User**:{full} **Gender:** {info['gender']} **Age:** {info['Age']}", color=0x8fd2ff)
                            normalembed.set_author(name=f"{user.id}")
                            if "imageurl" in info:
                                
                                normalembed.set_thumbnail(url=str(info["imageurl"]))
                            if "imageurl" not in info:
                                normalembed.set_thumbnail(url=str(user.avatar_url))
                                
                            if fver in member.roles or mver in member.roles or otherver in member.roles:
                                normalembed.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                            else:
                                normalembed.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                            normalembed.add_field(name="Age", value=info["Age"], inline=True)
                            normalembed.add_field(name="Gender", value=info["gender"], inline=True)
                            
                            #"field works")
                            normalembed.add_field(name="Location", value=info["location"], inline=True)
                            normalembed.add_field(name="Interests",value=interestString, inline=False)
                            normalembed.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                            normalembed.add_field(name="About Me", value=info["bio"], inline=False)
                            
                            normalembed.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                        if "green" in color.content.lower() or "6aff8d" in color.content.lower():
                            normalembed = discord.Embed(title=f"Finesse Profile bot",description=f"**Discord User**:{full} **Gender:** {info['gender']} **Age:** {info['Age']}", color=0x6aff8d)
                            normalembed.set_author(name=f"{user.id}")
                            if "imageurl" in info:
                                
                                normalembed.set_thumbnail(url=str(info["imageurl"]))
                            if "imageurl" not in info:
                                normalembed.set_thumbnail(url=str(user.avatar_url))
                                
                            if fver in member.roles or mver in member.roles or otherver in member.roles:
                                normalembed.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                            else:
                                normalembed.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                            normalembed.add_field(name="Age", value=info["Age"], inline=True)
                            normalembed.add_field(name="Gender", value=info["gender"], inline=True)
                            
                            #"field works")
                            normalembed.add_field(name="Location", value=info["location"], inline=True)
                            normalembed.add_field(name="Interests",value=interestString, inline=False)
                            normalembed.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                            normalembed.add_field(name="About Me", value=info["bio"], inline=False)
                            
                            normalembed.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                        else:
                            await user.send("Thats Not A Option, Sorry But You Will Need To Rerun This Command")
                            return


                        mes = await newchan.send(f"{user.mention}",embed=normalembed)
                        await user.send("Your Profile Has Been Sent")
                            
                            
                                
                            
                                

                            

                        with open(path, "r+") as f:
                            info = json.load(f)
                            
                            f.seek(0)  
                            json.dump(info, f,indent=4)
                            f.truncate()
                            
                        with open(path2, "r+") as write:
                            timewait = {"cooled": "false"}
                            write.seek(0)  
                            json.dump(timewait, write)
                            write.truncate()
        
                            await asyncio.sleep(57600)
                            timewait = {"cooled": "true"}
                            with open(path2, "r+") as write:
                                write.seek(0)  
                                json.dump(timewait, write)
                                write.truncate()

                if finesselite not in member.roles and finboost not in member.roles:
                    await user.send("Choose a Color From The Following, Normal or Gold(respond with Gold Or Normal)")
                    colorcode = await self.bot.wait_for("message",check=check)

                    with open(path, "r+") as info:
                        info = json.load(info)
                            
                    #0x80646b
                    if "normal" in colorcode.content.lower():
                        normalembed = discord.Embed(title=f"Finesse Profile bot",description=f"**Discord User**:{full} **Gender:** {info['gender']} **Age:** {info['Age']}", color=0x80646b)
                        normalembed.set_author(name=f"{user.id}")
                        if "imageurl" in info:
                            
                            normalembed.set_thumbnail(url=str(info["imageurl"]))
                        if "imageurl" not in info:
                            normalembed.set_thumbnail(url=str(user.avatar_url))
                            
                        if fver in member.roles or mver in member.roles or otherver in member.roles:
                            normalembed.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                        else:
                            normalembed.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                        normalembed.add_field(name="Age", value=info["Age"], inline=True)
                        normalembed.add_field(name="Gender", value=info["gender"], inline=True)
                        
                        normalembed.add_field(name="Interests",value=interestString, inline=False)
                        #"field works")
                        normalembed.add_field(name="Location", value=info["location"], inline=True)
                        
                        normalembed.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                        normalembed.add_field(name="About Me", value=info["bio"], inline=False)
                        
                        normalembed.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                    if "gold" in colorcode.content.lower():
                        normalembed = discord.Embed(title=f"Finesse Profile bot",description=f"**Discord User**:{full} **Gender:** {info['gender']} **Age:** {info['Age']}", color=0xcfc272)
                        normalembed.set_author(name=f"{user.id}")
                        if "imageurl" in info:
                            
                            normalembed.set_thumbnail(url=str(info["imageurl"]))
                        if "imageurl" not in info:
                            normalembed.set_thumbnail(url=str(user.avatar_url))
                            
                        if fver in member.roles or mver in member.roles or otherver in member.roles:
                            normalembed.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                        else:
                            normalembed.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                        normalembed.add_field(name="Age", value=info["Age"], inline=True)
                        normalembed.add_field(name="Gender", value=info["gender"], inline=True)
                        
                        #"field works")
                        normalembed.add_field(name="Interests",value=interestString, inline=False)
                        normalembed.add_field(name="Location", value=info["location"], inline=True)
                        
                        normalembed.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                        normalembed.add_field(name="About Me", value=info["bio"], inline=False)
                        
                        normalembed.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")

                    #"footter works")
                    #If for sending normals
                    mes = await newchan.send(f"{user.mention}",embed=normalembed)
                    await user.send("Your profile has been saved and posted!.")
                        
                    with open(path, "r+") as f:
                        info = json.load(f)
                        
                        f.seek(0)  
                        json.dump(info, f,indent=4)
                        f.truncate()

                    
                    with open(path2, "r+") as write:
                        timewait = {"cooled": "false"}
                        write.seek(0)  
                        json.dump(timewait, write)
                        write.truncate()

                        await asyncio.sleep(57600)
                        timewait = {"cooled": "true"}
                        with open(path2, "r+") as write:
                            write.seek(0)  
                            json.dump(timewait, write)
                            write.truncate()
                    return



                            
                                    
                        
                if finesselite not in member.roles and finboost in member.roles:


                            
                    await user.send("What Color Do You Wish Your Profile To Have? Select From The Following: \n Red \n Pink \n Blue \n Purple \n Green \n Yellow(respond with red, pink, blue, purple, green, yellow)")
                    colorcode = await self.bot.wait_for("message",check=check)
                    

                    with open(path, "r+") as info:
                        info = json.load(info)

                    if "pink" in colorcode.content.lower():
                        #"work damn you")

                        #
                        charm = discord.Embed(title=f"Finesse Profile bot",description=f"**Discord User**:{full} **Gender:** {info['gender']} **Age:** {info['Age']}", color=0xff89ff)
                        #"normal  works")
                        charm.set_author(name=f"{user.id}")
                        #"author  works")
                        if "imageurl" in info:
                            
                            charm.set_thumbnail(url=str(info["imageurl"]))
                        if "imageurl" not in info:
                            charm.set_thumbnail(url=str(user.avatar_url))
                            
                        if fver in member.roles or mver in member.roles or otherver in member.roles:
                            charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                        else:
                            charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                        charm.add_field(name="Age", value=info["Age"], inline=True)
                        charm.add_field(name="Gender", value=info["gender"], inline=True)
                        charm.add_field(name="Interests",value=interestString, inline=False)
                        charm.add_field(name="Location", value=info["location"], inline=True)
                        
                        charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                        charm.add_field(name="About Me", value=info["bio"], inline=False)
                        
                        charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                        #"footer works")
                        mes = await newchan.send(f"{user.mention}",embed=normalembed)
                        await user.send("Your profile has been saved and posted!.")
                        with open(path, "r+") as f:
                            info = json.load(f)
                            
                            f.seek(0)  
                            json.dump(info, f,indent=4)
                            f.truncate()

                            
                    if "yellow" in colorcode.content.lower():
                        with open(path, "r+") as info:
                            info = json.load(info)

                        #
                        charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0xfff595)
                        charm.set_author(name=f"{user.id}")
                        #"author  works")
                        if "imageurl" in info:
                            
                            charm.set_image(url=str(info["imageurl"]))
                        if "imageurl" not in info:
                            charm.set_image(url=str(user.avatar_url))
                            
                        if fver in member.roles or mver in member.roles or otherver in member.roles:
                            charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                        else:
                            charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                        charm.add_field(name="Age", value=info["Age"], inline=True)
                        charm.add_field(name="Gender", value=info["gender"], inline=True)
                        charm.add_field(name="Interests",value=interestString, inline=False)
                        charm.add_field(name="Location", value=info["location"], inline=True)
                        
                        charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                        charm.add_field(name="About Me", value=info["bio"], inline=False)
                        
                        charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                        mes = await newchan.send(f"{user.mention}",embed=normalembed)
                        await user.send("Your profile has been saved and posted!. been saved and posted!.")
                        with open(path, "r+") as f:
                            info = json.load(f)
                            
                            f.seek(0)  
                            json.dump(info, f,indent=4)
                            f.truncate()
                            

                    if "green" in colorcode.content.lower():
                        with open(path, "r+") as info:
                            info = json.load(info)
                        # 
                        charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0x6aff8d)
                        charm.set_author(name=f"{user.id}")
                        #"author  works")
                        if "imageurl" in info:
                            
                            charm.set_image(url=str(info["imageurl"]))
                        if "imageurl" not in info:
                            charm.set_image(url=str(user.avatar_url))
                            
                        if fver in member.roles or mver in member.roles or otherver in member.roles:
                            charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                        else:
                            charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990>**Not Verified** <:zplayroom_x:585586357783756820>", inline=True)
                        charm.add_field(name="Age", value=info["Age"], inline=True)
                        charm.add_field(name="Gender", value=info["gender"], inline=True)
                        charm.add_field(name="Interests",value=interestString, inline=False)
                        charm.add_field(name="Location", value=info["location"], inline=True)
                        
                        charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                        charm.add_field(name="About Me", value=info["bio"], inline=False)
                        
                        charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")

                        await newchan.send(f"{user.mention}",embed=charm)
                        await user.send("Your profile has been saved and posted!.")
                        
                        with open(path, "r+") as f:
                            info = json.load(f)
                            
                            f.seek(0)  
                            json.dump(info, f,indent=4)
                            f.truncate()

                    if "purple" in colorcode.content.lower():
                        with open(path, "r+") as info:
                            info = json.load(info)
                        #
                        charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0xc1a7ff)
                        charm.set_author(name=f"({user.id})")
                        #"author  works")
                        if "imageurl" in info:
                            
                            charm.set_image(url=str(info["imageurl"]))
                        if "imageurl" not in info:
                            charm.set_image(url=str(user.avatar_url))
                            
                        if fver in member.roles or mver in member.roles or otherver in member.roles:
                            charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                        else:
                            charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                        charm.add_field(name="Age", value=info["Age"], inline=True)
                        charm.add_field(name="Gender", value=info["gender"], inline=True)
                        charm.add_field(name="Interests",value=interestString, inline=False)
                        charm.add_field(name="Location", value=info["location"], inline=True)
                        
                        charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                        charm.add_field(name="About Me", value=info["bio"], inline=False)
                        
                        charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                        await newchan.send(f"{user.mention}",embed=charm)
                        await user.send("Your profile has been saved and posted!.")
                        with open(path, "r+") as f:
                            info = json.load(f)
                            
                            f.seek(0)  
                            json.dump(info, f,indent=4)
                            f.truncate()

                    if "red" in colorcode.content.lower():
                        with open(path, "r+") as info:
                            info = json.load(info)
                        #
                        charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0xff656d)
                        charm.set_author(name=f"{user.id}")
                        #"author  works")
                        if "imageurl" in info:
                            
                            charm.set_image(url=str(info["imageurl"]))
                        if "imageurl" not in info:
                            charm.set_image(url=str(user.avatar_url))
                            
                        if fver in member.roles or mver in member.roles or otherver in member.roles:
                            charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                        else:
                            charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                        charm.add_field(name="Age", value=info["Age"], inline=True)
                        charm.add_field(name="Gender", value=info["gender"], inline=True)
                        charm.add_field(name="Interests",value=interestString, inline=False)
                        charm.add_field(name="Location", value=info["location"], inline=True)
                        
                        charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                        charm.add_field(name="About Me", value=info["bio"], inline=False)
                        
                        charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                        await newchan.send(f"{user.mention}",embed=charm)
                        await user.send("Your profile has been saved and posted!.")
                        with open(path, "r+") as f:
                            info = json.load(f)
                            
                            f.seek(0)  
                            json.dump(info, f,indent=4)
                            f.truncate()

                    if "blue" in colorcode.content.lower():
                        with open(path, "r+") as info:
                            info = json.load(info)
                        #
                        charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0x8fd2ff)
                        charm.set_author(name=f"{user.id}")
                        #"author  works")
                        if "imageurl" in info:
                            
                            charm.set_image(url=str(info["imageurl"]))
                        if "imageurl" not in info:
                            charm.set_image(url=str(user.avatar_url))
                            
                        if fver in member.roles or mver in member.roles or otherver in member.roles:
                            charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                        else:
                            charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                        
                        #"image works")
                        charm.add_field(name="Age", value=info["Age"], inline=True)
                        charm.add_field(name="Gender", value=info["gender"], inline=True)
                        charm.add_field(name="Interests",value=interestString, inline=False)
                        charm.add_field(name="Location", value=info["location"], inline=True)
                        
                        charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                        charm.add_field(name="About Me", value=info["bio"], inline=False)
                        
                        charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                        await newchan.send(f"{user.mention}",embed=charm)
                        await user.send("Your profile has been saved and posted!.")
                        with open(path, "r+") as f:
                            info = json.load(f)
                            
                            f.seek(0)  
                            json.dump(info, f,indent=4)
                            f.truncate()
                    with open(path2, "w+") as write:
                        timewait = {"cooled": "false"}
                        write.seek(0)  
                        json.dump(timewait, write)
                        write.truncate()

                        await asyncio.sleep(28800)
                        timewait = {"cooled": "true"}
                        with open(path2, "w+") as write:
                            write.seek(0)  
                            json.dump(timewait, write)
                            write.truncate()
                    return

                    
                if finesselite in member.roles:
                    with open(path, "r+") as st:
                        info = json.load(st)
                    for x in range(4):
                        if x == 4:
                            await user.send("This Isnt Working, Retry The Command And Contact A Developer")
                            return
                        await user.send("What color do you wish your profile embed to have?, find a color hex,copy the hex and paste it here without the hashtag, eg `74ff00` from `#74ff00` \nhttps://htmlcolorcodes.com/color-picker/\n Red: ff656d\n Pink: ff89ff\n Blue: 8fd2ff\n Purple: c1a7ff\n Green: 6aff8d\n Yellow: fff595\n ")
                        #"sends the color message")
                        colorcode = await self.bot.wait_for("message", check=check)
                        smh = f"0x{colorcode.content}"
                        try:
                            color = discord.Colour(int(smh, 16))
                        except Exception as e:
                            #f"Color Convert Has Failed, Reason == {e}")
                            await user.send("Color Convert Failed, Try Again")
                            continue
                        else:
                            break
                    charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=color)
                    #"original works")
                    charm.set_author(name=f"{user.name}, {user.id}")
                    #"author works")
                    if "imageurl" in info:
                        
                        charm.set_image(url=str(info["imageurl"]))
                    if "imageurl" not in info:
                        charm.set_image(url=str(user.avatar_url))
                        
                    if fver in member.roles or mver in member.roles or otherver in member.roles:
                        charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                    else:
                        charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                    #"thumbnail works")
                    charm.add_field(name="Age", value=info["Age"], inline=True)
                    charm.add_field(name="Gender", value=info["gender"], inline=True)
                    charm.add_field(name="Interests",value=interestString, inline=False)
                    charm.add_field(name="Location", value=info["location"], inline=True)
                    
                    charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                    charm.add_field(name="About Me", value=info["bio"], inline=False)
                    
                    charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                    color = colorcode.content
                    #"embed works")
                    await newchan.send(f"{user.mention}",embed=charm)
                    await user.send("Your profile has been saved and posted!.")
                    with open(path, "r+") as f:
                        info = json.load(f)
                        
                        f.seek(0)  
                        json.dump(info, f,indent=4)
                        f.truncate()
                        
                    with open(path2, "w+") as write:
                        timewait = {"cooled": "false"}
                        write.seek(0)  
                        json.dump(timewait, write)
                        write.truncate()

                        await asyncio.sleep(14400)
                        timewait = {"cooled": "true"}
                        with open(path2, "w+") as write:
                            write.seek(0)  
                            json.dump(timewait, write)
                            write.truncate()
                    return


                normalembed = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0x80646b)
                #"original works")
                normalembed.set_author(name=f"{user.id}")
                #"author works")
                if "imageurl" in info:
                    normalembed.set_thumbnail(url=str(info["imageurl"]))
                if "imageurl" not in info:
                    normalembed.set_thumbnail(url=str(user.avatar_url))
                
                    
                if fver in member.roles or mver in member.roles or otherver in member.roles:
                    normalembed.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                else:
                    normalembed.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                #"thumbnail works")
                normalembed.add_field(name="Age", value=info["Age"], inline=True)
                normalembed.add_field(name="Gender", value=info["gender"], inline=True)
                
                #"field works")
                normalembed.add_field(name="Interests",value=interestString, inline=False)
                normalembed.add_field(name="Location", value=info["location"], inline=True)
                
                normalembed.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                normalembed.add_field(name="About Me", value=info["bio"], inline=False)
                
                normalembed.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                #"footter works")
                #If for sending normals
                await newchan.send(f"{user.mention}",embed=charm)
                await user.send("Your profile has been saved and posted!.")
                
                with open(path, "r+") as f:
                    info = json.load(f)
                    
                    f.seek(0)  
                    json.dump(info, f,indent=4)
                    f.truncate()
                    
            
                
            
                #"shad u did it so proud")
                path = os.path.join("/home/shadbot/prof_data/", f"{user.id}.json")
            
                with open(path2, "w+") as write:
                    timewait = {"cooled": "false"}
                    json.dump(timewait, write)
        
                await asyncio.sleep(57600)
                timewait = {"cooled": "true"}
                with open(path2, "w+") as write:
                    json.dump(timewait, write)
                return


    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if payload.emoji.id == 647803697530929152:
                await message.remove_reaction(payload.emoji, member)
                path = os.path.join("/home/shadbot/prof_data/", f"{user.id}.json")
                exist = os.path.exists(path) # Edit Function -------------------------
                #"right emoji")
                if not exist:
                    await user.send("You Have Not Created A Profile, Check <#615342434146058252>")
                    return
                otherver = finesse.get_role(593699293316120584)
                with open(path,"r+") as f:
                    info = json.load(f)
                if otherver in member.roles:
                    charm = discord.Embed(description=f"Please Send Your Selfie {user.name}!, You Have 15 Minutes To Choose", color=0xff89ff)
                    charm.set_author(name="Finesse")
                    await user.send(embed=charm)
                    img = await self.bot.wait_for("message", check=check, timeout=900.00)
                    #"msg ttaken")
                    if img.attachments:
                        #"It Is A IMage")
                        resp = discord.Embed(description="Good Work!, Please Wait While We Finish Up!")
                        await user.send(embed=resp)
                        #"Embed Works")
                        imgfile = img.attachments[0]
                        #"imgfil dont work")
                        imglink = imgfile.url
                        #"Works")
                        with open(path, "r+") as f:
                            data = json.load(f)
                            data["imageurl"] = f"{str(imglink)}"
                            f.seek(0)  
                            json.dump(data, f,indent=4)
                            f.truncate()
                                
                    else:
                        fail = discord.Embed(description="Thats Not A Image!, You Need To Rerun This Command Now! Check <#615342434146058252>")
                        await user.send(embed=fail)
                        return

                if fver in member.roles:
                    charm = discord.Embed(description=f"Please Send Your Selfie {user.name}!, You Have 15 Minutes To Choose", color=0xff89ff)
                    charm.set_author(name="Finesse")
                    await user.send(embed=charm)
                    img = await self.bot.wait_for("message", check=check, timeout=900.00)
                    #"msg ttaken")
                    if img.attachments:
                        #"It Is A IMage")
                        resp = discord.Embed(description="Good Work!, Please Wait While We Finish Up!")
                        await user.send(embed=resp)
                        #"Embed Works")
                        imgfile = img.attachments[0]
                        #"imgfil dont work")
                        imglink = imgfile.url
                        #"Works")
                        with open(path, "r+") as f:
                            data = json.load(f)
                            data["imageurl"] = f"{str(imglink)}"
                            f.seek(0)  
                            json.dump(data, f,indent=4)
                            f.truncate()
                                
                    else:
                        fail = discord.Embed(description="Thats Not A Image!, You Need To Rerun This Command Now! Check <#615342434146058252>")
                        await user.send(embed=fail)
                        return

                if mver in member.roles:
                    charm = discord.Embed(description=f"Please Send Your Selfie {user.name}!, You Have 15 Minutes To Choose,(Do Not Delete The Photo After)", color=0xff89ff)
                    charm.set_author(name="Finesse")
                    await user.send(embed=charm)
                    img = await self.bot.wait_for("message", check=check, timeout=900.00)
                    if img.attachments:
                        resp = discord.Embed(description="Good Work!, Please Wait While We Finish Up!")
                        imgfile = img.attachments[0]
                        imglink = imgfile.url
                        with open(path, "r+") as f:
                            data = json.load(f)
                            data["imageurl"] = f"{str(imglink)}"
                            f.seek(0)  
                            json.dump(data, f,indent=4)
                            f.truncate()
                    else:
                        fail = discord.Embed(description="Thats Not A Image!, You Need To Rerun This Command Now! Check <#592072362376167425>")
                        await user.send(embed=fail)
                        return
                
                if fver not in member.roles and mver not in member.roles and otherver not in member.roles:
                    fail = discord.Embed(description="You Are Not Verified And Can Not Upload Images")
                    await user.send(embed=fail)
                    return

                
                await user.send("Selfie Uploaded!")
                
                return
                

                    

                #-------------------------------------------------------------------------------------------------------------------------------------------
            if payload.emoji.id == 647803625736765440:
                await message.remove_reaction(payload.emoji, member)
                path = os.path.join("/home/shadbot/prof_data/", f"{user.id}.json")
                exist = os.path.exists(path) # Edit Function -------------------------
                #"right emoji")
                if not exist:
                    await user.send("You Have Not Created A Profile, Check <#615342434146058252>")
                    return
                
                charm = discord.Embed(description=f"React With The Corresponding Emoji, What You Wish To Edit. You Have 2 Minutes To Choose A Category", color=0xff89ff)
                charm.set_author(name=f"{user.id}")
                charm.set_thumbnail(url=str(user.avatar_url))
                charm.add_field(name="Name", value=":one:")
                charm.add_field(name="Reload Base Roles(Only Choose This If You Changed Your Roles That Are Displayed On Your Profile)", value=":two:")
                charm.add_field(name="Biography", value=":three:")
                charm.add_field(name="Hobbies", value=":four:")
                charm.add_field(name="Location", value=":five:")
                editmsg = await user.send(embed=charm)
                await editmsg.add_reaction(emoji="1\N{combining enclosing keycap}")
                await editmsg.add_reaction(emoji="2\N{combining enclosing keycap}")
                await editmsg.add_reaction(emoji="3\N{combining enclosing keycap}")
                await editmsg.add_reaction(emoji="4\N{combining enclosing keycap}")
                await editmsg.add_reaction(emoji="5\N{combining enclosing keycap}")
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", check=reaction_check(message=editmsg, emoji=[f"{i}\N{combining enclosing keycap}" for i in range(1,6)], author=user), timeout=120.00)
                except asyncio.TimeoutError:
                    await user.send("You Ran Out Of Time")
                else: # NAME 
                    if str(reaction.emoji) == "1\N{combining enclosing keycap}":
                        await user.send("What do you want your new name to be?.")
                        namechange = await self.bot.wait_for("message", check=check)
                        with open(path, "r+") as dat:
                            data = json.load(dat)
                            data["name"] = f"{namechange.content}"
                            dat.seek(0)  
                            json.dump(data, dat)
                            dat.truncate()
                        await user.send("Data Sucessfully Saved!")
                    #SEXUAL PREFERENCE
                    if str(reaction.emoji) == "2\N{combining enclosing keycap}":
                        editmsg = await user.send("Reloading Roles Now!..")
                        member = finesse.get_member(user.id)
                        finboost = finesse.get_role(585530183717748752)
                        finesselite = finesse.get_role(515567432799092737)
                        fver = finesse.get_role(593699295656542213)
                        mver = finesse.get_role(593699291722416129)
                        male = finesse.get_role(547823326689493012)
                        female = finesse.get_role(547923211699093532)
                        other = finesse.get_role(547851482045874178)
                        open1 = finesse.get_role(583713696543408167)
                        closed = finesse.get_role(583714006938681405)
                        ask = finesse.get_role(583713937598709822)
                        await editmsg.edit(content="Reloading Roles Now!...",suppress=True)
                        gender = "n/a"
                        age = 'n/a'
                        dm = "n/a"
                        if female in member.roles:
                            gender = "Female"

                        if male in member.roles:
                            gender = "Male"

                        if other in member.roles:
                            await user.send("Please Reply With Your Gender")
                            gender_event = await self.bot.wait_for("message",check=check)
                            gender = gender_event.content
                        role_id_list = [role.id for role in member.roles]
                        dm_status_list = [role.name for role in finesse.roles if role.name.startswith("DM |") and role.id in role_id_list]
                        dm = dm_status_list[0]
                        await user.send("What Age Are You")
                        ageGen = await self.bot.wait_for("Message",check=check)
                        age = ageGen.content

                        await editmsg.edit(content="Reloading Roles Now!....",suppress=True)
                        with open(path, "r+") as dat:
                            data = json.load(dat)
                            data["gender"] = gender
                            data["DM Status"] = dm
                            data["Age"] = age
                            dat.seek(0)  
                            json.dump(data, dat)
                            dat.truncate()
                        await editmsg.edit(content="Roles Are Reloaded!",suppress=True)
                        return
                        #BIOGRAPHY
                    if str(reaction.emoji) == "3\N{combining enclosing keycap}":
                        for x in range(4):
                            if x == 4:
                                await user.send("You Are struggling too hard with this, retry later")
                            await user.send("Please Write A New Biography, Under 200 Characters")
                            bio = await self.bot.wait_for("message", check=check)
                            if len(bio.content) > 200:
                                await user.send("Too Long!, Retry This Command To Change Your Bio Again!")
                                continue
                            else:
                                break

                        with open(path, "r+") as dat:
                            data = json.load(dat)
                            data["bio"] = f"{bio.content}"
                            dat.seek(0)  
                            json.dump(data, dat)
                            dat.truncate()
                        await user.send("Data Sucessfully Saved!")    
                        #HOBBIES
                    if str(reaction.emoji) == "4\N{combining enclosing keycap}":
                        await user.send("What Are Your Hobbies?")
                        change = await self.bot.wait_for("message", check=check)
                        with open(path, "r+") as dat:
                            data = json.load(dat)
                            data["hobbies"] = f"{change.content}"
                            dat.seek(0)  
                            json.dump(data, dat)
                            dat.truncate()
                        await user.send("Data Sucessfully Saved!")

                    if str(reaction.emoji) == "5\N{combining enclosing keycap}":
                        await user.send("what Is Your Current Location(Where Do You Live)")
                        change = await self.bot.wait_for("message", check=check)
                        with open(path, "r+") as dat:
                            data = json.load(dat)
                            data["location"] = f"{change.content}"
                            dat.seek(0)  
                            json.dump(data, dat)
                            dat.truncate()
                        await user.send("Data Sucessfully Saved!")
            #CUSTOMIZE FUNCTION

                
                    

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 615342434146058252:
            if message.content != ".start":
                await message.delete()


    @commands.Cog.listener()
    async def on_member_remove(self,member):
        #Checks if they made a profile before
        exist = os.path.exists(f"/home/shadbot/prof_data/{member.id}")
        if exist:
            finesse = self.bot.get_guild(534050853477285888)
            
            newchan = finesse.get_channel(566474557834395659)

            
            async for message in newchan.history(limit=500):
                embed = message.embed[0]
                if member.id in embed.author.name:
                    await message.delete()
    
            #"Purged.exe")
        
        



    @commands.command()
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395)
    async def resetme(self,ctx):
        path = os.path.join("/home/shadbot/prof_data", f"{ctx.author.id}.json")
        #path)
        exist = os.path.exists(path)
        if exist:
            os.remove(path)
            await ctx.send("Data Deleted For User")
        elif not exist:
            await ctx.send("This Person Does Not Have Any Profile Data")

    @commands.command()
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395)
    async def profilereset(self,ctx, uid):
        path = os.path.join("/home/shadbot/prof_data", f"{uid}.json")
        #path)
        exist = os.path.exists(path)
        if exist:
            os.remove(path)
            await ctx.send("Data Deleted For User")
        elif not exist:
            await ctx.send("This Person Does Not Have Any Profile Data")







    @commands.command()
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395)
    async def display(self,ctx, uid):
        try:
            with open(f"/home/shadbot/prof_data/{uid}") as f:
                data = json.load(f)
        except Exception as e:
            await ctx.send(f"Error Happened: {e}")
            return
        finally:
            await ctx.send(f"data== ```{data}")


        


    @commands.command()
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395)
    async def resetall(self,ctx):
        for files in os.listdir(f"/home/shadbot/bump_check/"):
            source = "/home/shadbot/bump_check" + "/" + files
            with open(source, "r+") as f:
                data = json.load(f)
                time = {"cooled": "true"}
                f.seek(0)
                json.dump(time, f,indent=4)
                f.truncate()
        await ctx.send("Reset Done!")

    @commands.command()
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395)
    async def gon(self,ctx, uid = int):
        path = os.path.join("/home/shadbot/bump_check/", f"{uid}.json")
        exist = os.path.exists(path)
        if exist:
            os.remove(path)
            await ctx.send("Data Deleted For User")
        elif not exist:
            await ctx.send("This Person Does Not Have Any Profile Data")

    @commands.command()
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395)
    async def ireset(self,ctx, uid: int):
            source = f"/home/shadbot/bump_check/{uid}.json"
            try:

                with open(source, "r+") as f:
                    data = json.load(f)
                    time = {"cooled": "true"}
                    f.seek(0)
                    json.dump(time, f,indent=4)
                    f.truncate()
                await ctx.send("Reset Done!")
            except Exception as e:
                await ctx.send("Error Occured : {}".format(e))


    @commands.command()
    @commands.has_any_role("Male", "Female", "Other Gender")
    @commands.has_any_role("Likes Sports", "Likes Coding", "Likes Gaming",
                            "Likes Technology","Likes Fashion","Likes Photography",
                            "Likes Music","Likes Literature","Likes Movies/TV",
                            "Likes Anime","Likes Singing","Likes Art")
    @commands.has_any_role("Europe", "United States", "Latin America", "Middle East", "Canada", "Asia","Africa","Oceania")
    @commands.has_any_role("Dm's ~ Open", "Dm's ~ Ask", "Dm's ~ Closed")
    async def start(self,ctx):
        
        await ctx.message.delete()
        def check(m):
                return isinstance(m.channel, discord.abc.PrivateChannel) and m.author.id == ctx.author.id
        colorcode = "none"
        color1 = "n/a"
        #VERY IMPORTANT INFO
        user = self.bot.get_user(ctx.author.id)
        finesse = self.bot.get_guild(534050853477285888)
        member = finesse.get_member(ctx.author.id)
        path2 = f"/home/shadbot/bump_check/{ctx.author.id}.json"

  
        user_interests = [role for role in finesse.roles if role.name.startswith("Likes") and role in member.roles]
        interests_names = [i.name[6:] for i in user_interests]
        interestString = " ,".join(interests_names)


        #ERROR HANDLER MINI
        
        if profile_exist_check is not None:
            error_embed = discord.Embed(
                title="Error!",
                description="You have already made a profile. try bumping instead or ask a staff to remove your profile if you think this is a error.",
                color=discord.Color.teal())
            await member.send(embed=error_embed)
            return
        


        #basic info

        
        full = f"{user.name}#{user.discriminator}, <@{user.id}>"
        intro_channel = finesse.get_channel(566474557834395659)
        
        
        #charm roles
        #C H A R M 
        finboost = finesse.get_role(585530183717748752)
        finesselite = finesse.get_role(515567432799092737)
        roles = {
            "female_verified": 593699295656542213,
            "male_verified": 593699291722416129,
            "other_verified": 593699293316120584,
            "male": 547823326689493012,
            "female": 547923211699093532,
            "other": 547851482045874178,
        }   

        #selfie verified roles
        fver = finesse.get_role(593699295656542213)
        mver = finesse.get_role(593699291722416129)
        otherver = finesse.get_role(593699293316120584)
        #age roles
        #gender roles 
        male = finesse.get_role(547823326689493012)
        female = finesse.get_role(547923211699093532)
        other = finesse.get_role(547851482045874178)

        newchan = finesse.get_channel(566474557834395659)

        #dm status
        
        # Age role
        
        dm_roles = ",".join((role.name) for role in finesse.roles if role.name.startswith("Dm's ~") and role in member.roles) # gets all dm status roles in members rolelist
       
    # -----------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------
        if finboost in member.roles:


            await user.send("What Color Do You Wish Your Profile To Have? Select From The Following: \n Red \n Pink \n Blue \n Purple \n Green \n Yellow")

            

            #"sends user message1")

            color1 = await self.bot.wait_for("message", check=check)
            #"sends user message2")
            await user.send("What Is Your Name?")

            name = await self.bot.wait_for("message", check=check)
            
            
        
                
            await user.send("What Are Your Hobbies?")
            hob = await self.bot.wait_for("message", check=check)
            
            for x in range(4):
                if x == 4:
                    await user.send("You Are struggling too hard with this, retry later")
                await user.send("Tell Us A Bit About Yourself!(200 Character Max)")
                bio = await self.bot.wait_for("message", check=check)
                if len(bio.content) > 200:
                    await user.send("Too Long!, Retry This Command To Change Your Bio Again!")
                    continue
                else:
                    break
            await user.send("Where Are You From?")
            locations = await self.bot.wait_for("message", check=check)
            #"all questions asked")

            age = "N/A"
            
            gender = "N/A"
            dm = "N/A"
            
            namcon = name.content
            
            
                
            biocon = bio.content
            hobcon = hob.content
            locationcon = locations.content
            colorcon = color1.content
            #"poss1")

            # charm
            await user.send("What Age Are You")
            ageGen = await self.bot.wait_for("Message",check=check)
            age = ageGen.content


            #"poss2")

            # Gender
            if female in member.roles:
                gender = "Female"

            if male in member.roles:
                gender = "Male"

            if other in member.roles:
                await user.send("Please Reply With Your Gender")
                gender_event = await self.bot.wait_for("message",check=check)
                gender = gender_event.content
            #"poss3")

            
            #"poss5")

            # DM Status
            dm = dm_roles
            #"poss6")
            info_list = [namcon,gender,hobcon,biocon,age,locationcon]
            for string in info_list:
                mystr = string.lower()
                wordList = re.sub("[^\w]", " ",  mystr).split()
                for mes in wordList:
                    if mes in self.banned_words:
                        await user.send(f"You Used A Banned Word, Please Redo The Command Without the Following word: {mes}")
                        return
                    else:
                        continue
            # F I N I S H E D
            info = {"name": namcon,
                    "gender": gender,
                    "interests": interests_names,
                    
                    "hobbies": hobcon,
                    "bio": biocon,
                    "Age": age,
                    
                    
                    "location": locationcon,
                    "DM Status": dm,
                    "color": colorcon,
                    "time": int(tx.time())
                    }
     
        

            if "pink" in color1.content.lower():
                #"work damn you")

                #
                
                charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0xff89ff)
                charm.set_author(name=f"{ctx.author.id}")
                #"author  works")
                charm.set_image(url=str(ctx.author.avatar_url))
                #"image works")
                if fver in member.roles or mver in member.roles or otherver in member.roles:
                    charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                else:
                    charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                charm.add_field(name="Age", value=info["Age"], inline=True)
                charm.add_field(name="Gender", value=info["gender"], inline=True)
                charm.add_field(name="Interests",value=interestString, inline=False)
                
                charm.add_field(name="Location", value=info["location"], inline=True)
                
                charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                charm.add_field(name="About Me", value=info["bio"], inline=False)
                
                charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                #"footer works")
                await newchan.send(f"{user.mention}",embed=charm)
                await user.send("Your profile has been saved and posted!.")
                
                

                    
            if "yellow" in color1.content.lower():

                #
                charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0xfff595)
                charm.set_author(name=f"{ctx.author.id}")
                charm.set_image(url=str(ctx.author.avatar_url))
                if fver in member.roles or mver in member.roles or otherver in member.roles:
                    charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                else:
                    charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                charm.add_field(name="Age", value=info["Age"], inline=True)
                charm.add_field(name="Gender", value=info["gender"], inline=True)
                charm.add_field(name="Interests",value=interestString, inline=False)
                charm.add_field(name="Location", value=info["location"], inline=True)
                
                charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                charm.add_field(name="About Me", value=info["bio"], inline=False)
                
                charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                await newchan.send(f"{user.mention}",embed=charm)
                await user.send("Your profile has been saved and posted!.")

                

                    

            if "green" in color1.content.lower():

                # 
                charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0x6aff8d)
                charm.set_author(name=f"{ctx.author.id}")
                charm.set_image(url=str(ctx.author.avatar_url))
                
                    
                if fver in member.roles or mver in member.roles or otherver in member.roles:
                    charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                else:
                    charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                charm.add_field(name="Age", value=info["Age"], inline=True)
                charm.add_field(name="Gender", value=info["gender"], inline=True)
                charm.add_field(name="Interests",value=interestString, inline=False)
                charm.add_field(name="Location", value=info["location"], inline=True)
                
                charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                charm.add_field(name="About Me", value=info["bio"], inline=False)
                
                charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                await newchan.send(f"{user.mention}",embed=charm)
                await user.send("Your profile has been saved and posted!.")
                

            if "purple" in color1.content.lower():
                #
                charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0xc1a7ff)
                charm.set_author(name=f"{ctx.author.id}")
                charm.set_image(url=str(ctx.author.avatar_url))
                
                    
                if fver in member.roles or mver in member.roles or otherver in member.roles:
                    charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                else:
                    charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                charm.add_field(name="Age", value=info["Age"], inline=True)
                charm.add_field(name="Gender", value=info["gender"], inline=True)
                charm.add_field(name="Interests",value=interestString, inline=False)
                charm.add_field(name="Location", value=info["location"], inline=True)
                
                charm.add_field(name="About Me", value=info["bio"], inline=False)
                
                charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                await newchan.send(f"{user.mention}",embed=charm)
                await user.send("Your profile has been saved and posted!.")

            if "red" in color1.content.lower():

                #
                charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0xff656d)
                charm.set_author(name=f"{ctx.author.id}")
                charm.set_image(url=str(ctx.author.avatar_url))
                
                    
                if fver in member.roles or mver in member.roles or otherver in member.roles:
                    charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                else:
                    charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                charm.add_field(name="Age", value=info["Age"], inline=True)
                charm.add_field(name="Gender", value=info["gender"], inline=True)
                charm.add_field(name="Interests",value=interestString, inline=False)
                charm.add_field(name="Location", value=info["location"], inline=True)
                
                charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                charm.add_field(name="About Me", value=info["bio"], inline=False)
                
                charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                await newchan.send(f"{user.mention}",embed=charm)
                await user.send("Your profile has been saved and posted!.")
                
                    

            if "blue" in color1.content.lower():

                #
                charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0x8fd2ff)
                charm.set_author(name=f"{ctx.author.id}")
                charm.set_image(url=str(ctx.author.avatar_url))
                
                    
                if fver in member.roles or mver in member.roles or otherver in member.roles:
                    charm.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
                else:
                    charm.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
                charm.add_field(name="Age", value=info["Age"], inline=True)
                charm.add_field(name="Gender", value=info["gender"], inline=True)
                charm.add_field(name="Interests",value=interestString, inline=False)
                charm.add_field(name="Location", value=info["location"], inline=True)
                
                charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
                charm.add_field(name="About Me", value=info["bio"], inline=False)
                
                charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
                await newchan.send(f"{user.mention}",embed=charm)
                await user.send("Your profile has been saved and posted!.")
                
                    

            path = os.path.join("/home/shadbot/prof_data/", f"{ctx.author.id}.json")
            with open(path, "w+") as write:
                json.dump(info, write,indent=4)
            #Bump Cooldown
            
            with open(path2, "w") as write:
                timewait = {"cooled": "false"}
                json.dump(timewait, write)


            await asyncio.sleep(28800)
            timewait = {"cooled": "true"}
            with open(path2, "w+") as write:
                json.dump(timewait, write)
            return

        if finesselite in member.roles:
            await user.send("What color do you wish your profile embed to have?, find a color hex,copy the hex and paste it here without the hashtag, eg `74ff00` from `#74ff00` \nhttps://htmlcolorcodes.com/color-picker/\n Red: ff656d\n Pink: ff89ff\n Blue: 8fd2ff\n Purple: c1a7ff\n Green: 6aff8d\n Yellow: fff595\n ")



            #"sends the color message")
            for x in range(4):
                if x == 4:
                    await user.send("You Took Too Many Tries, Redo The Command")
                    return
                colorcode = await self.bot.wait_for("message", check=check)
                try:
                    fincolor = await commands.ColourConverter().convert(ctx, colorcode.content)
                except Exception as e:
                    await user.send("This Is Not A Color")
                    continue
                else:
                    break
                
            #"saved colorcode")
            await user.send("What Is Your Name?")
            name = await self.bot.wait_for("message", check=check)
            #"name saved")
            
            
            
        
                
            await user.send("What Are Your Hobbies?")
            
            hob = await self.bot.wait_for("message", check=check)
            #"hobbies done")
            for x in range(4):
                if x == 4:
                    await user.send("You Are struggling too hard with this, retry later")
                await user.send("Please Write A New Biography, Under 200 Characters")
                bio = await self.bot.wait_for("message", check=check)
                if len(bio.content) > 200:
                    await user.send("Too Long!, Retry This Command To Change Your Bio Again!")
                    continue
                else:
                    break
            
            
            
            
            
            await user.send("Where Are You From?")
            locations = await self.bot.wait_for("message", check=check)
            #"all questions asked")


            gender = "N/A"
            #"gender works")
            dm = "N/A"
            #"dm stat works")
            namcon = name.content
            #"namcon")
            #"prefcn")
            biocon = bio.content
            #"biocon")
            hobcon = hob.content
            #"hobcon")
            locationcon = locations.content
            #"loccon")

            fincolor = await commands.ColourConverter().convert(ctx, colorcode.content)
            #"fincolorcon")
            #"poss1")

            # charm

            await user.send("What Age Are You")
            ageGen = await self.bot.wait_for("Message",check=check)
            age = ageGen.content


            #"poss2")

            # Gender
            if female in member.roles:
                gender = "Female"

            if male in member.roles:
                gender = "Male"

            if other in member.roles:
                await user.send("Please Reply With Your Gender")
                gender_event = await self.bot.wait_for("message",check=check)
                gender = gender_event.content
            #"poss3")

            # Dating Status
            
    

            
            # DM Status
            dm = dm_roles
            #"poss6")

            # F I N I S H E D
            info_list = [namcon,gender,hobcon,biocon,age,locationcon]
            for string in info_list:
                mystr = string.lower()
                wordList = re.sub("[^\w]", " ",  mystr).split()
                for mes in wordList:
                    if mes in self.banned_words:
                        await user.send(f"You Used A Banned Word, Please Redo The Command Without the Following word: {mes}")
                        return
                    else:
                        continue
                
            info = {"name": namcon,
                    "gender": gender,
                    "hobbies": hobcon,
                    "bio": biocon,
                    "interests": interests_names,
                    "Age": age,
                    "location": locationcon,
                    "DM Status": dm,
                    }
            #"dict problem")
            
            #"so proud shad iwuwuwuuw")

            
            
            #"Dumped")
            
            charm = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=fincolor)
            #"original works")
            charm.set_author(name=f" {ctx.author.id}")
            #"author works")
            charm.set_image(url=str(ctx.author.avatar_url))
            #"thumbnail works")
            charm.add_field(name="Age", value=info["Age"], inline=True)
            charm.add_field(name="Gender", value=info["gender"], inline=True)
            charm.add_field(name="Location", value=info["location"], inline=True)
            charm.add_field(name="Interests",value=interestString, inline=False)
            charm.add_field(name="Hobbies", value=info["hobbies"], inline=True)
            charm.add_field(name="About Me", value=info["bio"], inline=False)
            charm.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
            #"embed works")
            await newchan.send(f"{user.mention}",embed=charm)
            await user.send("Your profile has been saved and posted!.")
            
                

            
            path = os.path.join("/home/shadbot/prof_data/", f"{ctx.author.id}.json")
            with open(path, "w") as write:
                json.dump(info, write,indent=4)
            #? Bump Cool down
            with open(path2, "w+") as write:
                timewait = {"cooled": "false"}
                json.dump(timewait, write)

            await asyncio.sleep(14400)
            timewait = {"cooled": "true"}
            with open(path2, "w+") as write:
                json.dump(timewait, write)
            return

            
            

            






        await user.send("What Is Your Name?")
        name = await self.bot.wait_for("message", check=check)
        
        #"sends user message1")

        
        
        
        

        await user.send("What Are Your Hobbies?")
        hob = await self.bot.wait_for("message", check=check)
        for x in range(4):
            if x == 4:
                await user.send("You Are struggling too hard with this, retry later")
            await user.send("Please Write A New Biography, Under 200 Characters")
            bio = await self.bot.wait_for("message", check=check)
            if len(bio.content) > 200:
                await user.send("Too Long!, Retry This Command To Change Your Bio Again!")
                continue
            else:
                break
        await user.send("Where Are You From?")
        locations = await self.bot.wait_for("message", check=check)
        #"all questions asked")

        age = "N/A"
        
        gender = "N/A"
        dm = "N/A"
        
        namcon = name.content
    
            
        

            

            
        biocon = bio.content
        hobcon = hob.content
        locationcon = locations.content
        #"poss1")









        await user.send("What Age Are You")
        ageGen = await self.bot.wait_for("Message",check=check)
        age = ageGen.content



        #Gender
        # Gender
        if female in member.roles:
            gender = "Female"

        if male in member.roles:
            gender = "Male"

        if other in member.roles:
            await user.send("Please Reply With Your Gender")
            gender_event = await self.bot.wait_for("message",check=check)
            gender = gender_event.content

        #Dating Status
        
            
        
        
        #"poss4")

        #sexuality
        

        
        
            
        
            

        
            
        
        
        #"poss5")



        #DM Status
        
        dm = dm_roles
        #"poss6")


        info_list = [namcon,gender,hobcon,biocon,age,locationcon]
        for string in info_list:
            mystr = string.lower()
            wordList = re.sub("[^\w]", " ",  mystr).split()
            for mes in wordList:
                if mes in self.banned_words:
                    await user.send(f"You Used A Banned Word, Please Redo The Command Without the Following word: {mes}")
                    return
                else:
                    continue


        #F I N I S H E D
        info = {"name": namcon,
                "gender": gender,
                "interests": interests_names,
                
                "hobbies": hobcon,
                "bio": biocon,
                "Age": age,
                
                
                "location": locationcon,
                "DM Status": dm
            }
        #"dict problem")
        
        #"so proud shad iwuwuwuuw")

        

        # E M B E D
        normalembed = discord.Embed(title=f"Finesse Profile bot", description=f"**Discord User**:{full} ,**Name:**  {info['name']}", color=0x80646b)
        #"original works")
        normalembed.set_author(name=f"{ctx.author.id}")
        #"author works")
        normalembed.set_thumbnail(url=str(ctx.author.avatar_url))
        
            
        if fver in member.roles or mver in member.roles or otherver in member.roles:
            normalembed.add_field(name="Verification Level", value="<:zfinesse_check:695225075325992990> **Selfie Verified** <:zfinesse_check:695225075325992990>", inline=True)
        else:
            normalembed.add_field(name="Verification Level", value="<:finesse_x:695225262052474921> **Not Verified** <:finesse_x:695225262052474921>", inline=True)
        #"thumbnail works")
        normalembed.add_field(name="Age", value=info["Age"], inline=True)
        normalembed.add_field(name="Gender", value=info["gender"], inline=True)
        #"field works")
        normalembed.add_field(name="Interests",value=interestString, inline=False)
        normalembed.add_field(name="Location", value=info["location"], inline=True)
        
        normalembed.add_field(name="Hobbies", value=info["hobbies"], inline=True)
        normalembed.add_field(name="About Me", value=info["bio"], inline=False)
        
        normalembed.set_footer(text=info["DM Status"], icon_url="https://i.imgur.com/IPPs67V.png")
        #"footter works")
        #If for sending normals
        mes = await newchan.send(f"{user.mention}",embed=normalembed)
        await user.send("Your profile has been saved and posted!.")
        
            

        

        #"shad u did it so proud")
        path = os.path.join("/home/shadbot/prof_data/", f"{ctx.author.id}.json")
        with open(path, "w") as write:
            json.dump(info, write,indent=4)


        with open(path2, "w+") as write:
            timewait = {"cooled": "false"}
            json.dump(timewait, write)

        await asyncio.sleep(172800)
        timewait = {"cooled": "true"}
        with open(path2, "w+") as write:
            json.dump(timewait, write)


            

        
        






    

















        



    @start.error
    async def start_error(self,ctx, error):
        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.message.delete()
            string_roles = " ,".join(error.missing_roles)
            await ctx.author.send("You Cant Use This Command As You Do Not Have Your Roles Set Up, You Also Need One Interest Role, So Make Sure That You Do, For Reference, You Dont Have One Of The Following Roles: \n ``` {}```".format(string_roles))
        else:
            await ctx.message.delete()
            #error)










def setup(bot):
    #"Loading profile command System!")
    bot.add_cog(profiles(bot))
    #"profile command sys loaded")