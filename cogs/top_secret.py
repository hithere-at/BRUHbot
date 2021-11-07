import discord
import random
import asyncio
import secrets
from discord.utils import get
from discord.ext import commands

class ForbiddenCommands(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases = ['73&rhd8djdiieiedn'])
	async def whatsthemeaningoflife(self, ctx):

		for x in range(5):
			await ctx.author.send('im watching you')
			await asyncio.sleep(1)

	@commands.command(aliases = ['dontdoit'])
	async def idkwhatisthemeaningoflife(self, ctx):

		await ctx.reply('https://tenor.com/view/smiley-3d-vibe-check-creepy-gif-15669762', mention_author = True)

	@commands.command(aliases = ['spicypic'])
	async def doyouknowwhoateallthedoughnuts(self, ctx):

		await ctx.reply(file = discord.File('./pictures/SPOILER_spicy_pic.jpg'), mention_author = True)

class amogus(commands.Cog):

	def __init__(self, bot):
			self.bot = bot

	@commands.command()
	async def sus(self, ctx):

		await ctx.reply('https://tenor.com/view/sus-gif-20302681', mention_author = True)

	@commands.command()
	async def kill(self, ctx):

		await ctx.reply('https://tenor.com/view/among-us-kill-gif-19295404', mention_author = True)

def setup(bot):
	bot.add_cog(ForbiddenCommands(bot))
	bot.add_cog(amogus(bot))
