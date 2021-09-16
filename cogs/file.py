import discord
import random
import os
import psutil
import asyncio
import secrets
from discord.utils import get
from discord.ext import commands

class Moderation(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_message(self, message):
		
		msg_content = message.content.lower().replace(' ','').replace('$','s').replace('1', 'i').replace('!', 'i').replace('#','h').replace('7','t').replace('@','a').replace('0','o').replace('9','g').replace('4','a').replace('8','h').replace('¦','i')
		badWord = ['fuck','shit','dumbass','dick','penis','tities','motherfuck','stfu','bitch','asshole','cock','bollocks','nigga','mothafuck','fack','fak','niger','nigger','niga','titties','titie','tittie','pussy','pusy','mothefuck','motharfuck','retard','tard','cunt','nigge','nige']
		
		if any(word in msg_content for word in badWord):
			await message.delete()
		
		for file in message.attachments:
			if file.filename.endswith(('.exe','.apk','.zip','.rar','.7z','.tar.gz','.vb','.scr')):
				await message.delete()
	
	@commands.command()
	async def selfrole(self, ctx, roleName):
	
		user = ctx.author
		role = get(user.guild.roles, name=f'{roleName}')
		await user.add_roles(role)
		
	@selfrole.error
	async def on_command_error(self, ctx, error):
		
		if isinstance(error, commands.RoleNotFound):
			await ctx.reply('nope. i cant find the role you looking for', mention_author=True)
	
	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def giverole(self, ctx, roleName, user: discord.Member):
		
		role = get(user.guild.roles, name=f'{roleName}')
		await user.add_roles(role)
	
	@giverole.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MemberNotFound):
			await ctx.reply('I cant find the user with that name', mention_author=True)
			
		if isinstance(error, commands.RoleNotFound):
			await ctx.reply('I cant find the role', mention_author=True)
		
	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, user: discord.Member, *, reason):
		
		await user.kick(reason=reason)
	
	@kick.error
	async def on_command_error(self, ctx, error):
		
		if isinstance(error, commands.MemberNotFound):
			await ctx.reply('I cant find the user', mention_author=True)
	
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, user: discord.Member, *, reason):
	
		await user.ban(reason=reason)
		
	@ban.error
	async def on_command_error(self, ctx, error):
		
		if isinstance(error, commands.MemberNotFound):
			await ctx.reply('yeaaaaaaa, i cant find the user', mention_author=True)
	
