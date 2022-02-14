from webserver import keep_alive

import os
import discord 
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option



client  = commands.Bot(command_prefix='!')
slash = SlashCommand(client, sync_commands=True)

@slash.slash(
    name= "Hi",
    description="Just send a message",
    guild_ids = [942720087687839754]
)

async def _Hello(ctx:SlashContext,):
    await ctx.send("Hi there")



keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)

