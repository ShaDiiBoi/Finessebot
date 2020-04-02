import logging
import datetime
import random
import os
import json
import discord
from pathlib import Path
from discord.ext import commands
import sys
import asyncio
import time
import mysql.connector
from discord.ext import tasks
import praw
import re



class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.error_channel = bot.get_channel(596509055376162831)
        self.used = []
        self.discord_me_bump.start()

        
    

    
    # @tasks.loop(minutes=30)
    # async def memes(self):
    #     print("Meme Task Is Starting")
    #     reddit = praw.Reddit(client_id = "-oHDjYLqcFytSw",
    #                         client_secret ="vDmPPfQSIfgrRd4Z3F1cqd4ikxE",
    #                         password = "GDRG6SQtNQsc",
    #                         user_agent = "Discord Script By /u/ShaDiiBoi",
    #                         username = "ShaDiiBoi")
        
    #     print(reddit.user.me())
    #     randompicked = []

    #     subreddit = reddit.subreddit('memes')
         
    #     for x in subreddit.hot(limit=300):
    #         if x.url.startswith("https://www.reddit.com/"):
    #             pass
    #         elif x.url.startswith("https://i.redd.it"):
    #             embed = discord.Embed(title=f"r/meme Title: {x.title}",description=f"**Description**: {x.description}")
    #             randompicked.append(x.url)
    #     for x in range(len(randompicked)):
    #         meme = random.choice(randompicked)
    #         if meme in self.used:
    #             continue
    #         elif meme not in self.used:
               
    #             embed.set_image(url=meme)
    #             await self.bot.get_channel(566475605743501334).send(embed=embed)
    #             self.used.append(meme)
    #             break
            


  

    @tasks.loop(seconds=20)
    async def mem_check(self):
        print("Task Works")
        fn = self.bot.get_guild(534050853477285888)
        length = fn.member_count
        memchan = fn.get_channel(566715186812289025)
        leng = str(length)
        print(f"Member Checked {leng[0:2]} {leng[2:]}, {length}")
        await memchan.edit(name=f"Users  》 {leng[0:2]},{leng[2:]}")



    @commands.command(hidden=True)
    @commands.is_owner()
    async def loops(self, ctx, loop_name,loop_condition):
        if loop_name == "memes" and loop_condition == "start":
            self.memes.start()
            await ctx.send(f"`{loop_name} has changed its condition to {loop_condition}`")
        elif loop_name == "memes" and loop_condition == "stop":
            self.memes.stop()
            await ctx.send(f"`{loop_name} has changed its condition to {loop_condition}`")
        if loop_name == "membercount" and loop_condition == "start":
            self.mem_check.start()
            await ctx.send(f"`{loop_name} has changed its condition to {loop_condition}`")
        elif loop_name == "membercount" and loop_condition == "stop":
            self.mem_check.stop()
            await ctx.send(f"`{loop_name} has changed its condition to {loop_condition}`")
        


    @commands.Cog.listener()
    async def on_member_update(self,before,after):
        finesse = self.bot.get_guild(534050853477285888)
        fin_boost = finesse.get_role(586494766359904257)
        fin_elite = finesse.get_role(548846050056863756)
        if fin_boost not in before.roles and fin_boost in after.roles:
            embed = discord.Embed(title="Thanks For Boosting!",Description="Thanks For Boosting Finesse!, Check Out Your New Perks Below! ")
            embed.add_field(name="Color Menu!",value="You Have Access To The Color Menu We Made, Check <#594104577574567946> To Pick A Color!",inline=False)
            embed.add_field(name="Custom Command System!",value="You Can Create Custom Commands In <#611379940084023296>, The command is .create <command_name>!",inline=False)
            embed.add_field(name="Chat Roulette!",value="You Can Now Join The Queue For Chat Roulette!, Check <#607233448717058075> And React To Join The Queue And Make Some Friends!",inline=False)
            embed.add_field(name="Image Perms!",value="You Can Now Post Images In Lounge!, Make Sure Not To Spam Or You Will Be Muted!",inline=False)
            embed.add_field(name="Profile Perks!",value="You Get Access To More Colors In The Profile Color Menu, Try Bump/Start Your Profile In <#615342434146058252>",inline=False)
            await after.send(embed=embed)
        if fin_elite not in before.roles and fin_elite in after.roles:
            embed = discord.Embed(title="Thanks For Donating!!",Description="Thanks For Donating To Finesse!, Check Out Your New Perks Below! ")
            embed.add_field(name="Color Menu!",value="You Have Access To The Color Menu We Made, Check <#594104577574567946> To Pick A Color!",inline=False)
            embed.add_field(name="Custom Command System!",value="You Can Create Custom Commands In <#611379940084023296>, The command is .create <command_name>!",inline=False)
            embed.add_field(name="Chat Roulette!",value="You Can Now Join The Queue For Chat Roulette!, Check <#607233448717058075> And React To Join The Queue And Make Some Friends!",inline=False)
            embed.add_field(name="Image Perms!",value="You Can Now Post Images In Lounge!, Make Sure Not To Spam Or You Will Be Muted!",inline=False)
            embed.add_field(name="You Can Get A Custom Role!",value="DM <@475304536920031232> For More Information")
            embed.add_field(name="You Can Create Your Own VC!",value="In <#611379940084023296>, Type .vccreate to create your vc!, and .vctitle to name your vc(For Info On The Other Commands, Ask <@475304536920031232>)")
            embed.add_field(name="Profile Perks!",value="You Get Access To More Colors In The Profile Color Menu, Try Bump/Start Your Profile In <#615342434146058252>",inline=False)
            await after.send(embed=embed)


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        #called when a reaction is used
        if reaction.message.guild.id != 534050853477285888: return
        shadrole = reaction.message.guild.get_role(574397747319406592)
        if reaction.emoji.id == 593389757778624523:
            if shadrole in user.roles:


                chan = reaction.message.channel
                guild = reaction.message.guild
                channel = guild.get_channel(574398370693775370)
                if reaction.message.attachments:
                    urlmes = reaction.message.attachments[0]
                    embed = discord.Embed(title=f"{reaction.message.channel}", description=f"{reaction.message.content}", color=0x9dfff3)
                    embed.set_author(name=f"{reaction.message.author.display_name}")
                    embed.set_footer(text="ShadBotto")
                    embed.set_image(url=urlmes.url)
                    await channel.send(embed=embed)
                    await chan.send("Starred!")
                    return
                embed = discord.Embed(title=f"{reaction.message.channel}", description=f"{reaction.message.content}", color=0x9dfff3)
                embed.set_author(name=f"{reaction.message.author.display_name}")
                embed.set_footer(text="Property Of Shad")
                await channel.send(embed=embed)
                await chan.send("Starred!")
