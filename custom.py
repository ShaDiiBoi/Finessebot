
import random
import os
import json
import shutil
import discord
from pathlib import Path
import asyncio
from discord.ext import commands
from collections.abc import Sequence
import time
import logging
import datetime
import discord
from discord.ext import commands
from collections.abc import Sequence
from urllib.parse import urlparse
import shadsmod
# TODO make sure the url is checked when using images

class custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.error_channel = bot.get_channel(596509055376162831)
    

    @commands.Cog.listener()
    async def on_member_update(self,before,after):
        boost = before.guild.get_role(586494766359904257)
        if boost in before.roles and boost not in after.roles:
                
            folder = f'/home/shadbot/command_data/{after.id}'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
                print("cleared %s's Commands!" % (after.name))


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clearcomms(self,ctx,user):
                     
        folder = f'/home/shadbot/command_data/{user}'
        rolelist = [x.id for x in user.roles]
        if 586494766359904257 in rolelist or 548846050056863756 in rolelist:
            return
        else:

            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            await ctx.send(f"cleared <@{user}>'s Commands!")


    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(548846050056863756,586494766359904257)
    @commands.cooldown(1, 60.0, type=commands.BucketType.user)
    async def cmdlist(self, ctx):
        if not os.path.isdir(f"/home/shadbot/command_data/{ctx.author.id}"):
            await ctx.author.send("You Have No Commands")
            return
        commands_list = []
        for files in os.listdir(f"/home/shadbot/command_data/{ctx.author.id}"):
            commands_list.append(files)
        i = 0

        for thisItem in commands_list:
             commands_list[i] = os.path.splitext(thisItem)[0]
             i = i+1
            

        await ctx.send(f"```css {' ,'.join(commands_list)}```")
            
        

    @commands.command()
    @commands.guild_only()
    @commands.has_any_role(548846050056863756,586494766359904257)
    @commands.cooldown(1, 60.0, type=commands.BucketType.user)
    async def create(self, ctx, comm_name = None):
        
        whitelist = [566474760444182533,566478029644234752,611379940084023296]
        
        comms = self.bot.commands
        comm_name_base = []
        rolelist = [role.id for role in ctx.author.roles]

       
        for x in comms:
            comm_name_base.append(x.name)
        if comm_name in comm_name_base:
            await ctx.send("This Command Is A Finesse Bot Base Command, Use A Different Name Please!")
            return
        if ctx.channel.id not in whitelist:
            await ctx.send("This Is Not A White Listed Channel")
            return
        if not os.path.exists(f"/home/shadbot/command_data/{ctx.author.id}"):
            os.makedirs(f"/home/shadbot/command_data/{ctx.author.id}")
        elif os.path.exists(f"/home/shadbot/command_data/{ctx.author.id}"):
            amount = len([name for name in os.listdir(f"/home/shadbot/command_data/{ctx.author.id}")])
        if amount > 5 and 548846050056863756 not in rolelist:
            await ctx.send("You Cant Create More Than 5 Commands Unless You Donate.")
            return
        if comm_name is None:
            await ctx.send("You Need To Use The Following Syntax: \n `.create <commandname>` where `<commandname>` is the command name")
            return
        exist = os.path.isfile(f"/home/shadbot/command_data/{ctx.author.id}/{comm_name}.json")
        if exist:
            await ctx.send("This Command Name Is Already Registered")
            return
        await ctx.send("Please enter the title of the Embed")
        await ctx.send("You can change use %sender and %target to represent the executor and the person tagged with the command.")
        def check(m):
            return m.author == ctx.message.author and m.channel == ctx.channel

        try:
            title = await self.bot.wait_for('message', timeout=80,check=check)
        except asyncio.TimeoutError:
            await ctx.send("Sorry But Times Up!")
            return
        if "dating" in title.content or "underage dating" in title.content:
            await ctx.send("This Has A Banned Word In It, Please Retry")
            return
        await ctx.send("Please enter the body of the Embed")
        
        await ctx.channel.send("You can change use %sender and %target to represent the executor and the person tagged with the command.")
        try:
            body = await self.bot.wait_for('message', timeout=80,check=check)
        except asyncio.TimeoutError:
            await ctx.channel.send("You took too long! Please try again later.")
            return
        if "dating" in body.content or "underage dating" in body.content:
            await ctx.send("This Has A Banned Word In It, Please Retry")
            return
        member = ctx.guild.get_member(ctx.author.id)
        if ctx.guild.get_role(548846050056863756) in member.roles or ctx.guild.get_role(586494766359904257) in member.roles:
            for x in range(4):
                if x == 4:
                    await ctx.author.send("You Are Struggling With This Too Much, DM <@475304536920031232> For Help")
                    return
                await ctx.send("Please Pick A Color By copying the hex and paste it here, eg `#74ff00` \nhttps://htmlcolorcodes.com/color-picker/")
                colorcode = await self.bot.wait_for("message", check=check)
                try:
                    fincolor = await commands.ColourConverter().convert(ctx, colorcode.content)
                except Exception as e:
                    await ctx.send("This Is Not A Color")
                    continue
                else:
                    break
        #* Functions For Reaction Replys  
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
        
        msg = await ctx.channel.send("Ok, got it. Would you like to have an image on this embed?")
        await msg.add_reaction('\U0001f44d')
        await msg.add_reaction('\U0001f44e')
        try:
            reaction, user = await self.bot.wait_for("reaction_add", check=reaction_check(message=msg, author=ctx.author))
        except asyncio.TimeoutError:
            await ctx.channel.send("You took too long! Please try again later.")
            return
        if str(reaction.emoji) == '👍':
            image_use = True 
            for x in range(4):
                if x == 4:
                    await ctx.channel.send("It is clear this is not working. Try again later.")
                    return
                await ctx.channel.send("OK, please send a link to the image. Image uploading is not supported")
                try:
                    link = await self.bot.wait_for('message', timeout=80,check=check)
                except asyncio.TimeoutError:
                    await ctx.channel.send("You took too long! Please try again later.")
                    return
                        
                url = urlparse(link.content)
                if url.scheme == "":
                    link = f"https://{link.content}"
                if url.scheme == "" and url.netloc == "":
                    await ctx.send("That Isnt A Link!")
                    return
                else:
                    await ctx.send("it works!")
                    break  # Checks headers to see if it is an image.

            url = link.content
        else:
            image_use = False
            url = ""     
        new_command = {  # Creates the dict
            'name': comm_name,
            'title': title.content,
            'body': body.content,
            'creator': ctx.author.id,
            'image': image_use,
            'url': url,
            "unlocked": False
            
        }
        with open(f"/home/shadbot/command_data/{ctx.author.id}/{comm_name}.json", "w+") as datafile:
            json.dump(new_command,datafile)

        if ctx.guild.get_role(548846050056863756) in member.roles or ctx.guild.get_role(586494766359904257) in member.roles:
            with open(f"/home/shadbot/command_data/{ctx.author.id}/{comm_name}.json", "r+") as datafile:
                data = json.load(datafile)
                data["color"] = colorcode.content
                datafile.seek(0)  
                json.dump(data, datafile)
                datafile.truncate()


        await ctx.channel.send("Successfully registered new command.")

    @commands.command()
    @commands.has_any_role(548846050056863756,586494766359904257)
    @commands.cooldown(1, 60.0, type=commands.BucketType.user)
    async def edit(self, ctx, command = None):
        user = ctx.author
        if not command:
            await ctx.send(f"{command} is not a command")
            return
        if os.path.exists(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json"):
                
            def check(m):
                return m.author == ctx.message.author and m.channel.id == ctx.channel.id
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




            
            charm = discord.Embed(description=f"React With The Corresponding Emoji, What You Wish To Edit. You Have 2 Minutes To Choose A Category", color=0xff89ff)
            charm.set_author(name=f"{ctx.author.id}")
            charm.set_thumbnail(url=str(ctx.author.avatar_url))
            charm.add_field(name="Embed Title", value=":one:")
            charm.add_field(name="Embed Description", value=":two:")
            charm.add_field(name="Embed Color", value=":three:")
            charm.add_field(name="Embed Image", value=":four:")
            editmsg = await ctx.send(embed=charm)
            await editmsg.add_reaction(emoji="1\N{combining enclosing keycap}")
            await editmsg.add_reaction(emoji="2\N{combining enclosing keycap}")
            await editmsg.add_reaction(emoji="3\N{combining enclosing keycap}")
            await editmsg.add_reaction(emoji="4\N{combining enclosing keycap}")
            try:
                reaction, user = await self.bot.wait_for("reaction_add", check=reaction_check(message=editmsg, emoji=[f"{i}\N{combining enclosing keycap}" for i in range(1,6)], author=user), timeout=120.00)
            except asyncio.TimeoutError:
                await user.send("You Ran Out Of Time")
            else: # NAME 
                if str(reaction.emoji) == "1\N{combining enclosing keycap}":
                    await ctx.send("What do you want your new Title to be?.")
                    titlechange = await self.bot.wait_for("message", check=check)
                    with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json", "r+") as f:
                        data = json.load(f)
                        data["title"] = titlechange.content
                        f.seek(0)
                        json.dump(data,f)
                        f.truncate()
                    


                #SEXUAL PREFERENCE
                if str(reaction.emoji) == "2\N{combining enclosing keycap}":
                    await ctx.send("What are you changing your embed body to?")
                    sexchange = await self.bot.wait_for("message", check=check)
                    with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json", "r+") as dat:
                        data = json.load(dat)
                        data["body"] = f"{sexchange.content}"
                        dat.seek(0)  
                        json.dump(data, dat)
                        dat.truncate()
                    print("saved")
                    await ctx.send("Data Sucessfully Saved!")

                    #BIOGRAPHY
                if str(reaction.emoji) == "3\N{combining enclosing keycap}":
                    for x in range(4):
                        if x == 4:
                            await ctx.send("You Are Struggling With This Too Much, DM <@475304536920031232> For Help")
                            return
                        await ctx.send("Please Pick A Color By copying the hex and paste it here, eg `#74ff00` \nhttps://htmlcolorcodes.com/color-picker/")
                        colorcode = await self.bot.wait_for("message", check=check)
                        try:
                            fincolor = await commands.ColourConverter().convert(ctx, colorcode.content)
                        except Exception as e:
                            await ctx.send("This Is Not A Color")
                            continue
                        else:
                            break
                    with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json", "r+") as dat:
                        data = json.load(dat)
                        data["color"] = f"{fincolor}"
                        dat.seek(0)  
                        json.dump(data, dat)
                        dat.truncate()
                    await ctx.send("Data Sucessfully Saved!")
                if str(reaction.emoji) == "4\N{combining enclosing keycap}":
                    
                    for x in range(4):
                        if x == 4:
                            await ctx.channel.send("It is clear this is not working. Try again later.")
                            return
                        await ctx.channel.send("OK, please send a link to the image. Image uploading is not supported")
                        try:
                            url = await self.bot.wait_for('message', timeout=120,check=check)
                        except asyncio.TimeoutError:
                            await ctx.channel.send("You took too long! Please try again later.")
                            return
                        link = url.content
                        url = urlparse(url.content)
                        if url.scheme == "":
                            link = f"https://{link}"
                        if url.scheme == "" and url.netloc == "":
                            await ctx.send("That Isnt A Link!, try again")
                            continue  # Checks headers to see if it is an image.
                        print("cleared!")
                        
                        break

                    with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json", "r+") as dat:
                        data = json.load(dat)
                        data["url"] = f"{link}"
                        dat.seek(0)  
                        json.dump(data, dat)
                        dat.truncate()
                    await ctx.send("Data Sucessfully Saved!")   



    @commands.command()
    @commands.has_any_role(548846050056863756,586494766359904257) 
    async def lock(self, ctx, command = None):
        if command is None: #Checks to make sure they used a command name and not just .lock
            await ctx.send("Syntax = `.lock <command_name> where <command_name> is the command name you wish to lock, retry the command")
            return
        if not os.path.exists(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json"): # checks to see if they own the command or if the command exists
            await ctx.send("Not A Command!, Retry Again")
            return
        if os.path.exists(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json"):
            with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json", "r+") as f:
                comm_data = json.load(f) # loads the command data
            if "unlocked" not in comm_data.keys():
                comm_data["unlocked"] = True
                with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json","r+") as f:
                    f.seek(0)
                    json.dump(comm_data, f)
                    f.truncate()

            if not comm_data["unlocked"]:
                await ctx.send("This Command Is Already Locked")
                return
            if comm_data["unlocked"]:
                comm_data["unlocked"] = False
                with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json","r+") as f:
                    f.seek(0)
                    json.dump(comm_data, f)
                    f.truncate()
                await ctx.send("Command Has Been Locked!(This Means Only You Can Use It)")


    @commands.command()
    @commands.has_any_role(548846050056863756,586494766359904257) 
    async def unlock(self, ctx, command = None):
        if command is None: #Checks to make sure they used a command name and not just .lock
            await ctx.send("Syntax = `.unlock <command_name> where <command_name> is the command name you wish to unlock, retry the command")
            return
        if not os.path.exists(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json"): # checks to see if they own the command or if the command exists
            await ctx.send("Not A Command!, Retry Again")
            return
        if os.path.exists(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json"):
            with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json") as f:
                comm_data = json.load(f) # loads the command data
            if "unlocked" not in comm_data.keys():
                comm_data["unlocked"] = False
                with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json","r+") as f:
                    f.seek(0)
                    json.dump(comm_data, f)
                    f.truncate()
            if comm_data["unlocked"]:
                await ctx.send("This Command Is Already Unlocked!")
                return
            if not comm_data["unlocked"]:
                comm_data["unlocked"] = True
            with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json","r+") as f:
                f.seek(0)
                json.dump(comm_data, f)
                f.truncate()
            await ctx.send("Command Has Been Unlocked!(This Means Anyone With Finesse Perks Can Use It Can Use It)")

            
    @commands.command()
    @commands.is_owner()
    async def fix_all(self, ctx):
        start = time.time()
        filelist = []
        for subdir, dirnames, files in os.walk("/home/shadbot/command_data/"):
            for file in files:
                f = os.path.join(subdir, file)#gets all the files and makes a absolute path to them
                filelist.append(f)
        print("everything is appended to filelist")
        datalist = []
        accepted = False
        for x in filelist:
            
            try:
                with open(x,"r+") as f: # opens files and loads the json data
                    data = json.load(f)
            except Exception as e:
                print(e)
                print(f"The Following Data Was Corrupted For {x[:-5]}")
                continue
            if "unlocked" not in data.keys():
                data["unlocked"] = False
                with open(x,"r+") as e:
                    e.seek(0)
                    json.dump(data,e)
                    e.truncate()

        end = time.time()
        fin = end - start
        await ctx.send(f"commands have been fixed, time took was {fin}")



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)
        path = None
        if not isinstance(error, commands.errors.CommandNotFound): return # Test for CommandNotFound and not another error              
        elif not ctx.guild: return    
        rolelist = ctx.author.roles
        finrole = ctx.guild.get_role(586494766359904257)
        finrole2 = ctx.guild.get_role(548846050056863756)
        print(finrole.name)
        print(finrole2.name)
        print("roles have been gotten bois")
        if finrole not in rolelist and finrole2 not in rolelist: return
        elif not os.path.isfile(f"/home/shadbot/command_data/{ctx.author.id}/{ctx.invoked_with}.json"):
            
            filelist = []
            for subdir, dirnames, files in os.walk("/home/shadbot/command_data/"):
                for file in files:
                    f = os.path.join(subdir, file)#gets all the files and makes a absolute path to them
                    filelist.append(f)
            print("everything is appended to filelist")
            datalist = []
            accepted = False
            for x in filelist:
                
                
                try:
                    with open(x,"r+") as f: # opens files and loads the json data
                        data = json.load(f)
                except Exception as e:
                    print(e)
                    print(f"The Following Data Was Corrupted For {x[:-5]}")
                    continue
                if data["name"] == ctx.invoked_with and data["unlocked"]:
                    accepted = True
                    path = x
                    break
        elif os.path.isfile(f"/home/shadbot/command_data/{ctx.author.id}/{ctx.invoked_with}.json"): path = f"/home/shadbot/command_data/{ctx.author.id}/{ctx.invoked_with}.json"
        
        text = ctx.message.content.split(' ')
        text = text[len(text)-1]
        converter = commands.MemberConverter()
        try:
            target = await converter.convert(ctx, text)
            print(f"convert failed FOR {ctx.author.name}")
        except commands.errors.BadArgument:
            target = None
        cmdname = ""
        with open(f"{path}", "r+") as datafile:
            data = json.load(datafile)
            cmdname = data["name"]
            if ctx.author.id != data["creator"]:
                if not data["unlocked"]:
                    await ctx.author.send("You Are Not The Author Of This Command")
                    return
            if '%target' in data['title'] or '%target' in data['body']:
                if not target:
                    await ctx.channel.send("A valid target is required for this command.")
                    return
        title = data['title']
        body = data["body"]
        if target:  # Swapping out the variables with the real values.
            title = title.replace("%target", target.name)
            body = body.replace("%target", target.name)
        title = title.replace("%sender", ctx.author.name)
        body = body.replace("%sender", ctx.author.name)

        def checkKey(dict_obj, key): 
            if not isinstance(dict_obj, dict):
                raise SyntaxError
                return
            if key in dict_obj.keys(): 
                return True
            else: 
                return False
        if checkKey(data, "color"):
            converter = commands.ColourConverter()
            try:
                color2 = await converter.convert(ctx, data["color"])
            except Exception as e:
                await ctx.send("Error Happened, Send The Following To <@475304536920031232>, " + e)
                return
            embed = discord.Embed(title=title, description=body,
                            colour=color2)
        elif not checkKey(data, "color"):
            
            embed = discord.Embed(title=title, description=body,
                                colour=discord.Colour.red())
        if data['image']:  # Sets the image if one is specified.
        
            embed.set_image(url=data['url'])

        await ctx.channel.send(embed=embed)  # Sends it. 
    
    @commands.command()
    async def rem(self, ctx, command=None):
        # Checks to see if youre in the guild and the command exists.
        if not os.path.exists(f"/home/shadbot/command_data/{ctx.author.id}"):
            await ctx.author.send("You Havent Created A Command Before, Please Run The Create Command")
            return
        if not ctx.guild:
            return
        elif not command:
            await ctx.channel.send("Please specify a command")
            return
        
        if not os.path.isfile(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json"):
            await ctx.send("This Isnt A Command")
            return
        with open(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json","r+") as data:
            stuff = json.load(data)
            if stuff["creator"] != ctx.author.id:
                await ctx.send("This command isn't yours")
                return
        os.remove(f"/home/shadbot/command_data/{ctx.author.id}/{command}.json")
        await ctx.send("Command Removed")
    
    @commands.has_any_role(547784731157200927,547780757251424258,547784768981434395)
    @commands.command()
    async def staff_rem(self, ctx,member: discord.Member,command=None):
        # Checks to see if youre in the guild and the command exists.
        if not os.path.exists(f"/home/shadbot/command_data/{member.id}"):
            await ctx.author.send("You Havent Created A Command Before, Please Run The Create Command")
            return
        if not ctx.guild:
            return
        elif not command:
            await ctx.channel.send("Please specify a command")
            return
        
        if not os.path.isfile(f"/home/shadbot/command_data/{member.id}/{command}.json"):
            await ctx.send("This Isnt A Command")
            return
        os.remove(f"/home/shadbot/command_data/{member.id}/{command}.json")
        await ctx.send("Command Removed")
        logchan = self.bot.get_channel(649366716836610059)

        embed = discord.Embed(title="Command Deleted",description=F"<@{ctx.author.id}> Has Deleted {command}",colour=discord.Colour.red())
        await logchan.send(embed=embed)
    
        

    @create.error
    async def start_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send("You Are On Cooldown,(The Cooldown Is 60 Seconds)")
    
def setup(bot):
    print("Loading custom command System!")
    bot.add_cog(custom(bot))
    print("custom command sys loaded")