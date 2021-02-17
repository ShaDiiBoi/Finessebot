import logging
import datetime

import mysql.connector
import random
import os
import json
import typing
import discord
from pathlib import Path
from discord.ext import commands
import time
import random
from translate import Translator


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

def push(*args):
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="shad",
                    passwd="shadii",
                    database="finesse")
    dbcursor = mydb.cursor(buffered=True)
    dbcursor.execute(*args)
    mydb.commit()
    mydb.close()
    return None

def pull_one(*args):
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="shad",
                    passwd="shadii",
                    database="finesse",
                    )
    dbcursor = mydb.cursor(buffered=False)
    dbcursor.execute(*args)
    
    results = dbcursor.fetchone()
    mydb.commit()
    dbcursor.close()
    mydb.close()
    return results



class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timeformat = "%Y-%m-%d %H:%M:%S"
        self.staff_ids = [547784768981434395,547780757251424258,534098929617207326,547792652029001737,534583040454688781,547784731157200927]
        self.staff_path = "/home/shadbot/punish_data/staff"
        self.logchan = self.bot.get_channel(668163108090413088)

    @classmethod
    def id_gen(cls):
        
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
    @classmethod
    def check_hierarchy(cls, punisher,punishee):
        if punishee.top_role >= punisher.top_role:return True 
        else: return False

    @commands.has_any_role(586494766359904257, 548846050056863756)
    @commands.command()
    async def translate(self, ctx, fromlang, tolang, *, sentence):
        translator = Translator(to_lang=f"{tolang}",from_lang=f"{fromlang}")
        process = translator.translate(f"{sentence}")
        embed = discord.Embed(title="Finesse",description=f"{process}",color=discord.Color.teal())
        await ctx.send(embed=embed)




        

    @commands.command()
    @commands.is_owner()
    async def listening(self, ctx, *, song):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{song}"))

    @commands.command()
    @commands.cooldown(3,10)
    async def lat(self, ctx):
        await ctx.send(self.bot.latency)


    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395,534098929617207326)
    async def unmute(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("Please specify a member")
            return
            print()
        x = pull("SELECT * FROM mutes WHERE uid = %s", (str(member.id),))
        if len(x) == 0: 
            await ctx.send("This User Is Not Muted")
            return

        rolelist = x[0][1].split(",")
     
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        print(role.name)
        await member.remove_roles(role)
        finesse = self.bot.get_guild(534050853477285888)
        for role in rolelist:
            role = finesse.get_role(int(role))
            await member.add_roles(role)
        embed = discord.Embed(title="Finesse Moderation System!",timestamp=ctx.message.created_at, description=f"{member.mention} Has Been Unmuted!",color=discord.Color.teal())
        embed.set_author(name="Finesse")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Finesse Moderation System!", description=f"{member.mention} Has Been Unmuted By {ctx.author.mention}",color=discord.Color.teal())
        await self.logchan.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title="Finesse Moderation System!",timestamp=ctx.message.created_at, description="You Do Not Have Permissions To Do That",color=discord.Color.teal())
                    
            embed.set_author(name="Finesse")
            embed.set_footer(text="Made By ShaD")
            await ctx.send(embed=embed)
        else:
            print(error)

    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395,534098929617207326,547792652029001737)
    async def purge(self,ctx,user: discord.Member,amount: int):
        def check2(m):
            return m.author.id == user.id
        await ctx.channel.purge(limit=amount,check=check2)
        embed = discord.Embed(title="Finesse Moderation System!",timestamp=ctx.message.created_at, description=f"{amount} messages have been Purged By {ctx.author}!",color=discord.Color.teal())
        await ctx.send(embed=embed)
        await self.logchan.send(embed=embed)

    @commands.command()
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395,534098929617207326)
    async def mute(self, ctx,member: discord.Member, reason: str=f"No Reason"):
        
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        
        embed = discord.Embed(title="Finesse Moderation System!",timestamp=ctx.message.created_at, description=f"{member.mention} Has Been Muted By {ctx.author.mention}!",color=discord.Color.teal())
        embed.set_author(name="Finesse")
        embed.set_footer(text="Made By ShaD")
        role_list = []
        if mod.check_hierarchy(ctx.author,member):
            ret_embed = discord.Embed(timestamp=ctx.message.created_at,title="Finesse",description="You can not mute this member as they  are higher than you in hierarchy",color=discord.Color.teal())
            await ctx.send(embed=ret_embed)
            return
        for role in member.roles:
            try:
                await member.remove_roles(role)

            except: continue
            role_list.append(role.id)
        

        listrole = ",".join(map(str, role_list)) 
        await member.add_roles(mute_role)
        push("insert into mutes VALUES (%s, %s,%s)",(member.id,listrole,reason))
        await ctx.send(embed=embed)
        embed2 = discord.Embed(title="Finesse", description=f"{member.mention} Has Been Muted By {ctx.author.mention} For {reason}",color=discord.Color.teal())
        embed.set_author(name="Finesse")
        embed.set_footer(text="Made By ShaD")
        await self.logchan.send(embed=embed2)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title="Finesse", description="You do not have permissions to do this.",color=discord.Color.teal())
            embed.set_author(name="Finesse")
            embed.set_footer(text="Made By ShaDii")
            await ctx.send(embed=embed)
        elif isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(title="Finesse", description="Syntax Is `.mute <member_mention_or_id> <reason>`",color=discord.Color.teal())
            embed.set_author(name="Finesse")
            embed.set_footer(text="Made By ShaDii")
            await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, reason: str = None):
        if reason is None: reason = f'Action done by {ctx.author.mention} (ID: {ctx.author.id})'
        if reason is not None: reason = f"Action Done By {ctx.author.mention}(Reason: {reason})"
        await member.kick(reason=reason)
        logchan = self.bot.get_channel(668163108090413088)
        kicked = discord.Embed(title="Finesse Moderation System!",timestamp=ctx.message.created_at,description=f"<@{member.id}> Has Been Kicked From {ctx.guild.name} by <@{ctx.author.id}>",color=discord.Color.teal())
        embed = discord.Embed(title="Finesse", description=(f"{member.mention} Has Been Kicked By {ctx.author}!"))
        embed.set_author(name="Finesse")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)
        await logchan.send(embed=kicked)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title="Finesse", description="You Are Not Allowed To Do This....")
            embed.set_author(name="Finesse")
            embed.set_footer(text="Made By ShaD")
            await ctx.send(embed=embed)


    @commands.has_any_role(547784768981434395,547780757251424258,534098929617207326,547792652029001737,534583040454688781,547784731157200927)
    @commands.command()
    async def ban(self, ctx, user_id: typing.Union[int, discord.Member], ban_reason="No Reason Given"):
        
        banr = f"{ban_reason} (Requested By {ctx.author.mention})"
        ban_victim = None
        if isinstance(user_id, int):
            print("its a int")
            user = False
            try:
                ban_victim = ctx.guild.get_member(user_id)#trys to get user through server method
                in_guild = True
            except Exception as e:
                print("NOT A MEMBER")   
                in_guild = False
            if in_guild:
                if mod.check_hierarchy(ctx.author,ban_victim):
                    ret_embed = discord.Embed(timestamp=ctx.message.created_at,title="Finesse",description="You can not ban this member as they are higher than you in hierarchy",color=discord.Color.teal())
                    await ctx.send(embed=ret_embed)
                    return
                else: pass
            if not in_guild:
                ban_victim = discord.Object(id=int(user_id))
                ban_victim.server = discord.Object(id=ctx.guild.id)
            punish_id,punished,punisher,timestamp = self.id_gen(),ban_victim.id,ctx.author.id,ctx.message.created_at
            try: 
                await ban_victim.send(content="https://discord.gg/yR7QXCt",embed=discord.Embed(title="Finesse Moderation System",description="You have been banned from finesse, to appeal your ban , join the server link below"))
            except Exception as e:
                print(e)

            await ctx.guild.ban(user=ban_victim, reason=ban_reason) 
            ban_push = pull("INSERT INTO bans VALUES (%s,%s,%s,%s)",(punished,timestamp,ban_reason,punisher))
            
        
            logchan = self.bot.get_channel(668163108090413088)
            banned = discord.Embed(title="Finesse Moderation System!",timestamp=ctx.message.created_at,description=f"{ban_victim.mention} Has Been Banned From {ctx.guild.name} by {ctx.author.mention}") # embed for ban
            await logchan.send(embed=banned)
            await ctx.send(embed=banned)
            return
            
        if isinstance(user_id, discord.Member):
            print("its a member")
            if mod.check_hierarchy(ctx.author,user_id):
                ret_embed = discord.Embed(timestamp=ctx.message.created_at,title="Finesse",description="You can not ban this member as they are higher than you in hierarchy",color=discord.Color.teal())
                await ctx.send(embed=ret_embed)
                return
            else: pass
            logchan = self.bot.get_channel(668163108090413088)
            banned = discord.Embed(title="Finesse Moderation System!",timestamp=ctx.message.created_at,description=f"<@{user_id.id}> Has Been Banned From {ctx.guild.name} by <@{ctx.author.id}>",color=discord.Color.teal()) # embed for ban
            await logchan.send(embed=banned)
            ban_victim = user_id
            punish_id,punished,punisher,timestamp = self.id_gen(),ban_victim.id,ctx.author.id,ctx.message.created_at        
            ban_push = pull("INSERT INTO bans VALUES (%s,%s,%s,%s)",(punished,timestamp,ban_reason,punisher))
            await user_id.ban(reason=ban_reason)
            await ctx.send(embed=banned)
            return
            
            
    @commands.has_any_role(547784768981434395,547780757251424258,534098929617207326,547792652029001737,534583040454688781,547784731157200927)
    @commands.command(description="Unbans A User From The Server Through Their ID")
    async def unban(self, ctx, user_id: typing.Union[int, discord.User]):
        if isinstance(user_id,int):
            try:
                await ctx.guild.unban(user=discord.Object(id=int(user_id)),reason=f"Unbanned By {ctx.author.mention}")
            except Exception as e:
                embed = discord.Embed(title="Finesse Moderation System!",timestamp=ctx.message.created_at,description=F"Error Occured, Send This To Shad:{e}",color=discord.Color.teal())
                await ctx.send(embed=embed)
                return
            uid = user_id
        if isinstance(user_id,discord.User):
            try:
                await ctx.guild.unban(user=discord.Object(id=int(user_id.id)),reason=f"Unbanned By {ctx.author.mention}")
            except Exception as e:
                embed = discord.Embed(title="Finesse Moderation System!",timestamp=ctx.message.created_at,description=F"Error Occured, Send This To Shad:{e}",color=discord.Color.teal())
                await ctx.send(embed=embed)
                return
            uid = user_id.id
        finished_embed = discord.Embed(title="Finesse Moderation System!",description=f"<@{uid}> Was Unbanned By <@{ctx.author.id}>",timestamp=ctx.message.created_at,color=discord.Color.teal())

        await self.logchan.send(embed=finished_embed)
        await ctx.send(embed=finished_embed)


    
    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.has_any_role(547792652029001737,547780757251424258,547784731157200927,547784768981434395,534098929617207326,547780757251424258,547784731157200927,378667625036644353)
    async def warn(self, ctx, member: discord.Member,reason):
        now = datetime.datetime.utcnow()
        strtime = now.strftime(self.timeformat)
        pull_one("INSERT INTO warns (uid,reason,author,date) VALUES (%s,%s,%s,%s)",(member.id,reason,ctx.author.id,strtime,))

        embed = discord.Embed(title="Finesse Warn System!",timestamp=ctx.message.created_at, description=f"{member.mention} Has Been Warned!",color=discord.Color.teal())
        embed.set_author(name="Finesse")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Finesse Warn System!",timestamp=ctx.message.created_at, description=f"{member.mention} Has Been Warned By {ctx.author.mention} for {reason}",color=discord.Color.teal())
        await self.bot.get_channel(668163108090413088).send(embed=embed)
        embed = discord.Embed(title="Finesse Warn System!",timestamp=ctx.message.created_at, description=f"You were warned in Finesse by a staff member for {reason}.If you have a problem with this punishment, DM Manager/HR+",color=discord.Color.teal())
        await member.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.has_any_role(547792652029001737,547780757251424258,547784731157200927,547784768981434395,534098929617207326,547780757251424258,547784731157200927)
    async def wc(self, ctx, member: discord.Member):
        
        insert_query = pull("SELECT * FROM warns WHERE uid = '%s' LIMIT 20",(member.id,)) # Grabs Warns
        if insert_query is None or len(insert_query) == 0:
            no_warns = discord.Embed(title="Finesse Warn System!",timestamp=ctx.message.created_at, description=f"{member.mention} Has Not Been Warned Before",color=discord.Color.teal())
            await ctx.send(embed=no_warns)
            return
        author_list = [f"<@{x[3]}>" for x in insert_query]
        author_string = f"<@{author_list[0]}> ,".join(author_list[1:])
        embed = discord.Embed(title="Finesse Warn System!",timestamp=ctx.message.created_at, description=f"{member.mention} Has Been Warned By {author_string},Check Your Dms For More Information",color=discord.Color.teal())
        embed.set_author(name="Finesse")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Finesse Warn System!",timestamp=ctx.message.created_at, description=f"Warn List",color=discord.Color.teal())
        for data in insert_query:
            embed.add_field(name=f"{data[0]}",value=f"**Reason:** {data[2]}. **Author:** <@{data[3]}>. **Date:** {data[4]}")
        await ctx.author.send(embed=embed)
    
    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.has_any_role(547792652029001737,547780757251424258,547784731157200927,547784768981434395,534098929617207326,547780757251424258,547784731157200927)
    async def delwarn(self, ctx, member: discord.Member,reason):

        insert_query = pull_one("SELECT * FROM warns WHERE num = %s LIMIT 1",(wid,)) # Grabs Warns
        if insert_query is None or len(insert_query) == 0:# Checks if there are any rows with the conditions asked
            no_warns = discord.Embed(title="Finesse Warn System!",timestamp=ctx.message.created_at, description=f"This Warn ID Is Invalid",color=discord.Color.teal())
            await ctx.send(embed=no_warns)
            return
        pull_one("DELETE FROM warns WHERE num = %s",(wid))
        embed = discord.Embed(title="Finesse Warn System!",timestamp=ctx.message.created_at, description=f"This Warning Has Been Deleted",color=discord.Color.teal())
        embed.set_author(name="Finesse")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)
     




    @commands.has_any_role(547780757251424258,547784768981434395)
    @commands.command()
    async def shads_cleanse(self, ctx):
        users = [238663674309378048,238663674309378048,243214515460767744,550398711042277386,579675594628005901,238663674309378048,203697474903212032,427292582939197441,342497540261806082]
        members = []
        finesse = self.bot.get_guild(534050853477285888)
        def traitors(m):
            return m.author.id in users
        for uid in users:
            try:
                user = finesse.get_member(int(uid))
            except discord.NotFound as e:
                print("could not find user")
                continue
            members.append(user)
        for x in members:
            try:
                await x.send("you have been banned by shad for `4.3//Plotting Against Finesse//acting against the servers best interests//Possible Attempt To Expose Staff/Members`")
                await x.ban(reason="4.3//Betrayal//Plotting Against Finesse//Possible Attempt To Expose Staff/Members//Possible DM Advertising")
            except Exception as e:
                print(f"could not ban {x.name}")
        await ctx.send("The traitors have been removed")
            
        
        


    
def setup(bot):
    print("Loading Mod Commands!")
    bot.add_cog(mod(bot))
    print("Mod Commands Have Been Loaded")
