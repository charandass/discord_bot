from webserver import keep_alive

import os
import discord 
from discord.ext import commands

client = discord.Client()
client  = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("$hi"):
    await message.channel.send("hello")
  
  if msg.startswith("$TodaySales"):
    await message.channel.send(450000)

  if msg.startswith("$WeeklySales"):
    await message.channel.send(9800000)


keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)


# from discord.ext import commands
# from discord import guild
# from discord_slash import SlashCommand, SlashContext
# from discord_slash.utils.manage_commands import create_choice, create_option


# client  = commands.Bot(command_prefix='!')
# slash = SlashCommand(client, sync_commands=True)

# @slash.slash(
#     name= "Hi",
#     description="Just send a message",
#     guild_ids = [942720087687839754]
# )

# @slash.slash(
#   name='sales',
#   description="Tells you the sales today",
#   guild_ids = [942720087687839754]
# )

# async def _Sales(ctx:SlashContext):
#   await ctx.send(4560000)

# async def _Hello(ctx:SlashContext,):
#     await ctx.send("Hi there")
