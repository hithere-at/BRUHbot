import json
import random
import discord
from discord.ext import commands

def dump_data(od_data, user_id, amount, where):
	od_data[user_id] = od_data[user_id] + amount
	json.dump(od_data, where)

def dump_new_data(nw_data, member_id, number, no_idea):
	stuff = {member_id: number}
	nw_data.update(stuff)
	no_idea.seek(0)
	json.dump(nw_data, no_idea)

class currency(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.cooldown(1, 86400, commands.BucketType.user)
	@commands.max_concurrency(1, commands.BucketType.user, wait = True)
	async def daily(self, ctx):

		with open('hello.json', 'r') as file:
			temp = json.load(file)

		id = str(ctx.author.id)
		pls_help = discord.Embed(title = 'Daily Zenny', description = 'The "thing" give you 2500z. The money has been given to you', color = 0x4050FF)
		pls_help.set_thumbnail(url = f'{ctx.author.avatar_url}')

		if id in temp:

			with open('hello.json', 'r+') as file:
				dump_data(temp, id, 2500, file)

		else:

			with open('hello.json', 'r+') as file:
				dump_new_data(temp, id, 2500, file)

		await ctx.reply(embed = pls_help, mention_author = True)

	@daily.error
	async def on_command_error(self, ctx, error):

		oof = ['Command is on cooldown', 'Are you trying to spam daily command ?']

		if isinstance(error, commands.CommandOnCooldown):
			await ctx.reply(random.choice(oof), mention_author = True)

		if isinstance(error, commands.MaxConcurrencyReached):
			await ctx.reply('A hunter is still on queue waiting for the same thing like you, Please wait', mention_author = True)

	@commands.command(aliases = ['bal'])
	async def balance(self, ctx):

		with open('hello.json', 'r') as file:
			temp = json.load(file)

		id = str(ctx.author.id)

		if id in temp:
			await ctx.reply(f'You have this much money: {temp[id]}z', mention_author = True)


		else:
			await ctx.reply('you absolutely have no money. do something to fill it', mention_author = True)

	@commands.command()
	@commands.cooldown(1, 1800, commands.BucketType.user)
	@commands.max_concurrency(1, commands.BucketType.user, wait = True)
	async def quest(self, ctx):

		heavy_weapon_guy = ['a big', 'an average', 'a small']
		decide_urfate = random.choice(heavy_weapon_guy)

		with open('hello.json', 'r') as file:
			temp = json.load(file)

		res = None
		id = str(ctx.author.id)

		if id in temp:
			if decide_urfate == 'a small':

				with open('hello.json', 'r+') as file:
					reward1 = random.randint(1500, 3501)
					dump_data(temp, id, reward1, file)
					res = reward1

			elif decide_urfate == 'an average':

				with open('hello.json', 'r+') as file:
					reward2 = random.randint(4000, 6501)
					dump_data(temp, id, reward2, file)
					res = reward2

			elif decide_urfate == 'a big':

				with open('hello.json', 'r+') as file:
					reward3 = random.randint(6501, 9501)
					dump_data(temp, id, reward3, file)
					res = reward3

		else:
			if decide_urfate == 'a small':

				with open('hello.json', 'r+') as file:
					reward4 = random.randint(1500, 3501)
					dump_new_data(temp, id, reward4, file)
					res = reward4

			elif decide_urfate == 'an average':

				with open('hello.json', 'r+') as file:
					reward5 = random.randint(4000,6501)
					dump_new_data(temp, id, reward5, file)
					res = reward5

			elif decide_urfate == 'a big':

				with open('hello.json', 'r+') as file:
					reward6 = random.randint(6501, 9501)
					dump_new_data(temp, id, reward6, file)
					res = reward6

		huh = discord.Embed(title = 'Quest Result', description = f'You killed {decide_urfate} monster. You get {res}z', color = 0xBC18C4)
		huh.set_thumbnail(url = f'{ctx.author.avatar_url}')

		await ctx.reply(embed = huh, mention_author = True)

	@quest.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.CommandOnCooldown):
			await ctx.reply('You just killed a monster before, go rest', mention_author = True)

		if isinstance(error, commands.MaxConcurrencyReached):
			await ctx.reply('A hunter is still on a quest, try again in a few moments')

def setup(bot):

	bot.add_cog(currency(bot))
