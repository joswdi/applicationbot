import discord
from discord.ext import commands

bot = None

def set_bot(bot_instance):
    global bot
    bot = bot_instance

def get_bot():
    return bot