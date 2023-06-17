import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx):
 await ctx.send("heya")


bot.run("MTExOTI0Njg5NDUyNzQzMDcyNw.GGIosW.UcqTzFFccoyBXoDF27b5lAvR7B7Y8X0YvngGcY")
