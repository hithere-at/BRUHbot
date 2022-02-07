# Import all required libaries
import dns.resolver # Resolver fix
import random
import os # .env file
import discord
import pymongo
from discord.ext import commands
from discord.commands import slash_command, SlashCommandGroup, Option

# DNS fix in case resolver configuration is f*cked up ._. this fix save me
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

# Functions to write user zenny to MongoDB database
def update_doc(user_id, amount: int, operator: str):
	user_zen = zenny.find_one({"_id": user_id}, limit=1)

	if operator == "substract":

		if user_zen["value"] < res:
			zenny.update_one({"_id": user_id}, {"$set": {"value": user_zen["value"] - user_zen["value"]}})

		else:
			zenny.update_one({"_id": user_id}, {"$set": {"value": user_zen["value"] - amount}})


	elif operator == "add":
		zenny.update_one({"_id": user_id}, {"$set": {"value": user_zen["value"] + amount}})

def write_new_doc(info):
	zenny.insert_one(info)

# Initialize MongoDB client
client = pymongo.MongoClient(f'{os.getenv("MONGODB_URI")}')
db = client["money"]
zenny = db["zen"]

# Initialize currency commands
class Economy(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	hunter_shop = SlashCommandGroup("shop", "Shop for the hunters")

	@slash_command(description="Claim your daily zenny")
	@commands.cooldown(1, 86400, commands.BucketType.user)
	@commands.max_concurrency(1, commands.BucketType.user, wait=True)
	async def daily(self, ctx):

		await ctx.defer()

		id = str(ctx.author.id) # Change author id from integer to string, idk why i did this
		documents = zenny.count_documents({"_id": id}, limit=1)
		pls_help = discord.Embed(title = 'Daily Zenny', description = 'The "thing" give you 2500z. The money has been given to you', color = 0x4050FF)
		pls_help.set_thumbnail(url = f'{ctx.author.avatar.url}')

        # If author document exist, then add 2500 to author current zenny
		if documents != 0:
			update_doc(id, 2500, "add")

        # Else, write a new document for author
		else:
			write_new_doc({"_id": id, "value": 2500})

		await ctx.respond(embed=pls_help)

	@daily.error
	async def on_command_error(self, ctx, error):

		oof = ['Command is on cooldown', 'Are you trying to spam daily command ?']

		if isinstance(error, commands.CommandOnCooldown):
			await ctx.respond(random.choice(oof))

	@slash_command(description="Check how much you have zenny on your wallet")
	@commands.max_concurrency(1, commands.BucketType.user, wait=True)
	async def balance(self, ctx):

		await ctx.defer()

		id = str(ctx.author.id)
		documents = zenny.count_documents({"_id": id}, limit=1)

        # If author document exist, then make find author document with their discord id as query
		if documents != 0:
			user_zenny = zenny.find_one({"_id": id}, limit=1)
			await ctx.respond(f'You have this much money: {user_zenny["value"]}z')

        # Else, just say that they're economically bruh in our currency system :)
		else:
			await ctx.respond('you absolutely have no money. do something to fill it')

	@slash_command(description="Depart to a quest and kill monster")
	@commands.cooldown(1, 1800, commands.BucketType.user) # 30 minute cooldown for each quest per user
	@commands.max_concurrency(1, commands.BucketType.user, wait=True)
	async def quest(self, ctx):

		await ctx.defer()

		heavy_weapon_guy = ['a big', 'an average', 'a small', "failed"]
		decide_urfate = random.choice(heavy_weapon_guy)
		res = 0
		amount = 0
		id = str(ctx.author.id)
		bruh = zenny.find_one({"_id": id}, limit=1)
		documents = zenny.count_documents({"_id": id}, limit=1)

		if bruh.get("2x_zen_active") is True: amount = 2
		else: amount = 1

        # Someone optimize this please. Thank you :D
		if documents != 0 and decide_urfate == 'a small':
			res = random.randint(1500, 3500) * amount
			update_doc(id, res, "add")

		elif documents != 0 and decide_urfate == 'an average':
			res = random.randint(4000, 6500) * amount
			update_doc(id, res, "add")

		elif documents != 0 and decide_urfate == 'a big':
			res = random.randint(6501, 9500) * amount
			update_doc(id, res, "add")

		elif documents != 0 and decide_urfate == 'failed':
			res = random.randint(1000, 5000)
			update_doc(id, res, "substract")
			huh = discord.Embed(title='Quest Result', description=f'Quest failed. You lost {res}z', color=0xBC18C4)

		elif documents == 0 and decide_urfate == 'a small':
			res = random.randint(1500, 3500)
			write_new_doc({"_id": id, "value": res})

		elif documents == 0 and decide_urfate == 'an average':
			res = random.randint(4000,6500)
			write_new_doc({"_id": id, "value": res})

		elif documents == 0 and decide_urfate == 'a big':
			res = random.randint(6501, 9500)
			write_new_doc({"_id": id, "value": res})

		elif documents == 0 and decide_urfate == 'failed':
			write_new_doc({"_id": id, "value": 2500})
			huh = discord.Embed(title='Quest Result', description='Quest failed. But because you are new, you get 2500z as compensation', color=0xBC18C4)

		if res != 0 and decide_urfate != 'failed':
			huh = discord.Embed(title='Quest Result', description=f'You killed {decide_urfate} monster. You get {res}z', color=0xBC18C4)

		if bruh.get("2x_zen_active") is True:
			zenny.update_one({"_id": id}, {"$unset": {"2x_zen_active": ""}})

		huh.set_thumbnail(url=f'{ctx.author.avatar.url}')

		await ctx.respond(embed=huh)

	@quest.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.CommandOnCooldown):
			await ctx.respond('You just killed a monster before, go rest')

	@slash_command(description="Give your zenny to someone")
	@commands.max_concurrency(1, commands.BucketType.user, wait=True)
	async def share(self, ctx, amount: Option(int, "How much?"), receiver: Option(discord.Member, "To who?")):

		await ctx.defer()

		author_id = str(ctx.author.id)
		receiver_id = str(receiver.id) # Get discord id of the member that the user want to give to
		author_zenny = zenny.find_one({"_id": author_id}, limit=1)
		documents = zenny.count_documents({"_id": author_id}, limit=1)
		receiver_acc = zenny.count_documents({"_id": receiver_id}, limit=1)

		if documents != 0 and receiver_acc != 0 and author_zenny["value"] >= amount:
			update_doc(receiver_id, amount, "add") # Increase the member argument or receiver zenny
			update_doc(author_id, amount, "substract") # Decrease author zenny
			await ctx.respond(f'{amount}z has been given to {to_where.name}')

		elif documents != 0 and receiver_acc == 0 and author_zenny["value"] >= amount:
			receiver_info = {"_id": receiver_id, "value": amount}
			write_new_doc(receiver_info) # In case the member argument doesnt have a document, make a new one
			update_doc(author_id, amount, "substract") # Decrease the author zenny
			await ctx.respond(f'{amount}z has been given to {to_where.name}')

		else:
			await ctx.respond("looks like there is an error. make sure your zenny is more than the zenny you want to give and make sure your account exists")

	@slash_command(description="Use the item that you buy on the store for next quest")
	@commands.max_concurrency(1, commands.BucketType.user, wait=True)
	async def useitem(self, ctx, item_id: Option(str, "Pick the item id", choices=["2x_zen"])):

		await ctx.defer()

		exist = zenny.count_documents({"_id": str(ctx.author.id)}, limit=1)

		if exist == 0:
			await ctx.respond("You're not even a hunter")
			return

		item_list = {"2x_zen": ["2X Zenny card", "2x_zen"]}

		if item_list.get(item_id) is None:
			await ctx.respond("No such item available")
			return

		bored = zenny.find_one({"_id": str(ctx.author.id)}, limit=1)
		item = bored.get(item_id)
		item_active = bored.get(f'{item_list.get(item_id)[1]}_active')

		if item_active is True:
			await ctx.respond(f'{item_list[item_id][0]} has been activated already')
			return

		if item == 0 or item is None:
			await ctx.respond(f"You dont have a {item_list[item_id][0]}")

		elif item is not None:
			zenny.update_one({"_id": str(ctx.author.id)}, {"$set": {item_list[item_id][1]: item - 1, f"{item_list[item_id][1]}_active": True}})
			await ctx.respond(f"{item_list[item_id][0]} activated. It will be used for your next quest")

		else:
			await ctx.respond("Something went wrong")

	@hunter_shop.command(description="List all things that the store have")
	@commands.max_concurrency(1, commands.BucketType.user, wait=True)
	async def list(self, ctx):

		shop_embed = discord.Embed(title="Hunter's Shop", description="This is where you buy stuff for your hunter needs", color=0xAB34EB)
		shop_embed.add_field(name="2X Zenny / Item ID: \"2x_zen\" | 12000z", value="Give you twice the amount that you get from doing quest. It use a 2X Zenny card per quest if you activate this")
		shop_embed.add_field(name="Advanced Gear / Item id: \"nice_gear\" | 200000z", value="Increase the chance to meet bigger monster to get more zenny. This item is permanent (Coming Soon)")
		shop_embed.set_footer(text="More stuff coming soon. Sorry if the shop is small :)")

		await ctx.respond(embed=shop_embed)

	@hunter_shop.command(description="Buy an item from the hunter's shop")
	@commands.max_concurrency(1, commands.BucketType.user, wait=True)
	async def buy(self, ctx, item_id: Option(str, "Pick the item id", choices=["2x_zen"]), amount: Option(int, "How much?")):

		await ctx.defer()

		shit = zenny.count_documents({"_id": str(ctx.author.id)}, limit=1)

		if amount == 0:
			await ctx.respond("really, buying nothing?")
			return

		elif shit == 0:
			await ctx.respond("you're not in our hunter list. go do some quest or somethin")
			return

		no = zenny.find_one({"_id": str(ctx.author.id)}, limit=1)

		if item_id == "2x_zen" and no["value"] >= amount*12000:
			zenny.update_one({"_id": str(ctx.author.id)}, {"$set": {"value": no["value"] - 12000*amount, "2x_zen": amount}})
			await ctx.respond(f'You have {amount} 2X Zenny card')

		elif item_id == "nice_gear" and no ["value"] >= 200000:
			zenny.update_one({"_id": str(ctx.author.id)}, {"$set": {"value": no["value"] - 200000, "nice_gear": True}})
			await ctx.respond("You got the Advanced Gear, nice")

		elif item_id == "2x_zen" and no["value"] < amount*12000:
			await ctx.respond(f'You dont have money enough to buy {amount} of 2X Zenny')

		elif item_id == "nice_gear" and no["value"] < 200000:
			await ctx.respond(f'You dont have money enough to buy an Advanced Gear')

		else:
			await ctx.respond("cant find such item. please check if you type the item id correctly")

def setup(bot):
	bot.add_cog(Economy(bot))
