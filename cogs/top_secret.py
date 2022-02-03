import discord
import asyncio
from discord.ext import commands
from discord.commands import slash_command

class ForbiddenCommands(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@slash_command(description="What is it")
	async def whatsthemeaningoflife(self, ctx):

		await ctx.respond("_ _")

		for x in range(5):
			await ctx.author.send('im watching you')
			await asyncio.sleep(1)

	@slash_command(description="Me too")
	async def idkwhatisthemeaningoflife(self, ctx):

		await ctx.respond('https://tenor.com/view/smiley-3d-vibe-check-creepy-gif-15669762')

	@slash_command(description="No, i didn't")
	async def doyouknowwhoateallthedoughnuts(self, ctx):

		await ctx.respond(file=discord.File('./pictures/SPOILER_spicy_pic.jpg'))

class amogus(commands.Cog):

	def __init__(self, bot):
			self.bot = bot

	@slash_command(description="ummmmm what?")
	async def sus(self, ctx):

		await ctx.respond('https://tenor.com/view/sus-gif-20302681')

	@slash_command(description="die")
	async def kill(self, ctx):

		await ctx.respond('https://tenor.com/view/among-us-kill-gif-19295404')

def setup(bot):
	bot.add_cog(ForbiddenCommands(bot))
	bot.add_cog(amogus(bot))