class SayHello(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def sup(self, ctx):
	
		supRpns = ['yo wassup','shut up lol','uhhh, are you talking to me ?','ok']
		await ctx.reply(random.choice(supRpns), mention_author=True)

	@commands.command(hidden=True)
	async def hello(self, ctx):
	
		if ctx.author.id == 668794109020078080:
		
			supRpnsToUser = ["Moth ? Is that you ? wassup my man","How's life ?","Endless Agony when ?"]		
			await ctx.reply(random.choice(supRpnsToUser), mention_author=True)

class UpdateLog(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(aliases=['updatelogall'])
	async def updatelog(self, ctx):
			
		await ctx.reply('1.0.0= This first release comes with 7 commands. Commands can be found by typing :help\n\n1.1.0 = This updates comes with 3 new commands and :latityintro command patch, it was not working due to typing error. New commands can be found by typing :help\n\n1.1.1 = Added forbidden command\n\n1.1.2 = Minor optimization for forbidden command\n\n1.2.0 = Added 3 new commands and deleted some unnecessary junk. New commands can be found by typing :help\n\n1.3.0 = Added 1 forbidden command and 2 new command. This update also comes with reply system, so now bot can reply in order to eliminate any confusion. New commands can be found by typing :help\n\n1.3.1 = Added a simple error handling of "No command found", major optimization for forbidden command, and patches for some commands\n\n1.4.0 = Code is now written in discord.py rewrite branch, so the bot have full coverage of the Discord API, added error handling for some command and 3 new commands. Commands can be found by typing :help\n\n1.5.0 = Added 3 new command, swear word filter, and attachments filter. Commands can be found by typing :help\n\n1.6.0 = Code is now using "cog", so everytime there is a bug, the dev doesnt need to turn off the bot :). Added 1 new commands, which is role giver. Added patch for some commands. Improved swear word filter. New commands can be found by typing :help', mention_author=True)

class ServerStatus(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()		
	async def latency(self, ctx):
		
		await ctx.send(f'{round(self.bot.latency * 1000)}ms')
		
	@commands.command()
	async def stats(self, ctx):
	
		cpuUsage, cpuFrequency, memoryUsed, totalCPUCores = round(psutil.cpu_percent(0.1) / 10), round(psutil.cpu_freq().current), round(psutil.virtual_memory().used / 1000000), os.cpu_count()
	
		await ctx.reply(f'Total CPU cores: {totalCPUCores} cores\nCPU usage: {cpuUsage}%\nCurrent CPU frequency: {cpuFrequency}MHz\nMemory used: {memoryUsed}MB')
	
class VidandGif(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def smile(self, ctx):
	
		await ctx.reply('https://tenor.com/view/perro-xd-xd-moises-xd-gif-18316386', mention_author=True)

	@commands.command()
	async def mrkrabsbruh(self, ctx):
	
		await ctx.reply('https://tenor.com/view/mr-krabs-bruh-cringe-meme-gif-20821912', mention_author=True)

	@commands.command()
	async def SHRIIIIIIIIIMP(self, ctx):
			
		await ctx.reply('https://cdn.discordapp.com/attachments/879172329450643488/879717503784345651/bruh_1.mp4', mention_author=True)

	@commands.command()
	async def dababy(self, ctx):
	
		await ctx.reply('https://tenor.com/view/dababy-lets-go-car-vroom-vroom-gif-21874738', mention_author=True)

	@commands.command()
	async def latityintro(self, ctx):
	
		await ctx.reply('https://cdn.discordapp.com/attachments/875395171880165398/879641942131097620/ElectroBOOM_LATITY.mp4', mention_author=True)

	@commands.command()
	async def mindifipraisethelord(self, ctx):
	
		await ctx.reply('https://cdn.discordapp.com/attachments/875395171880165398/879641696432947210/PRAISE_THE_LAWD.mp4', mention_author=True)
	
	@commands.command()
	async def chickennugget(self, ctx):
	
		await ctx.reply('https://tenor.com/view/chicken-nuggets-pics-art-chicken-chicken-nugget-yeah-gif-16426997', mention_author=True)
	
	@commands.command()
	async def phishe(self, ctx):
	
		await ctx.reply('https://cdn.discordapp.com/attachments/875395171880165398/879642028462448650/phishe.mp4', mention_author=True)
	
class ForbiddenCommands(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(hidden=True, aliases=['73&rhd8djdiieiedn'])
	async def ForbiddenCommand1(self, ctx):
	
		loopStuff = 0
		while loopStuff < 5:
			loopStuff += 1
			await ctx.author.send('im watching you')
			await asyncio.sleep(1)
			
	@commands.command(hidden=True, aliases=['dontdoit'])
	async def ForbiddenCommand2(self, ctx):
		
		await ctx.reply('https://tenor.com/view/smiley-3d-vibe-check-creepy-gif-15669762', mention_author=True)

class GiveFood(commands.Cog):
	
	def __init__(self, bot):
			self.bot = bot
	
	@commands.command()
	async def givefood(self, ctx, *, food):
	
		foodList = ['hamburger','pizza','bacon','bread','doughnut','candy','chocolate_bar','ice_cream','rice','rice_ball','green_apple','apple','pear','tangerine','lemon','banana','watermelon','grapes','blueberries','strawberry','melon','cherries','mango','peach','pineapple','tomato','coconut','eggplant','kiwi','avocado','olive','broccoli','leafy_green','bell_pepper','cucumber','hot_pepper','corn','carrot','french_bread','bagel','garlic','onion','croissant','potato','sweet_potato','flatbread','pretzel','cheese','egg','cooking','butter','pancakes','waffle','cut_of_meat','poultry_leg','meat_on_bone','hotdog','fries','sandwich','stuffed_flatbread','falafel','taco','burrito','tamale','salad','shallow_pan_of_food','fondue','canned_food','spaghetti','ramen','stew','curry','sushi','bento','dumpling','oyster','fried_shrimp','rice_cracker','fish_cake','fortune_cookie','moon_cake','oden','dango','shaved_ice','icecream','pie','cupcake','cake','custard','lollipop','popcorn','cookie','chestnut','peanuts','honey_pot','milk','baby_bottle','coffee','tea','teapot','mate','bubble_tea','beverage_box','cup_with_straw','sake','beer','beers','champagne_glass','wine_glass','tumbler_glass','cocktail','tropical_drink','champagne','ice_cube','spoon','fork_and_knife','fork_knife_plate','bowl_with_spoon','takeout_box','chopsticks','salt']
	
		if any(word in food for word in foodList):
			await ctx.reply(f'Here you go :{food}:', mention_author=True)
		
		else:
			await ctx.reply('no such food found', mention_author=True)
	
	@givefood.error
	async def on_command_error(self, ctx, error):
		
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('give what', mention_author=True)
			
class RNGstuff(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def cat(self, ctx):
		
		catStuffs = ['https://cdn.discordapp.com/attachments/733869939227624457/876518209342308362/cat.gif','https://tenor.com/view/post-this-cat-instantly-gif-21407907','https://tenor.com/view/cat-dance-cat-dance-gif-20491618','https://tenor.com/view/caracal-big-floppa-flop-fo-gif-18296053','https://cdn.discordapp.com/attachments/880251530723356762/880447528108183572/20210729_103016.jpg']
	
		await ctx.reply(random.choice(catStuffs), mention_author=True)
	
	@commands.command()
	async def kittyreview(self, ctx):
	
		catReviewGifs = ['https://tenor.com/view/kitty-review-kitty-cat-review-gif-20973771','https://tenor.com/view/kitty-review-performance-kittie-cute-gif-21164379','https://tenor.com/view/kitty-review-kitty-ballin-kitty-review-cat-gif-21145619','https://tenor.com/view/kitty-review-kitty-cat-cat-review-squishy-cat-gif-21193166','https://tenor.com/view/kitty-review-cat-kitty-review-stanky-gif-21071465','https://tenor.com/view/kitty-review-cat-kitty-review-gif-20973783','https://tenor.com/view/kitty-review-kitty-cat-cat-review-gif-21193114','https://tenor.com/view/seals-emporium-kitty-review-gif-21748019','https://tenor.com/view/kitty-review-gif-21031795','https://tenor.com/view/kitty-review-cat-kitty-review-gif-20973774','https://tenor.com/view/kitty-gif-21363562','https://tenor.com/view/kitty-review-kitty-review-gif-22462155','https://tenor.com/view/kitty-review-kitty-review-gaming-cat-gif-22352786']
	
		await ctx.reply(random.choice(catReviewGifs), mention_author=True)
	
	@commands.command(aliases=['levelrate'])
	async def GDlevelrate(self, ctx, levelID):
	
		rateResponse = ['✩0: Does your level even exist ?','★1 (Auto): You like to make auto level ? weird... but ok','★2 (Easy): I bet its your first time making this level','★3 (Normal): You probably like to play HOW ny spu7nix','★4 (Hard): I hope your level get featured mate','★5 (Hard): You like to make a level that make people grinding stars an easy life','★6 (Harder): To the person who like to make this kind of level, i like you. you make my grind less painful',"★7 (Harder): Your level is kinda hard, y'know ?",'★8 (Insane): You have annoying gameplay, i swear...','★9 (Insane): Your level is basically failed demon','★10 (Demon): Hope you make it to the weekly demon :)']
	
		await ctx.reply(f'ID = {levelID}\n\n{random.choice(rateResponse)}', mention_author=True)
	
	@GDlevelrate.error
	async def on_command_error(self, ctx, error):
	
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('where is the level ?', mention_author=True)
	
	@commands.command()
	async def luckcheck(self, ctx):
	
		luckResponse = ['Your luck is bad, very bad. Ask blessing from the lord or something idk','Your luck is normal, nothing special','Your luck is very good. i think you will get good score in your test, hopefully...']
	
		await ctx.send(ctx.author.mention, random.choice(luckResponse))

class stuff(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def ask(self, ctx, *, question):
	
		questionResponse = ['very yes','wth no','idk']
	
		await ctx.reply(f'Q: {question}\nA: {random.choice(questionResponse)}', mention_author=True)
	
	@ask.error
	async def on_command_error(ctx, error):
	
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('where is the question ?', mention_author=True)

	@commands.command()
	async def outofcontext(self, ctx):
	
		bruhNumber = random.randint(0, 101)
		aList = ['% bruh','% noice','% cool :sunglasses:','% sh*t (jk)','% fury']
	
		await ctx.send(f'{ctx.author.mention} You are **{bruhNumber}% {random.choice(aList)}**')
		
	@commands.command()
	async def spicypic(self, ctx):
		
		await ctx.send(file = discord.File('./SPOILER_spicy pic.jpg'))

class amogus(commands.Cog):
	
	def __init__(self, bot):
			self.bot = bot			
	
	@commands.command()
	async def sus(self, ctx):
	
		await ctx.reply('https://tenor.com/view/sus-gif-20302681')

	@commands.command()
	async def kill(self, ctx):
	
		await ctx.reply('https://tenor.com/view/among-us-kill-gif-19295404')			

	@commands.command()
	async def pfp(self, ctx, user: discord.Member):
		
		picEmbed = discord.Embed(title = '', description = '', color = discord.Color.blue())
		picEmbed.set_image(url = user.avatar_url)
		
		await ctx.send(embed = picEmbed)
		
		if user == None:
		
			picEmbed.set_image(url = ctx.author.avatar_url)
		
			await ctx.send(embed = picEmbed)

class ProbablyUseful(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def password(self, ctx, TempPassLength):
	
		passLength = int(TempPassLength)
		letterList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
		realPassword = ''.join(secrets.choice(letterList) for i in range(passLength))
		
		await ctx.author.send(f'Here is your password: {realPassword}')
	
def setup(bot):
	bot.add_cog(SayHello(bot))
	bot.add_cog(Moderation(bot))
	bot.add_cog(UpdateLog(bot))
	bot.add_cog(ServerStatus(bot))
	bot.add_cog(ForbiddenCommands(bot))
	bot.add_cog(RNGstuff(bot))
	bot.add_cog(amogus(bot))
	bot.add_cog(ProbablyUseful(bot))
	bot.add_cog(GiveFood(bot))
	bot.add_cog(VidandGif(bot))
	bot.add_cog(stuff(bot))
