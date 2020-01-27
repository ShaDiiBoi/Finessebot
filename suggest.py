
import discord
from pathlib import Path
import time
import sys, traceback
import logging
import datetime
import json
import os.path
from discord.ext import commands
from collections.abc import Sequence
import asyncio


class suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.blacklist = []


    @commands.Cog.listener()
    async def on_message(self,message):
        if message.channel.id == 566781963286085642:
            if ".suggest" not in message.content and message.author.id != 530945830006292480:
                await message.delete()


    @commands.command()
    @commands.cooldown(1, 500.0, type=commands.BucketType.user)
    async def suggest(self, ctx):
        if ctx.author.id in self.blacklist:
            await ctx.author.send("You Are Blacklisted From Suggesting")
            return
        #Variables For Use
        altera = self.bot.get_guild(523042374209765377)
        suggestions_channel = altera.get_channel(616046324491485214)
        
        user = ctx.author
        await ctx.message.delete()
        body_message = "What Is Your Suggestion, Please Detail It Well:"
        reason_message = "How Should Your Suggestion Be Implemented"
        why_message = "How Would This Suggestion Better Finesse?"
        suggestion_body = ""
        suggestion_reason = "" 
        suggestion_why = ""
        await user.send(body_message)#literally telling random people "we are trying to get proof on reilly being a pedo"
        def check1(m):
            return isinstance(m.channel, discord.abc.PrivateChannel) and m.author.id == user.id
        suggestionBodyGen = await self.bot.wait_for("message", check=check1)
        await user.send(reason_message) 
        reasonBodyGen = await self.bot.wait_for("message",check=check1)
        await user.send(why_message)
        whySugGen = await self.bot.wait_for("message",check=check1)
        suggestion_body = suggestionBodyGen.content
        suggestion_reason = reasonBodyGen.content
        suggestion_idea = whySugGen.content
        embedparts = [suggestion_body,suggestion_reason,suggestion_idea]
        embedq = [body_message,reason_message,why_message]
        inter = embedparts + embedq
        embedstuff = list(zip(embedparts, embedq))
        suggestion = discord.Embed(title=f"{ctx.author.id}",description=F"Suggestion System(Requested By {ctx.author.mention})",color=0xff85d5)
        for information in embedstuff:
            suggestion.add_field(name=information[1],value=information[0])
        suggestion_message = await suggestions_channel.send(embed=suggestion)
        emoji_list = ["✅","❌","⏫","⏬","⛔"]
        for emoji in emoji_list:
            await suggestion_message.add_reaction(f"{emoji}")
        await user.send("Suggestion Has Been Sent For Review!")



    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        if payload.user_id == self.bot.user.id:
            return
        server = self.bot.get_guild(payload.guild_id)
        altera = self.bot.get_guild(523042374209765377)
        finesse = self.bot.get_guild(534050853477285888)
        channel = server.get_channel(payload.channel_id)
        emoji = payload.emoji
        if channel.id == 616046324491485214:
            log_chan = self.bot.get_channel(616286983010123787)
            todo_channel = altera.get_channel(616082763509923927)
            judge = self.bot.get_user(payload.user_id)
            emoji = payload.emoji
            msg = await channel.fetch_message(payload.message_id)
            embed = msg.embeds[0]
            user = self.bot.get_user(int(embed.title))
            member = altera.get_member(payload.user_id)
            judge = self.bot.get_user(payload.user_id)
            if str(emoji) == "✅":
                manager = altera.get_role(553271668152336412)
                if manager not in member.roles:
                    await msg.remove_reaction(emoji, judge)
                    return
                await msg.delete()
                await user.send("Your Suggestion Has Been Accepted, And Will Be Implemented In The Coming Days, Please Expect A Review Time Of At Most 5 Days")
                log_embed = discord.Embed(title="Logs",description=F"{judge.mention} Has Accepted {user.mention}'s Suggestion")
                await log_chan.send(embed=log_embed)
                await todo_channel.send(embed=embed)
               
            if str(emoji) == "❌":
                await msg.delete()
                log_embed = discord.Embed(title="Logs",description=F"{judge.mention} Has Denied {user.mention}'s Suggestion")
                await log_chan.send(embed=log_embed)
                await user.send("Your Suggestion Has Been Denied")
                return
            if str(emoji) == "⏫":
                trainee = altera.get_role(553271228035497984)

                if trainee in member.roles:
                    await msg.remove_reaction(emoji, judge)
                    return
                log_embed = discord.Embed(title="Logs",description=F"{judge.mention} Has Upvoted {user.mention}'s Suggestion")
                await log_chan.send(embed=log_embed)
            if str(emoji) == "⏬":
                trainee = altera.get_role(553271228035497984)
                if trainee in member.roles:
                    await msg.remove_reaction(emoji, judge)
                    return
                log_embed = discord.Embed(title="Logs",description=F"{judge.mention} Has Downvoted {user.mention}'s Suggestion")
                await log_chan.send(embed=log_embed)
            if str(emoji) == "⛔":
                manager = altera.get_role(553271668152336412)
                await msg.delete()
                if manager not in member.roles:
                    await msg.remove_reaction(emoji, judge)
                    return
                self.blacklist.append(user.id)
                log_embed = discord.Embed(title="Logs",description=F"{judge.mention} Has Blacklisted {user.mention}")
                await log_chan.send(embed=log_embed)
                await user.send("You have been blacklisted from suggesting anything through this system, please contact a staff member if you think this is unjust")
            

            return
        



    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            error_time = str(error.retry_after)
            await ctx.author.send(f"This Command Is On Cooldown, Please Try Again After `{error_time[0:5]}` Seconds")




def setup(bot):
    print("Loading Suggestion System!")
    bot.add_cog(suggestions(bot))
    print("Suggestion System  Has Loaded!")
