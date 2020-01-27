import logging
import datetime
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
from database import insert, xcute, get_blacklist
class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.staff_ids = [547784768981434395,547780757251424258,534098929617207326,547792652029001737,534583040454688781,547784731157200927]
        self.staff_path = "/home/shadbot/punish_data/staff"
        self.logchan = self.bot.get_channel(647215305885483019)

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


    @commands.has_any_role(586494766359904257, 548846050056863756)
    @commands.command()
    async def translate(self, ctx, fromlang, tolang, *, sentence):
        translator = Translator(to_lang=f"{tolang}",from_lang=f"{fromlang}")
        process = translator.translate(f"{sentence}")
        embed = discord.Embed(title="Angelica",description=f"{process}")
        await ctx.send(embed=embed)


    @commands.has_permissions(administrator=True)
    @commands.command()
    async def trainee(self, ctx, member: discord.Member):
        guild = self.bot.get_guild(523042374209765377)
        trainee = ctx.guild.get_role(547792652029001737)
        await member.add_roles(trainee)
        invite = await guild.invites()
        inv = invite[0]
        print(inv.url)
        welcome_embed = discord.Embed(title="Finesse Promoter",description=f"Welcome To The Finesse Staff Team, Join The Server Below.",colour=discord.Colour.teal())
        await member.send(content=inv.url,embed=welcome_embed)
        print("embed sent")
        def if_right_user(m): 
            return m.guild.id == 523042374209765377 and m.id == member.id
        altera_member = await self.bot.wait_for("member_join",check=if_right_user)
        print("user joined")
        fin_role = self.bot.get_guild(523042374209765377).get_role(523043000742313984)
        trainee_altera_role = self.bot.get_guild(523042374209765377).get_role(553271228035497984)
        await altera_member.add_roles(roles=[fin_role,trainee_altera_role])
        print("roles used")
        await self.bot.get_channel(567462624355155988).send(f"{member.mention} Promoted To Trainee,Check out <#663865191766949915>, <#663865191766949915> and <#663865191766949915>")



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
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse", description=(f"{member.mention} Has Been Unmuted!"))
        embed.set_author(name="Finesse")
        embed.set_footer(text="Made By ShaD")
        await ctx.send(embed=embed)
        await self.logchan.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title="Finesse", description="You Are Not Allowed To Do This....")
                    discord.Embed(title="Finesse", description="You Are Not Allowed To Do This....")
            embed.set_author(name="Finesse")
            embed.set_footer(text="Made By ShaD")
            await ctx.send(embed=embed)
        else:
            print(error)

    @commands.command()
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395,534098929617207326,547792652029001737)
    async def purge(self, ctx,user: discord.Member, amount: int):
        def check(m):
            return m.author.id == user.id
        await ctx.channel.purge(limit=amount,check=check)
        embed = discord.Embed(title='ShaDBot', description=(f"{amount} messages have been Purged By {ctx.author}!"))
        await ctx.send(embed=embed)
        await self.logchan.send(embed=embed)

    @commands.command()
    @commands.has_any_role(547780757251424258,547784731157200927,547784768981434395,534098929617207326)
    async def mute(self, ctx,member: discord.Member=None, reason: str):
        
        if not member:
            plz = discord.Embed(title="Finesse", description="Please Specify A Member...")
            plz.set_author(name="Finesse")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        
        embed = discord.Embed(title="Finesse", description=(f"{member.mention} Has Been Muted By {ctx.author}!"))
        embed.set_author(name="Finesse")
        embed.set_footer(text="Made By ShaD")
        role_list = []
        for role in member.roles:
            try:
                await member.remove_roles(role)

            except: continue
            role_list.append(role)
        

        listrole = ",".join(map(str, role_list)) 
        await member.add_roles(mute_role)
        insert("mutes",(ctx.author.id,listrole,))
        await ctx.send(embed=embed)
        await self.logchan.send(embed=embed)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title="Finesse", description="You Are Not Allowed To Do This....")
            embed.set_author(name="Finesse")
            embed.set_footer(text="Made By ShaD")
            await ctx.send(embed=embed)
        else:
            print(error)
    # @commands.command()
    # @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    # @commands.guild_only()
    # @commands.has_permissions(administrator=True)
    # async def kick(self, ctx, member: discord.Member, reason: str = None):
    #     if reason is None:
    #         reason = f'Action done by {ctx.author} (ID: {ctx.author.id}'
    #         await member.kick(reason=reason)
    #         embed = discord.Embed(title="Finesse", description=(f"{member.mention} Has Been Kicked By {ctx.author}!"))
    #         embed.set_author(name="Finesse")
    #         embed.set_footer(text="Made By ShaD")
    #         await ctx.send(embed=embed)

    # @kick.error
    # async def kick_error(self, ctx, error):
    #     if isinstance(error, commands.CheckFailure):
    #         embed = discord.Embed(title="Finesse", description="You Are Not Allowed To Do This....")
    #         embed.set_author(name="Finesse")
    #         embed.set_footer(text="Made By ShaD")
          #  await ctx.send(embed=embed)


    @commands.has_any_role(547784768981434395,547780757251424258,534098929617207326,547792652029001737,534583040454688781,547784731157200927)
    @commands.command()
    async def pban(self, ctx, user_id: typing.Union[int, discord.Member], ban_reason=None):
        banr = f"{ban_reason} (Requested By {ctx.author.mention})"
        if isinstance(user_id, int):
            user = False
            try:
                ban_victim = ctx.guild.get_member(user_id)#trys to get user through id method
            except Exception as e:
                print("NOT A MEMBER")   
                user = True
            try:
                ban_victim = self.bot.get_user(user_id)
            except Exception as e:
                ban_victim = discord.Object(id=user_id)
                ban_victim.server = discord.Object(id=ctx.guild.id)
            punish_id,punished,punisher,timestamp = self.id_gen(),ban_victim.id,ctx.author.id,ctx.message.created_at
            
            await ctx.guild.ban(user=ban_victim, reason=ban_reason) 

            
            # if not os.path.isfile(f"/home/shadbot/punish_data/{ctx.author.id}.json"):
            #     with open(f"/home/shadbot/punish_data/{ctx.author.id}.json","w+") as f:
            #         info = {}
            #         info[f"{punish_id}"]["punish_id"] = str(punish_id)
            #         info[f"{punish_id}"]["punished"] = str(punished)
            #         info[f"{punish_id}"]["punisher"] = str(punisher)
            #         info[f"{punish_id}"]["timestamp"] = str(timestamp)
            #         info[f"{punish_id}"]["ban_reason"] = ban_reason 
            #         json.dump(info, f)
            # if os.path.isfile(f"/home/shadbot/punish_data/{ctx.author.id}.json"):
            #     with open(f"/home/shadbot/punish_data/{ctx.author.id}.json","r+") as f:
            #         info = json.load(f)
            #         info[f"{punish_id}"]["punish_id"] = str(punish_id)
            #         info[f"{punish_id}"]["punished"] = str(punished)
            #         info[f"{punish_id}"]["punisher"] = str(punisher)
            #         info[f"{punish_id}"]["timestamp"] = str(timestamp)
            #         info[f"{punish_id}"]["ban_reason"] = ban_reason 
            #         f.seek(0)
            #         json.dump(info, f)
            #         f.truncate()
            # if os.path.isfile(f"/home/shadbot/punish_data/{ban_victim.id}.json"):
            #     with open(f"/home/shadbot/punish_data/{ban_victim.id}.json","r+") as f:
            #         info = json.load(f)
            #         info[f"{punish_id}"]["punish_id"] = str(punish_id)
            #         info[f"{punish_id}"]["punished"] = str(punished)
            #         info[f"{punish_id}"]["punisher"] = str(punisher)
            #         info[f"{punish_id}"]["timestamp"] = str(timestamp)
            #         info[f"{punish_id}"]["ban_reason"] = ban_reason 
            #         f.seek(0)
            #         json.dump(info, f)
            #         f.truncate()

            # if not os.path.isfile(f"/home/shadbot/punish_data/{ban_victim.id}.json"):
            #     with open(f"/home/shadbot/punish_data/{ban_victim.id}.json","w+") as f:     
            #         info = {}
            #         info[f"{punish_id}"]["punish_id"] = str(punish_id)
            #         info[f"{punish_id}"]["punished"] = str(punished)
            #         info[f"{punish_id}"]["punisher"] = str(punisher)
            #         info[f"{punish_id}"]["timestamp"] = str(timestamp)
            #         info[f"{punish_id}"]["ban_reason"] = ban_reason 
            #         json.dump(info, f)
            logchan = self.bot.get_channel(647215305885483019)
            banned = discord.Embed(timestamp=ctx.message.created_at,description=f"{ban_victim.mention} Has Been Banned From {ctx.guild.name} by {ctx.author.mention}") # embed for ban
            await logchan.send(embed=banned)
            await ctx.send(embed=banned)
            
        if isinstance(user_id, discord.Member):
            
            logchan = self.bot.get_channel(647215305885483019)
            banned = discord.Embed(timestamp=ctx.message.created_at,description=f"{ban_victim.mention} Has Been Banned From {ctx.guild.name} by {ctx.author.mention}") # embed for ban
            await logchan.send(embed=banned)
            await ctx.send(embed=banned)
            ban_victim = user_id
            punish_id,punished,punisher,timestamp = self.id_gen(),ban_victim.id,ctx.author.id,ctx.message.created_at        
            await user_id.ban(reason=ban_reason)
            # if not os.path.isfile(f"/home/shadbot/punish_data/{ctx.author.id}.json"):
            #     with open(f"/home/shadbot/punish_data/{ctx.author.id}.json","w+") as f:
            #         info = {}
            #         info[f"{punish_id}"]["punish_id"] = str(punish_id)
            #         info[f"{punish_id}"]["punished"] = str(punished)
            #         info[f"{punish_id}"]["punisher"] = str(punisher)
            #         info[f"{punish_id}"]["timestamp"] = str(timestamp)
            #         info[f"{punish_id}"]["ban_reason"] = ban_reason 
            #         json.dump(info, f)
            # if os.path.isfile(f"/home/shadbot/punish_data/{ctx.author.id}.json"):
            #     with open(f"/home/shadbot/punish_data/{ctx.author.id}.json","r+") as f:
            #         info = json.load(f)
            #         info[f"{punish_id}"]["punish_id"] = str(punish_id)
            #         info[f"{punish_id}"]["punished"] = str(punished)
            #         info[f"{punish_id}"]["punisher"] = str(punisher)
            #         info[f"{punish_id}"]["timestamp"] = str(timestamp)
            #         info[f"{punish_id}"]["ban_reason"] = ban_reason 
            #         f.seek(0)
            #         json.dump(info, f)
            #         f.truncate()
            # if os.path.isfile(f"/home/shadbot/punish_data/{ban_victim.id}.json"):
            #     with open(f"/home/shadbot/punish_data/{ban_victim.id}.json","r+") as f:
            #         info = json.load(f)
            #         info[f"{punish_id}"]["punish_id"] = str(punish_id)
            #         info[f"{punish_id}"]["punished"] = str(punished)
            #         info[f"{punish_id}"]["punisher"] = str(punisher)
            #         info[f"{punish_id}"]["timestamp"] = str(timestamp)
            #         info[f"{punish_id}"]["ban_reason"] = ban_reason 
            #         f.seek(0)
            #         json.dump(info, f)
            #         f.truncate()

            # if not os.path.isfile(f"/home/shadbot/punish_data/{ban_victim.id}.json"):
            #     with open(f"/home/shadbot/punish_data/{ban_victim.id}.json","w+") as f:     
            #         info = {}
            #         info[f"{punish_id}"]["punish_id"] = str(punish_id)
            #         info[f"{punish_id}"]["punished"] = str(punished)
            #         info[f"{punish_id}"]["punisher"] = str(punisher)
            #         info[f"{punish_id}"]["timestamp"] = str(timestamp)
            #         info[f"{punish_id}"]["ban_reason"] = ban_reason 
            #         json.dump(info, f)
            
            await ctx.send(embed=banned)
            
    @commands.has_any_role(547784768981434395,547780757251424258,534098929617207326,547792652029001737,534583040454688781,547784731157200927)
    @commands.command(description="Unbans A User From The Server Through Their ID")
    async def unban(self, ctx, user_id: typing.Union[int, discord.Member]):
        try:
            bans = await ctx.guild.bans()

            for banEntry in bans:
                user = banEntry.user
                if user.id == user_id:
                   await ctx.guild.unban(user=user,reason=f"Unbanned By {ctx.author.mention}")
        except Exception as e:
            embed = discord.Embed(title="Error!",description=F"Error Occured, Send This To Shad:{e}")
            await ctx.send(embed=embed)
            return





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
