

import asyncio
import datetime
import json
import os
import os.path
import random
import sys
import time
import traceback
import typing
from collections.abc import Sequence
from pathlib import Path
import discord
import mysql.connector
from discord.ext import commands

mydb = mysql.connector.connect(
                    host="localhost",
                    user="shad",
                    passwd="shadii",
                    database="finesse")
dbcursor = mydb.cursor(buffered=True)
def xcute(seq,values: tuple=None):
    if values is None:
        dbcursor.execute(seq)
        results = dbcursor.fetchall()
        mydb.commit()
        return results
    if values is not None:
        dbcursor.execute(seq,values)
        results = dbcursor.fetchall()
        mydb.commit()
        return results

def pull(*args):
    dbcursor.execute(*args)
    results = dbcursor.fetchall()
    return results
    


def get_blacklist():
    seq = "SELECT uid FROM blacklist"
    dbcursor.execute(seq)
    results = dbcursor.fetchall()
    return list(results)
