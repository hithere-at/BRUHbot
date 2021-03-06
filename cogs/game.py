# Import all required libaries
import discord
import time
import random
import secrets
from discord.ext import commands
from discord.commands import slash_command, Option

class RPSButton(discord.ui.View):

	def __init__(self):
		super().__init__(timeout=8.0)
		self.value = 0

	async def close_inter(self):

		for gonna_die in self.children:
			gonna_die.style = discord.ButtonStyle.grey
			gonna_die.disabled = True

	@discord.ui.button(label="Rock", style=discord.ButtonStyle.grey)
	async def rock(self, button: discord.ui.Button, inter: discord.Interaction):
		self.value = 1
		self.stop()
		await self.close_inter()
		await inter.response.edit_message(view=self)

	@discord.ui.button(label="Paper", style=discord.ButtonStyle.green)
	async def paper(self, button: discord.ui.Button, inter: discord.Interaction):
		self.value = 2
		self.stop()
		await self.close_inter()
		await inter.response.edit_message(view=self)

	@discord.ui.button(label="Scissor", style=discord.ButtonStyle.red)
	async def scissor(self, button: discord.ui.Button, inter: discord.Interaction):
		self.value = 3
		self.stop()
		await self.close_inter()
		await inter.response.edit_message(view=self)

# Collection of "Game" commands
class Game(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	# Rock-Paper-Scissor command
	@slash_command(description="Play Rock-Paper-Scissor with the bot")
	async def rps(self, ctx):

		name = {1: "Rock", 2: "Paper", 3: "Scissor"}
		rules = {1: 3, 2: 1, 3: 2}
		enemy = secrets.choice([1, 2, 3]) # Basically the same as random.choice but more secure
		choices = RPSButton()

		await ctx.respond("Welcome to rock paper scissor, please choose one the following choices\n1. Rock\n2. Paper\n3. Scissor\nYou have 8 seconds to choose", view=choices)
		await choices.wait()
		# Is there a better way to check if the player win, i hope someone optimize this (it was a gigantic elif statements)
		# Optimized, credit goes to TechAndNews/Python-Scripts (GitHub)

		if choices.value == 0:
			await choices.close_inter()
			await ctx.interaction.edit_original_message(view=choices)
			await ctx.respond("Timeout")

		elif choices.value == enemy:
			await ctx.respond(f'You: {name[choices.value]}\nEnemy: {name[enemy]}\nDraw!')

		elif rules[choices.value] == enemy:
			await ctx.respond(f'You: {name[choices.value]}\nEnemy: {name[enemy]}\nYou win!')

		else:
			await ctx.respond(f'You: {name[choices.value]}\nEnemy: {name[enemy]}\nYou lost!')

	# Guess the number command
	@slash_command(description="Play \"Guess the number\" game")
	async def guessnum(self, ctx, lower: Option(int, "Lowest possible number"), upper: Option(int, "Highest possible number")):

		if lower > upper:
				await ctx.respond("lowerbound is greater than upperbound. not possible")
				return

		num = random.randrange(lower, upper)
		checker = lambda x: x.author == ctx.author and x.channel == ctx.channel

		await ctx.respond("Guess now. You have 15 seconds and one chance")

		try:
			guess = await self.bot.wait_for("message", check=checker, timeout=15)

		except asyncio.TimeoutError:
			return await ctx.respond("Timeout. Quitting...")

		try:
			temp = int(guess.content)

		except ValueError:
			return await ctx.respond("In number, not in words. Quitting")

		if temp == num:
			await ctx.respond("You are right")

		else:
			await ctx.respond("You are wrong, try again")

def setup(bot):
	bot.add_cog(Game(bot))
