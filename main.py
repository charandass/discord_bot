from webserver import keep_alive

import os
import discord 
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

guild_id = [942720087687839754]


client  = commands.Bot(command_prefix='!')
slash = SlashCommand(client, sync_commands=True)

@slash.slash(
    name= "Hi",
    description="Just send a message",
    guild_ids = guild_id
)
async def _Hello(ctx:SlashContext,):
    await ctx.send("Hi there")

@slash.slash(
  name='todaysales',
  description="Tells you the today's sales ",
  guild_ids = guild_id
)

async def _TodaySales(ctx:SlashContext):
  await ctx.send(4560000)

@slash.slash(
  name='weeklysales',
  description="Tells you the stoday",
  guild_ids = guild_id
)

async def _WeeklySales(ctx:SlashContext):
  await ctx.send(98000000)


@slash.slash(
  name='balance',
  description="Tells you the stoday",
  guild_ids = guild_id
)

async def _Balance(ctx:SlashContext):
  await ctx.send(7800000000)





keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)








