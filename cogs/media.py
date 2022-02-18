import discord
from discord.ext import commands
import random
from discord.commands import slash_command

class media(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@slash_command(description="Doge smile")
	async def smile(self, ctx):

		await ctx.respond('https://tenor.com/view/perro-xd-xd-moises-xd-gif-18316386')

	@slash_command(description="Mr Krab's bruh-ing")
	async def mrkrabsbruh(self, ctx):

		await ctx.respond('https://tenor.com/view/mr-krabs-bruh-cringe-meme-gif-20821912')

	@slash_command(description="shrimp")
	async def shrimp(self, ctx):

		await ctx.respond('https://cdn.discordapp.com/attachments/879172329450643488/879717503784345651/bruh_1.mp4')

	@slash_command(description="lesss gooooooooo")
	async def dababy(self, ctx):

		await ctx.respond('https://tenor.com/view/dababy-lets-go-car-vroom-vroom-gif-21874738')

	@slash_command(description="OK BOOMers")
	async def latityintro(self, ctx):

		await ctx.respond('https://cdn.discordapp.com/attachments/875395171880165398/879641942131097620/ElectroBOOM_LATITY.mp4')

	@slash_command(description="mind if i praise the lord?")
	async def thelord(self, ctx):

		await ctx.respond('https://cdn.discordapp.com/attachments/875395171880165398/879641696432947210/PRAISE_THE_LAWD.mp4')

	@slash_command(description="chicken mcnuggets")
	async def chickennugget(self, ctx):

		await ctx.respond('https://tenor.com/view/chicken-nuggets-pics-art-chicken-chicken-nugget-yeah-gif-16426997')

	@slash_command(description="phishe being phishe")
	async def phishe(self, ctx):

		await ctx.respond('https://cdn.discordapp.com/attachments/875395171880165398/879642028462448650/phishe.mp4')

	@slash_command(description="cat gifs. its cute")
	async def cat(self, ctx):

		cat_stuff = ['https://cdn.discordapp.com/attachments/733869939227624457/876518209342308362/cat.gif',
				'https://tenor.com/view/post-this-cat-instantly-gif-21407907',
				'https://tenor.com/view/cat-dance-cat-dance-gif-20491618',
				'https://tenor.com/view/caracal-big-floppa-flop-fo-gif-18296053',
				'https://cdn.discordapp.com/attachments/880251530723356762/880447528108183572/20210729_103016.jpg']
		await ctx.respond(random.choice(cat_stuff))

	@slash_command(description="cmon, who doesnt love hampter?")
	async def hampter(self, ctx):

		hampter_list = ['https://tenor.com/view/bootythehamster-booty-hamster-syrian-syrian-hamster-gif-20948949',
				'https://tenor.com/view/shummer-hamster-gif-13082806',
				'https://tenor.com/view/hamster-pet-cute-adorable-bff-hamsters-gif-17730896',
				'https://tenor.com/view/hamster-chase-cuddles-gif-4372189']
		await ctx.respond(random.choice(hampter_list))

	@slash_command(description="All kitty review reports goes here (well actually no)")
	async def kittyreview(self, ctx):

		very_cute = ['https://tenor.com/view/kitty-review-kitty-cat-review-gif-20973771',
				'https://tenor.com/view/kitty-review-performance-kittie-cute-gif-21164379',
				'https://tenor.com/view/kitty-review-kitty-ballin-kitty-review-cat-gif-21145619',
				'https://tenor.com/view/kitty-review-kitty-cat-cat-review-squishy-cat-gif-21193166',
				'https://tenor.com/view/kitty-review-cat-kitty-review-stanky-gif-21071465',
				'https://tenor.com/view/kitty-review-cat-kitty-review-gif-20973783',
				'https://tenor.com/view/kitty-review-kitty-cat-cat-review-gif-21193114',
				'https://tenor.com/view/seals-emporium-kitty-review-gif-21748019',
				'https://tenor.com/view/kitty-review-gif-21031795',
				'https://tenor.com/view/kitty-review-cat-kitty-review-gif-20973774',
				'https://tenor.com/view/kitty-gif-21363562',
				'https://tenor.com/view/kitty-review-kitty-review-gif-22462155',
				'https://tenor.com/view/kitty-review-kitty-review-gaming-cat-gif-22352786']
		await ctx.respond(random.choice(very_cute))

	@slash_command(description="Cursed image, yea its kinda cursed")
	async def cursedimg(self, ctx):

		await ctx.respond(file=discord.File(f'./pictures/pic{random.randint(1, 14)}.jpeg'))

	@slash_command(description="fumo's? hell yeah dude")
	async def fumo(self, ctx):

		fumos_boi = ['https://tenor.com/view/touhou-fumo-sakuya-spin-gif-18209352',
				'https://tenor.com/view/touhou-touhou-fumo-fumo-touhou-yuyuko-fumo-gif-23291237',
				'https://tenor.com/view/fumo-reimu-fumo-fumo-fumo-sleep-time-gif-21713443',
				'https://tenor.com/view/fumo-fumofumo-touhou-touhou-fumo-alice-margatroid-gif-20710104',
				'https://tenor.com/view/murder-fumo-frog-touhou-touhou-doll-gif-21576540',
				'https://tenor.com/view/touhou-fumo-flandre-generator-gif-19559237',
				'https://tenor.com/view/touhou-fumo-cirno-jumpscare-gif-22884418',
				'https://tenor.com/view/touhou-cirno-fumo-cirno-fumo-funky-gif-22838318',
				'https://tenor.com/view/hakurei-reimu-fumo-fumo-fumo-fumo-doll-el-transporte-gif-20650216',
				'https://tenor.com/view/touhou-fumo-touhou-fumo-fumo-touhou-aya-gif-23193653',
				'https://tenor.com/view/reimu-fumo-cry-about-it-gif-21782335',
				'https://tenor.com/view/anime-touhou-gif-22815463']

		await ctx.respond(random.choice(fumos_boi))

	@slash_command(description="The skeleton appears")
	async def skeleton(self, ctx):

		skull = ["https://tenor.com/view/fart-memes-i-farted-skeleton-gif-24093226",
				"https://tenor.com/view/the-skeleton-appears-theskeleton-theskeletonappears-gif-24753701",
				"https://tenor.com/view/pablo-escobar-gif-22308826",
				"https://tenor.com/view/skeleton-dancing-skeleton-skeleton-dancing-mental-mental-health-gif-22285576"]

		await ctx.respond(random.choice(skull))

	@slash_command(description="Flavored doorknob testing facility")
	async def doorknob(self, ctx):

		await ctx.respond("https://cdn.discordapp.com/attachments/529475315953696770/876700584227508234/caption.gif")

	@slash_command(description="A man and a TV")
	async def tvmp4(self, ctx):

		await ctx.respond("https://cdn.discordapp.com/attachments/741920768388104272/943121237658435624/TV.mp4")

	@slash_command(description="willi in a bike")
	async def willi(self, ctx):

		await ctx.respond("https://cdn.discordapp.com/attachments/741920768388104272/943121935640977408/willi.mp4")

	@slash_command(description="dudes get bonked in a truck")
	async def truck(self, ctx):

		await ctx.respond("https://cdn.discordapp.com/attachments/741920768388104272/943122194584711189/truck.mp4")

	@slash_command(description="Welcome to EPIC RAP BATTLE HISTORY")
	async def rapbattlehistory(self, ctx):

		await ctx.respond("https://cdn.discordapp.com/attachments/741920768388104272/943122686811459614/EMINEM_VS_IBS.mp4")

	@slash_command(description="Im a gamer")
	async def gamer(self, ctx):

		await ctx.respond("https://cdn.discordapp.com/attachments/741920768388104272/943122992316174356/gamer.jpg")

	@slash_command(description="lagh.mp4")
	async def lagh(self, ctx):

		await ctx.respond("https://cdn.discordapp.com/attachments/741920768388104272/943123134838624286/LAGH.mp4")

	@slash_command(description="Watermelon taste good when you sleep")
	async def watermelon(self, ctx):

		await ctx.respond("https://cdn.discordapp.com/attachments/741920768388104272/943126605679722496/hmmmmm.mp4")

	@slash_command(description="Sauce ?")
	async def sauce(self, ctx):

		await ctx.respond("https://cdn.discordapp.com/attachments/901972458914062457/943037052268716042/video0.mov")

def setup(bot):
	bot.add_cog(media(bot))