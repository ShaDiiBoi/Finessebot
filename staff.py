#S


import logging
import datetime
import json
import os.path
import discord
from discord.ext import commands
from collections.abc import Sequence
import mysql.connector
import zipfile
import asyncio
import datetime
import pinterest
import re
import mysql.connector



def pull(*args):
    
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="shad",
                    passwd="shadii",
                    database="finesse",)

    dbcursor = mydb.cursor(buffered=True)
    dbcursor.execute(*args)
    
    results = dbcursor.fetchall()
    mydb.commit()
    dbcursor.close()
    mydb.close()
    return results
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


class staffcom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timeformat = "%Y-%m-%d %H:%M:%S"
        self.error_channel = bot.get_channel(596509055376162831)
        self.whitelist = [342497540261806082,475304536920031232]
        self.num = 0
    
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
        await altera_member.add_roles(fin_role,trainee_altera_role)
        print("roles used")
        await self.bot.get_channel(567462624355155988).send(f"{member.mention} Promoted To Trainee,Check out <#567466338617131010>, <#582968437018460165> and <#567466355629096980>")



 # ? S T A F F  W A R N  S Y S T E M 





# ? E N D  O F  S T A F F  W A R N  S Y S T E M 

    @commands.command()
    @commands.has_any_role(547784768981434395,547780757251424258,534098929617207326,534583040454688781)
    async def ban_reason(self,ctx, fullname):

        found = False
        bans = await ctx.guild.bans()
        for ban in bans:
            fullBanName = ban.user.display_name + "#" + ban.user.discriminator
            if fullBanName == fullname:
                found = True
                user_ban = ban
                found_name = ban.user.display_name + "#" + ban.user.discriminator
            else: continue

            
        if found is False:
            embed = discord.Embed(title="Error!",description="Could Not Find This Ban, Retry Again",colour=discord.Colour.teal())
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="Ban Found!",description=f"Ban user is {found_name} ----- Ban Reason Is {ban.reason}")
        await ctx.send(embed=embed)
    @ban_reason.error
    async def banreason_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send("You Are Not Staff So You Can Not Use This Role")
            return
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send("Argument Was Not Parsed, Retry Again!")
            return
        else:
            print(error)
        

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def role_create(self, ctx, rolename, color=None):
        def check(m):
            return m.channel.id == ctx.channel.id and m.author.id == ctx.author.id
        posembed = discord.Embed(title="Choose a position")
        xxx = " "
        
        await ctx.send(f"Choose a position between 0 and {len(ctx.guild.roles)} \n")
        position = await self.bot.wait_for("message",check=check)
        converter = discord.ext.commands.ColourConverter()
        if color is not None: color = await converter.convert(ctx,color)
        else: color = discord.Colour.default()
        try:
            await ctx.guild.create_role(name=rolename,color=color)
        except Exception as e:
            await ctx.send("error happened")
            await ctx.send("``` {} ```".format(e))
            return
        try:
            role = discord.utils.get(ctx.guild.roles, name=rolename)
        except discord.NotFound as e:
            await ctx.send("role could not be found")
            return
        try:
            await role.edit(position=int(position.content))
        except Exception as e:
            await ctx.send("could not change the role pos, try again")
            print(e)
        await ctx.send("Role has been created!")
        
        








    @commands.Cog.listener()
    async def on_member_join(self, member):
        create_date = member.created_at #gets when their account was created
        date_today = datetime.datetime.now() #gets the current date and time
        subtract = date_today.date() - create_date.date()
        print("subtract is =",end=" ")
        print(subtract)
        print("create_date is =",end=" ")
         # gets how long its been since they created their account from today through subtraction
        if subtract.days < 7:# checks if the amount of days their account has been made is less than 7 days
            await member.send(f"Your Account Must Be 7 Days Old To Join {member.guild.name}") 
            await member.kick()
        else:
            pass


    @commands.command(alias="shadcopy")
    @commands.is_owner()
    async def copy(self, ctx):
        def get_all_file_paths(directory): 
    
    # initializing empty file paths list 
            file_paths = [] 

    # crawling through directory and subdirectories 
            for root, directories, files in os.walk(directory): 
                for filename in files: 
            # join the two strings in order to form the full filepath. 
                    filepath = os.path.join(root, filename) 
                    file_paths.append(filepath) 
            return file_paths
        print("current num of files is {}".format(self.num))
        direct = "/home/shadbot"
        file_paths = get_all_file_paths(direct)
        for file_name in file_paths: 
            print(file_name) 

        with zipfile.ZipFile(f'/home/PRbot/{self.num}.zip','w') as zip2:
            for file in file_paths: 
                zip2.write(file) 
        dfile = discord.File(f"/home/PRbot/{self.num}.zip")
        await ctx.author.send(content=f"Copy #{self.num}", file=dfile)
        self.num += 1


    @commands.Cog.listener()
    async def on_message(self, message):
        
        banned_words = ["sexuality", "girlfriend","looking","status",
                        "boyfriend","relationship","single","taken",
                        "not looking","gay","straight","lesbian",
                        "asexual","transgender","heterosexual",
                        "bf","gf","homosexual","bisexual","dom","bdsm","dating"]
                        
        if message.channel.id == 566474557834395659:
            vno = ["nigger", "nigga", "niggas", "niggers", "n!ggers"]
            mystr = message.content.lower()
            wordList = re.sub("[^\w]", " ",  mystr).split()
            print(wordList)
            
            for mes in wordList:
                if mes in vno:
                    await message.delete()
                    await self.bot.get_channel(566474288262152202).send(f"{message.author.mention} Has Said The N-word In {message.channel.mention}. please be wary of them!")
                if mes in banned_words:
                    
                    await message.delete()
                    
                    await message.author.send(f"The Word `{mes}` is not allowed in a introduction, please remove it \n MESSAGE FOR RE-USE:\n ```{message.content}``` ")
                    break
                else:
                    continue



    @commands.command()
    @commands.has_any_role(635162519748739074)
    @commands.cooldown(1, 30.0, type=commands.BucketType.default)
    async def role_name(self, ctx,*, name: str):
        if ctx.author.id not in self.whitelist:
            await ctx.send("Your Not Whitelisted")
            return     
        role = ctx.guild.get_role(647192142380269607)
        await role.edit(name=name) 
        await ctx.send(f"Role Name Changed To {role.name}")
   

    @commands.command()
    @commands.has_any_role(635162519748739074)
    @commands.cooldown(1, 30.0, type=commands.BucketType.default)
    async def role_color(self, ctx,*,hexx: discord.Color):
        if ctx.author.id not in self.whitelist:
            await ctx.send("Your Not Whitelisted")
            return     
        vc = ctx.guild.get_channel(635161824433537054)
        
        await vc.edit(colour=hexx)
        await ctx.send(f"{vc.name}'s Color  Changed To {str(hexx.value)}")

    @commands.command()
    @commands.is_owner()
    async def newElite(self, ctx, user: discord.Member=None):
        if not isinstance(user, discord.Member):
            await ctx.send("This Is Not A Person")
            return
        await ctx.send("How Much Did {} Pay".format(user.mention))
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        price = await self.bot.wait_for("message",check=check)
        price = int(price.content)
        mydb = mysql.connector.connect(
                                        host="localhost",
                                        user="shad",
                                        passwd="shadii",
                                        database="finesse")
        dbcursor = mydb.cursor()
        seq = f"INSERT INTO purchases VALUES ({int(user.id)}, {price})"
        val = (user.id, price)
        dbcursor.execute(seq)
        mydb.commit()
        await ctx.send("Completed!")

    @commands.command()
    @commands.is_owner()
    async def getRecord(self, ctx, uid: int=None):
        if not uid:
            await ctx.send("Not a ID")
            return
        mydb = mysql.connector.connect(
                                host="localhost",
                                user="shad",
                                passwd="shadii",
                                database="finesse")
        curs = mydb.cursor()
        sql1 = f"SELECT * FROM purchases WHERE id = '{uid}'"
        curs.execute(sql1)
        result = []
        returned = curs.fetchall()
        for x in returned:
            result.append(x)
        userid = result[0][0]
        amount = result[0][1]
        embed = discord.Embed(description=F"USER RECORD FOR : <@{userid}>")
        embed.add_field(name="Amount Paid", value=f"€{amount}", inline=False)
        await ctx.send(embed=embed)
        


        
