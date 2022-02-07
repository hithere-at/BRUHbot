import discord
import gd
import os
from discord.ext import commands
from discord.commands import slash_command,	Option
from github import Github
import random # random module for randomizing

git_user = Github(os.getenv("GITHUB_TOKEN"))
gd_client = gd.Client()

class NormalStuff(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@slash_command(description="Say hello to the bot")
	async def sup(self, ctx):

		if ctx.author.id == 668794109020078080: # if the author id is the id of my friend then chose a random respond specified below
			sup_response_motheye = ['moth ? Is that you ? wassup my man',
						'how is life ?',
						'Endless Agony sequel when ?']
			await ctx.respond(random.choice(sup_response_motheye))

		else: # else, just chose a random respond lol
			sup_response = ['yo wassup',
							'shut up lol',
							'uhhh, are you talking to me ?',
							'ok',
							'phishe']
			await ctx.respond(random.choice(sup_response))

	async def get_phishe_list(ctx: discord.AutocompleteContext):
		global phishe_list
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
				'broccoli'
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
				'hotdog',
				'fries',
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
				'salt'] # The discord food emoji list

		return [food for food in phishe_list if food.startswith(ctx.value.lower())]

	@slash_command(description="Ask the bot to give you food")
	async def givefood(self, ctx, *, food: Option(str, "What food?", autocomplete=get_phishe_list)):

		food = food.replace(' ', '_') # replace space with underscore

		if any(phishe in food for phishe in phishe_list): # if any "food" varible is in the discord food emoji list, then respond with the "food" varible
			await ctx.respond(f'Here you go :{food}:')

		else: # else, just say theres nothing
			await ctx.respond('no such food found on discord food emoji list')

	@slash_command(description="Display your profile picture")
	async def pfp(self, ctx, member: Option(discord.Member, "Whose profile picture ?") = None):

		user = member or ctx.author

		pic_embed = discord.Embed(title = '', description = '', color = discord.Color.blue())
		pic_embed.set_image(url = user.avatar.url)
		await ctx.respond(embed=pic_embed)

	@slash_command(description="Check bot latency")
	async def latency(self, ctx):

		await ctx.respond(f'{round(self.bot.latency * 1000)}ms')

	@slash_command(description="Check how lucky you are")
	async def luckcheck(self, ctx):

		luckResponse = ['Your luck is bad, very bad. Ask blessing from the lord or something idk',
						'Your luck is normal, nothing special',
						'Your luck is very good. i think you will get good score in your test, hopefully...']
		await ctx.respond(random.choice(luckResponse))

	@slash_command(description="out of context")
	async def nocontext(self, ctx, *, custom_content: Option(str, "idk how to explain this") = None):

		im_you = random.randint(0, 101) # make a random number

		if custom_content is not None: # self explanatory
			await ctx.respond(f'You are **{im_you}% {custom_content}**')

		else: # else, chose a random content from a list
			barney = ['bruh',
				'noice',
				'cool :sunglasses:',
				'sh*t (jk)',
				'fury']
			await ctx.respond(f'You are **{im_you}% {random.choice(barney)}**')

	@slash_command(description="Ask the bot a question")
	async def ask(self, ctx, *, question: str):

		gordon = ['yes',
			'wth no',
			'maybe',
			'idk']
		await ctx.respond(f'Q: {question}\nA: {random.choice(gordon)}')

	@slash_command(description="Rate your GD level (no this is just a joke)")
	async def gdlevelrate(self, ctx, level_id: Option(int, "Level ID to be rated")):

		try:
			level = await gd_client.get_level(level_id)

		except gd.MissingAccess:
			return await ctx.respond("An error has occured when finding level")

		rate_response = {0: "✩0: You're a shy person",
						1: '★1 (Auto): You like to make auto level ? weird... but ok',
						2: '★2 (Easy): I bet its your first time making this level',
						3: '★3 (Normal): You probably like to play HOW by spu7nix',
						4: '★4 (Hard): I hope your level get featured mate',
						5: '★5 (Hard): You like to make a level that make people grinding stars an easy life',
						6: '★6 (Harder): To the person who like to make this kind of level, i like you. you make my grind less painful',
						7: '★7 (Harder): Your level is kinda hard, y\'know ?',
						8: '★8 (Insane): You have annoying gameplay, i swear...',
						9: '★9 (Insane): Your level is basically failed demon',
						10: '★10 (Demon): Hope you make it to the weekly demon :)'}

		await ctx.respond(f'Level name: **{level.name}**\nLevel creator: **{level.creator}**\nLevel ID: **{level_id}**\n\n{rate_response[level.requested_stars]}')

	@slash_command(description="Give you whale facts")
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
		await ctx.respond(f'{random.choice(whale_shits)}\n\nCredit: fat boat#9172')

	@slash_command(description="Change normal message to spoiler based on the type")
	async def mts(self, ctx, type: Option(str, "Pick the type", choices=["word", "char"]), *, message: str):

		type = type.lower()
		res = ""

		if type == "word": # turn string to spoiler string per word

			for x in message.split():
				res += f'||{x} ||'

		elif type == "char": # its the same as above, but per character

			for x in message:
				res += f'||{x}||'

		else:
				await ctx.respond("Unknown type")
				return

		await ctx.respond(res)

	@slash_command(description="Give developers feedback")
	async def feedback(self, ctx, type: Option(str, "Pick the type", choices=["suggestion", "bug"]), *, content: Option(str, "The content of the feedback")):

		await ctx.defer()

		type = type.lower()

		bot_repo = git_user.get_repo("bestpeople105/BRUHbot")
		bot_repo.create_issue(title=f"{type} from {ctx.author.name}", body=content)
		await ctx.respond("Sent!")

def setup(bot):
	bot.add_cog(NormalStuff(bot))