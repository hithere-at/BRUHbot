import discord
from discord.ext import commands
import random

class NormalStuff(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def sup(self, ctx):

		if ctx.author.id == 668794109020078080:
			sup_response_motheye = ['moth ? Is that you ? wassup my man',
						'how is life ?',
						'Endless Agony sequel when ?']
			await ctx.reply(random.choice(sup_response_motheye), mention_author = True)

		else:
			sup_response = ['yo wassup',
					'shut up lol',
					'uhhh, are you talking to me ?',
					'ok',
					'phishe']
			await ctx.reply(random.choice(sup_response), mention_author = True)

	@commands.command()
	async def givefood(self, ctx, *, food: str):

		food = food.replace(' ', '_')
		phishe_list = ['hamburger',
				'pizza',
				'bacon',
				'bread',
				'doughnut',
				'candy',
				'chocolate_bar',
				'ice_cream',
				'rice',
				'rice_ball',
				'green_apple',
				'apple','pear',
				'tangerine',
				'lemon',
				'banana',
				'watermelon',
				'grapes',
				'blueberries',
				'strawberry',
				'melon',
				'cherries',
				'mango',
				'peach',
				'pineapple',
				'tomato',
				'coconut',
				'eggplant',
				'kiwi',
				'avocado',
				'olive',
				'broccoli',
				'leafy_green',
				'bell_pepper',
				'cucumber',
				'hot_pepper',
				'corn',
				'carrot',
				'french_bread',
				'bagel',
				'garlic',
				'onion',
				'croissant',
				'potato',
				'sweet_potato',
				'flatbread',
				'pretzel',
				'cheese',
				'egg',
				'cooking',
				'butter',
				'pancakes',
				'waffle',
				'cut_of_meat',
				'poultry_leg',
				'meat_on_bone',
				'hotdog','fries',
				'sandwich',
				'stuffed_flatbread',
				'falafel',
				'taco',
				'burrito',
				'tamale',
				'salad',
				'shallow_pan_of_food',
				'fondue',
				'canned_food',
				'spaghetti',
				'ramen',
				'stew',
				'curry',
				'sushi',
				'bento',
				'dumpling',
				'oyster',
				'fried_shrimp',
				'rice_cracker',
				'fish_cake',
				'fortune_cookie',
				'moon_cake',
				'oden',
				'dango',
				'shaved_ice',
				'icecream',
				'pie',
				'cupcake',
				'cake',
				'custard',
				'lollipop',
				'popcorn',
				'cookie',
				'chestnut',
				'peanuts',
				'honey_pot',
				'milk',
				'baby_bottle',
				'coffee',
				'tea',
				'teapot',
				'mate',
				'bubble_tea',
				'beverage_box',
				'cup_with_straw',
				'sake',
				'beer',
				'beers',
				'champagne_glass',
				'wine_glass',
				'tumbler_glass',
				'cocktail',
				'tropical_drink',
				'champagne',
				'ice_cube',
				'spoon',
				'fork_and_knife',
				'fork_knife_plate',
				'bowl_with_spoon',
				'takeout_box',
				'chopsticks',
				'salt']

		if any(phishe in food for phishe in phishe_list):
			await ctx.reply(f'Here you go :{food}:', mention_author = True)

		else:
			await ctx.reply('no such food found on discord food emoji list', mention_author = True)

	@givefood.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('give what', mention_author = True)

	@commands.command()
	async def pfp(self, ctx, gman: discord.Member = None):

		if gman == None:
			author_pic_embed = discord.Embed(title = '', description = '', color = discord.Color.blue())
			author_pic_embed.set_image(url = ctx.author.avatar_url)
			await ctx.reply(embed = author_pic_embed, mention_author = True)

		else:
			pic_embed = discord.Embed(title = '', description = '', color = discord.Color.blue())
			pic_embed.set_image(url = gman.avatar_url)
			await ctx.reply(embed = pic_embed, mention_author = True)

	@commands.command()
	async def latency(self, ctx):

		await ctx.reply(f'{round(self.bot.latency * 1000)}ms', mention_author = True)

	@commands.command()
	async def luckcheck(self, ctx):

		luckResponse = ['Your luck is bad, very bad. Ask blessing from the lord or something idk',
				'Your luck is normal, nothing special',
				'Your luck is very good. i think you will get good score in your test, hopefully...']
		await ctx.send(f'{ctx.author.mention} {random.choice(luckResponse)}')

	@commands.command(aliases = ['outofcontext'])
	async def nocontext(self, ctx):

		im_you = random.randint(0, 101)
		barney = ['bruh',
			'noice',
			'cool :sunglasses:',
			'sh*t (jk)',
			'fury']
		await ctx.send(f'{ctx.author.mention} You are **{im_you}% {random.choice(barney)}**')

	@commands.command()
	async def ask(self, ctx, *, question: str):

		gordon = ['yes',
			'wth no',
			'idk']
		await ctx.reply(f'Q: {question}\nA: {random.choice(gordon)}', mention_author = True)

	@ask.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('Where is the question ?', mention_author = True)

	@commands.command(aliases=['levelrate'])
	async def gdlevelrate(self, ctx, levelID: int):

		rateResponse = ['✩0: Does your level even exist ?',
				'★1 (Auto): You like to make auto level ? weird... but ok',
				'★2 (Easy): I bet its your first time making this level',
				'★3 (Normal): You probably like to play HOW by spu7nix',
				'★4 (Hard): I hope your level get featured mate',
				'★5 (Hard): You like to make a level that make people grinding stars an easy life',
				'★6 (Harder): To the person who like to make this kind of level, i like you. you make my grind less painful',
				'★7 (Harder): Your level is kinda hard, y\'know ?',
				'★8 (Insane): You have annoying gameplay, i swear...',
				'★9 (Insane): Your level is basically failed demon',
				'★10 (Demon): Hope you make it to the weekly demon :)']
		await ctx.reply(f'ID = {levelID}\n\n{random.choice(rateResponse)}', mention_author=True)

	@gdlevelrate.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('where is the level ?', mention_author = True)

		if isinstance(error, commands.BadArgument):
			await ctx.reply('level must be ID to prevent ambiguity', mention_author = True)

	@commands.command()
	async def aboutwhale(self, ctx):

		whale_shits = ['Like all other mammals, whales need to get rid of the waste water they produce. About 166 gallons of urine is excreted by a sei whale in one day. A fin whale\'s daily production of urine amounts to 257 gallons.',
				'Beluga whales have flexible necks, allowing them to move their heads. Their complex communication repertoire of whistles, clicks, and chirps has prompted the nickname "canaries of the sea".',
				'Whales are descended from the Artiodactyl species of dinosaurs, which were land livers.',
				'Gray whales make one of the longest annual migrations of any mammal: they travel about 10,000 miles (16,000 km) round trip!',
				'Located in their massive heads, a sperm whale\'s brain can weigh up to 9kg. That\'s about as heavy as a Dachshund. Not only that, but the rest of the head which makes up about a third of their body is basically a giant container of oil. It\'s this oil that made sperm whales so popular for hunting in the last couple of centuries. You could park a car inside of the chamber filled with oils in their skull. Half this high-value oil is actually called "junk".',
				'**Killer whales eat moose**\nNo, they don\'t jump up onto land and attack the moose. However, orcas have been known to attack moose that are swimming between coastal islands off the northwestern coast of North America. However, this fact is misleading. It\'s not because it\'s false, but it\'s because orcas aren\'t actually whales, they\'re dolphins.',
				'WHALES ARE DIVIDED INTO TWO MAIN GROUPS\nThe baleen whales and the toothed whales. Baleen whales have fibrous "baleen" plates in their mouths instead of teeth which help them filter out huge quantities of krill, plankton, and crustaceans. Toothed whales have teeth which enable them to feed on larger prey such as fish and squid.',
				'Whale "vomit" is used in perfumes.',
				'HUMPBACK WHALES DON’T EAT FOR MOST OF THE YEAR\nHumpback whales in the Southern Hemisphere live off their fat reserves for 5.5-7.5 months each year, as they migrate from their tropical breeding grounds to the Antarctic, to feed on krill.​',
				'ALL TOOTHED WHALES HAVE A "MELON" IN THEIR FOREHEADS\nIts a mass of tissue which focuses the whales calls, vital for communication and echolocation.​ Like bats, they use this echolocation to "see".',
				'SOME WHALES BUBBLE NET FEED\nThis involves whales cooperatively blowing bubbles that encircle their prey. As the prey won\'t cross through the bubbles, they\'re trapped, making it easy for the whales to eat them.',
				'THE NAME "NARWHAL" COMES FROM OLD NORSE\nIt means "corpse whale" as their skin colour resembles that of a drowned sailor.',
				'**Whales are World-Class Divers**\nMany whale species are able to dive to exceptional depths for exceedingly long durations, but none more so than that Cuvier\'s beaked whale, which can dive to depths as deep as 3km and stay there for over 2 hours. They eat a great deal of squid, so diving this deep is necessary in order to catch them.',
				'**Whales are never fully asleep**\nWhen whales sleep, they don\'t fully rest their brains like we humans do. Instead, when they sleep they only rest one half of their brain. The other half remains active in order to maintain their breathing, otherwise they would drown!',
				'This whale fact is brought to you by Spesta. I Have no idea if it is true, it probably isnt (it isnt) but idc.\nHere it is: A whale cock weighs over 10 kilos']
		await ctx.send(f'{random.choice(whale_shits)}\n\nCredit: fat boat#9172')

def setup(bot):

	bot.add_cog(NormalStuff(bot))
