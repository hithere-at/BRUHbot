import discord
from discord.ext import commands
import random

class media(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def smile(self, ctx):

		await ctx.reply('https://tenor.com/view/perro-xd-xd-moises-xd-gif-18316386', mention_author = True)

	@commands.command()
	async def mrkrabsbruh(self, ctx):

		await ctx.reply('https://tenor.com/view/mr-krabs-bruh-cringe-meme-gif-20821912', mention_author = True)

	@commands.command(aliases = ['SHRIIIIIIIIIMP'])
	async def shrimp(self, ctx):

		await ctx.reply('https://cdn.discordapp.com/attachments/879172329450643488/879717503784345651/bruh_1.mp4', mention_author = True)

	@commands.command()
	async def dababy(self, ctx):

		await ctx.reply('https://tenor.com/view/dababy-lets-go-car-vroom-vroom-gif-21874738', mention_author = True)

	@commands.command()
	async def latityintro(self, ctx):

		await ctx.reply('https://cdn.discordapp.com/attachments/875395171880165398/879641942131097620/ElectroBOOM_LATITY.mp4', mention_author = True)

	@commands.command(aliases = ['mindifipraisethelord'])
	async def thelord(self, ctx):

		await ctx.reply('https://cdn.discordapp.com/attachments/875395171880165398/879641696432947210/PRAISE_THE_LAWD.mp4', mention_author = True)

	@commands.command()
	async def chickennugget(self, ctx):

		await ctx.reply('https://tenor.com/view/chicken-nuggets-pics-art-chicken-chicken-nugget-yeah-gif-16426997', mention_author=True)

	@commands.command()
	async def phishe(self, ctx):

		await ctx.reply('https://cdn.discordapp.com/attachments/875395171880165398/879642028462448650/phishe.mp4', mention_author=True)

	@commands.command()
	async def cat(self, ctx):

		cat_stuff = ['https://cdn.discordapp.com/attachments/733869939227624457/876518209342308362/cat.gif',
				'https://tenor.com/view/post-this-cat-instantly-gif-21407907',
				'https://tenor.com/view/cat-dance-cat-dance-gif-20491618',
				'https://tenor.com/view/caracal-big-floppa-flop-fo-gif-18296053',
				'https://cdn.discordapp.com/attachments/880251530723356762/880447528108183572/20210729_103016.jpg']
		await ctx.reply(random.choice(cat_stuff), mention_author = True)

	@commands.command()
	async def hampter(self, ctx):

		hampter_list = ['https://tenor.com/view/bootythehamster-booty-hamster-syrian-syrian-hamster-gif-20948949',
				'https://tenor.com/view/shummer-hamster-gif-13082806',
				'https://tenor.com/view/hamster-pet-cute-adorable-bff-hamsters-gif-17730896',
				'https://tenor.com/view/hamster-chase-cuddles-gif-4372189']
		await ctx.reply(random.choice(hampter_list), mention_author = True)

	@commands.command()
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
		await ctx.reply(random.choice(very_cute), mention_author = True)

	@commands.command()
	async def cursedimg(self, ctx):

		crsdimg_lst = ['pic1', 'pic2', 'pic3', 'pic4', 'pic5', 'pic6', 'pic7', 'pic8', 'pic9', 'pic10', 'pic11', 'pic12']
		await ctx.reply(file = discord.File(f'./pictures/{random.choice(crsdimg_lst)}.jpeg'), mention_author=True)

def setup(bot):

	bot.add_cog(media(bot))