#--------------------------------------------------------------------------------------------------==--------------------------------#########################################
            if reaction.count == 3:
                for users in user:
                    if shadrole in user.roles:
                        await reaction.channel.send("Message Already Starred")
                        return
                chan = reaction.message.channel
                guild = reaction.message.guild
                channel = guild.get_channel(574398370693775370)
                if reaction.message.attachments:

                    urlmes = reaction.message.attachments[0]
                    embed = discord.Embed(title=f"{reaction.message.channel}", description=f"{reaction.message.content}", color=0x9dfff3)
                    embed.set_author(name=f"{reaction.message.author.display_name}")
                    embed.set_footer(text="ShadBotto")
                    embed.set_image(url=urlmes.url)
                    await channel.send(embed=embed)
                    await chan.send("Starred!")
                    return

                embed = discord.Embed(title=f"{reaction.message.channel}", description=f"{reaction.message.content}", color=0x9dfff3)
                embed.set_author(name=f"{reaction.message.author.display_name}")
                embed.set_footer(text="Property Of Shad")
                await channel.send(embed=embed)
                await chan.send("Starred!")
            if reaction.count > 3:
                print("no")
                return
                


        
    
        









    @commands.Cog.listener()
    async def on_message(self, message):
        blacklist = [181470050039889920, 277233016974213120, 403549673857744898]  # list of people the bot wont take messages from
        lovelist = [550398711042277386,203931003453046784, 276011140734255104]
        stafflist = [547784731157200927,547784768981434395,615624883405324289,534098929617207326,534583040454688781,547792652029001737,547780757251424258]
        banned_words = ["dating","d@ting","dayting","d8ing","d8ting"]
        channel = message.channel
        
        mystr = message.content.lower()
        wordList = re.sub("[^\w]", " ",  mystr).split()
        for word in wordList:
            if word in banned_words:
                rolelist = [x.id for x in message.author.roles if x.id in stafflist]
                if len(rolelist) == 0:
                    await message.delete()
                    embed = discord.Embed(title="Finesse Automod",description=f"You Cant Say `{word}` in finesse, sorry for the inconvenience and if you have a issue with this, DM the owner.",color=discord.Color.teal())
                    await message.author.send(embed=embed)
                else: pass
                    
        if channel.id == 566473203921321984:
            mystr = message.content.lower()
       
            word_list = re.sub("[^\w]", " ",  mystr).split()
            if "how" in word_list and "verify" in word_list:
                    embed = discord.Embed(
                                        title="Verification Info",
                                        description="If you want to verify, check out the <#566523946934075393> For More Information"
                                        )
                    embed.set_footer(text="Finesse")
                    await message.channel.send(embed=embed)
            else: pass

                
            
            
        
        msg = message.content
        if channel.id == 609427615450791937:
            embed = discord.Embed(title="How to stop these pings!",description="**To stop getting these pings, grab the no event role from the** <#566514394612105216> **channel!**")
            await message.channel.send(embed=embed)
        if channel.id == 566523629886504972:
            if message.author.id == 599536624870752282:
                embed = discord.Embed(title="How to stop these pings!",description="**To stop getting these pings, grab the no partner role from the** <#566514394612105216> **channel!**")
                await message.channel.send(embed=embed)
        if channel.id == 566481803204886549:
            if "discord.gg/" in msg:
                
                mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="shad",
                                    passwd="shadii",
                                    database="finesse")
                dbcursor = mydb.cursor()

                new_partner = False
                check = "SELECT * FROM partner WHERE uid = %s" 
                x = (str(message.author.id),)
                dbcursor.execute(check,x)
                returned = dbcursor.fetchall()
                if len(returned) == 0: new_partner = True
                if new_partner:
                    seq = "INSERT INTO partner (uid, amount) VALUES (%s,%s)"
                    val = (str(message.author.id), "1")
                    dbcursor.execute(seq,val)
                if not new_partner:
                    seq = "SELECT amount FROM partner WHERE uid = %s" 
                    val = (str(message.author.id),)
                    dbcursor.execute(seq,val) 
                    amount = int(dbcursor.fetchone()[0]) + 1
                    update = "UPDATE partner SET amount = %s WHERE uid = %s"
                    values = (str(amount),str(message.author.id))
                    dbcursor.execute(update,values)
                seq = "SELECT amount FROM partner WHERE uid = %s" 
                val = (str(message.author.id),)
                dbcursor.execute(seq,val) 
                amount = dbcursor.fetchone()
                mydb.commit()
                embed = discord.Embed(title="Partner Log",description=f"{dbcursor.rowcount} rows have been updated")
                embed.add_field(name=f"Partner Counter",value=f"<@{message.author.id}> Has Partnered,They Now Have {amount[0]} Partners")
                await self.bot.get_channel(649366716836610059).send(embed=embed)

        if channel.id == 566475605743501334:
            if message.attachments:
                await message.add_reaction(emoji="✅")
        if "shad" in msg.lower():
            if message.author.id == 530945830006292480: # if the message sent is from the bo
                return

            if message.author.id in blacklist:
                return
            if message.author.id in lovelist:
                await channel.send(f"love u {message.author.name} - Shad")
                return
            user = self.bot.get_user(236802606352039938)
            plz = discord.Embed(title="ShaDBoT", description=f"*{message.content}* From ***{message.author}***")
            plz.set_footer(text="Made By ShaD")
            await user.send(embed=plz)
            print("Test Complete")
        # if isinstance(channel, discord.abc.PrivateChannel):
        #     if msg.startswith("!confess"):
                
        #         await channel.send(f"Hello {message.author.mention}!, What Do You Want To Confess Today?")
        #         def check1(m):
        #             return m.channel == channel and m.author.id == message.author.id
        #         confession = await self.bot.wait_for("message", check=check1)

        #         confessChannel = self.bot.get_channel(570045064990949376)
        #         embed = discord.Embed(title=f"Finesse Confessions!", description=(f"**{confession.content}**"))
        #         embed.set_author(name="ShaDBoT")
        #         embed.set_footer(text="Angels")
        #         await confessChannel.send(embed=embed)
        #         await channel.send("Confession Complete!, Have A Good Day")
        #         shad = self.bot.get_user(236802606352039938)
        #         await shad.send(f"```{confession.content}``` \n BY `{message.author.mention}")
        #     if msg.startswith("!report"):
        #         log = discord.utils.get(self.bot.get_all_channels(), guild__name='✧ Finesse ✧', name='shad-logs')
        #         auth = message.author
        #         if message.author == self.bot.user:
        #             return
        #         plz = discord.Embed(title="ShaDBoT", description=f"{message.content} From ***{message.author.mention}***")
        #         plz.set_footer(text="Made By ShaD")
        #         await log.send(embed=plz)
    


    @tasks.loop(hours=5,minutes=25)
    async def discord_me_bump(self):
        shad = self.bot.get_user(475304536920031232)
        await shad.send("Go Bump Finesse On Discord.me! \n https://discord.me/dashboard")


    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name="DM Me Your Verification Photo!", type=1))
        print("ShaDBoT Has Been Activated")










def setup(bot):
    print("Loading Events!")
    bot.add_cog(events(bot))
    print("Events  Have Loaded!")
