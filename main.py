from webserver import keep_alive

import os
import discord 
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

from googlesearch import search





# guild_id = [942720087687839754]


# client  = commands.Bot(command_prefix='!')
bot = commands.Bot(command_prefix="/",case_insensitive=True
	)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def hi(ctx):
		author = ctx.author.mention
		await ctx.send(f":wave: Hello there!!:wave: \n Glad to see you {author} !")



@bot.command()
async def find(ctx,*, query):
		author = ctx.author.mention
		await ctx.channel.send(f"Here are the links related to your question {author} !")
		async with ctx.typing():
				for j in search(query, tld="co.in", num=5, stop=5, pause=2): 
						await ctx.send(f"\n:point_right: {j}")
				await ctx.send("Have any more questions:question:\nFeel free to ask again :smiley: !")






# @slash.slash(
#     name= "Hi",
#     description="Just send a message",
#     guild_ids = guild_id
# )
# async def _Hello(ctx:SlashContext,):
#     await ctx.send("Hi there")

@slash.slash(
  name='todaysales',
  description="Tells you the today's sales ",
  # guild_ids = guild_id
)

async def _TodaySales(ctx:SlashContext):
  await ctx.send(4560000)

@slash.slash(
  name='weeklysales',
  description="Tells you the stoday",
  # guild_ids = guild_id
)

async def _WeeklySales(ctx:SlashContext):
  await ctx.send(98000000)


@slash.slash(
  name='balance',
  description="Tells you the stoday",
  # guild_ids = guild_id
)

async def _Balance(ctx:SlashContext):
  await ctx.send(7800000000)





keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)
# client.run(TOKEN)