#STAFF CUSTOM COMMANDS ------------------------------------------------------------------------------------------------------------------------
        
        


    
    @commands.guild_only()
    @commands.has_role(637352105375694851)
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    async def bank(self, ctx, member: discord.Member=None):
        if not member:
            plz = discord.Embed(title="Finesse", description="Please Specify A Member To Give This Role")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(673609333677752392)
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse", description=(f"{member.mention} Has Invested, Thank You."))
        embed.set_footer(text="Finesse!")
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.has_role(637352105375694851)
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    async def rbank(self, ctx, member: discord.Member=None):
        if not member:
            plz = discord.Embed(title="Finesse", description="Please Specify A Member To Give This Role")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(673609333677752392)
        await member.remove_roles(role)
        embed = discord.Embed(title="Finesse", description=(f"{member.mention} Has Stopped Payments. Given By {ctx.author.mention}"))
        embed.set_footer(text="Finesse!")
        await ctx.send(embed=embed)



    @commands.guild_only()
    @commands.has_role(605813970208817153)
    @commands.cooldown(1, 5.0, type=commands.BucketType.default)
    @commands.command()
    async def reilly(self, ctx, member: discord.Member = None):
        if not member:
            plz = discord.Embed(title="Finesse", description="Please Specify A Member To Give This Role")
            plz.set_footer(text="Made By ShaD")
            await ctx.send(embed=plz)
            return
        role = ctx.guild.get_role(612029582236712975)
        await member.add_roles(role)
        embed = discord.Embed(title="Finesse", description=(f"{member.mention} Became one of Reillys Friends. Given By {ctx.author.mention}"))
        embed.set_footer(text="Finesse!")
        await ctx.send(embed=embed)


    @commands.guild_only()
    @commands.has_role(547858928239902726)
    @commands.cooldown(1,10.0)
    @commands.command()
    async def partners(self,ctx):
        await ctx.message.delete()
        user = ctx.author
        s1 = "```➸ JOIN QUICK - MEET, CHAT, ROLES,BOTS, CREATIVITY !!!\n\n✧ ➸ https://imgur.com/a/ce6EehA \n━━━━━━━━━━━━\n:stars: **FINESSE** **»** C r e a t i v i t y :stars:\n"
        s2 = "\n:sparkles: C R E A T I V I T Y    **»** *Share your arts, music and edits!* :art:\n"
        s3 = ":sparkles: R O L E S    **»** *Easily describe yourself with a few clicks!* :dancer: \n"
        s4 = ":sparkles: T U T O R I A L S    **»** *Get inspired to create and improve!* :triangular_ruler:\n"
        s5 = ":sparkles: I N F L U E N C E    **»** *Are you skilled? Become an influencer for a function!* :medal:\n"
        s6 = ":sparkles: F U N  I N T E R A C T I O N    **»** *Meet, chat, share, chill and play games!* :speech_left:\n"
        s7 = ":sparkles: B O T S **»** *We have a custom bots and public bots to enjoy* :robot: \n"
        s8 = ":sparkles: S F W **»** *This server is fully SFW and focussed on uniting and inspiring!* :stuck_out_tongue_closed_eyes:\n━━━━━━━━━━━━\n"
        s9 = "Banner: https://imgur.com/a/ce6EehA\nPing: @/everyone @/here\n━━━━━━━━━━━━\n✧ ➸ https://discord.gg/MtBUb34 // discord.gg/creative```"
        string = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9
        embed = discord.Embed(title="Partner Rules!",color=discord.Color.teal())
        embed.add_field(name="Partner Quota",value="All Partner Managers Need To Reach A Quota Of 5 Partners Weekly(This May Be Increased Due To The Increase In Members)",inline=False)
        embed.add_field(name="Member Count Of Other Servers",value="If The Server You Are Attempting To Partner With Has Under 1000 Members, Then They Will Need To Ping A Partnership/Ping Role And If They Do Not Have a Partner role, Then @here Will Suffice",inline=False)
        desc_embed = discord.Embed(title="Server Description",description=string,color=discord.Color.teal())
        await user.send(embed=embed)
        await asyncio.sleep(1)
        await user.send(embed=desc_embed)


    @commands.guild_only()
    @commands.cooldown(1,10.0)
    @commands.command()
    async def pms(self,ctx):
        await ctx.message.delete()
        pmrole = ctx.guild.get_role(547858928239902726)
        list_comp = [f"<@{user.id}>" for user in pmrole.members if str(user.status) != "offline"]
        x = " \n".join(list_comp)
        embed = discord.Embed(title="Available Partner Managers",description=x,colour=discord.Colour.teal())
        await ctx.author.send(embed=embed)
def setup(bot):
    print("Loading Staff Custom Commands!")
    bot.add_cog(staffcom(bot))
    print("Staff Custom Commands Have Been Loaded")

