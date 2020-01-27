import logging
import datetime
import random
import os
import os.path
import shadsmod
import json
import discord
from pathlib import Path
from discord.ext import commands
from discord.ext import tasks
import time
import asyncio
import sys, traceback




class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

class helps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command
    

def setup(bot):
    print("Loading custom command System!")
    bot.add_cog(helps(bot))
    print("custom command sys loaded")
