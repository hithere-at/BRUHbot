import discord
from discord.ext import commands

class Help(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx, cmd: str = None):

		if cmd == None:
			help_embed = discord.Embed(title = 'BRUHbot all commands', description = "This command will show all BRUHbot commands and its functions", color = 0x14D93B)
			help_embed.set_author(name = 'BRUHbot', icon_url = 'https://images-ext-2.discordapp.net/external/0OavdISaaL7vL2nD4sL6VgEz_ow6i42Pdo_jWdHfcYQ/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/745294860839420034/4f4fa33ae47e49a5f7aca65d92bcaf75.webp')
			help_embed.add_field(name = 'Category: Moderation', value = '`ban, kick, delete, selfrole, giverole`',  inline = False)
			help_embed.add_field(name = 'Category: Security', value = '`encrypt, decrypt, piglatin, genpass, dcpl`')
			help_embed.add_field(name = 'Category: Normal Stuff', value = '`sup, givefood, pfp, updatelog, latency, luckcheck, nocontext, ask, gdlevelrate, aboutwhale`')
			help_embed.add_field(name = 'Category: Media', value = '`smile, mrkrabsbruh, shrimp, dababy, latityintro, thelord, chickennugget, phishe, cat, hampter, kittyreview, cursedimg`')
			help_embed.add_field(name = 'Category: amogus (pls dont try this)', value = '`sus, kill`')
			help_embed.add_field(name = 'Category: Economy', value = '`daily, balance, quest`')
			await ctx.reply(embed = help_embed, mention_author = True)

		else:

#Category: Moderation
			if cmd == 'ban':
				await ctx.reply("""
Category: Moderation
Command: `ban`\n
Ban people who dont follow the server rules and being sh*t to someone\n
Usage: `ban <member> <reason>`
**NOTE: Argument <reason> is optional**
""", mention_author = True)

			elif cmd == 'kick':
				await ctx.reply("""
Category: Moderation
Command: `kick`\n
Kick people who dont follow server rules\n
Usage: `kick <member> <reason>`
**NOTE: Argument <reason> is optional**
""", mention_author = True)

			elif cmd == 'delete' or cmd == 'purge':
				await ctx.reply("""
Category: Moderation
Command: `delete`
Aliases = `delete, purge`\n
Delete / purge bulk messages, useful when cleaning leftovers messages from raiders\n
Usage: `any_mentioned_aliases <amount>`
""", mention_author = True)

			elif cmd == 'giverole':
				await ctx.reply("""
Category: Moderation
Command: `giverole`\n
Give specified role to a specified member, useful for moderators\n
Usage: `giverole <member> <role>`
**NOTE: You cannot give role to someone using role ID in order to avoid a bug**
""", mention_author = True)

			elif cmd == 'selfrole':
				await ctx.reply("""
Category: Moderation
Command: `selfrole`\n
Give specified role to yourself\n
Usage: `selfrole <role>`
**NOTE: You cannot give yourself role using role ID in order to avoid a bug**
""", mention_author = True)

#Category: Security
			elif cmd == 'genpass' or cmd == 'password':
				await ctx.reply("""
Category: Security
Command `genpass`
Aliases: `genpass, password`\n
Generate a passowrd for you, Dont worry, we will not log the password :)\n
Usage: `any_mentioned_aliases <password_length>`
""", mention_author = True)

			elif cmd == 'encrypt':
				await ctx.reply("""
Category: Security
Command: `encrypt`\n
Encrypt message using my own encryption
Usage: `encrypt <message>`
**NOTE: DONT USE THIS TO ENCRYPT YOUR SECRET MESSAGE. In fact this is not even an encryption because it doesnt jave public and private key, but i think its still a fun stuff to make**
""", mention_author = True)

			elif cmd == 'decrypt':
				await ctx.reply("""
Category: Security
Command: `decrypt`\n
Decrypt encrypted message that use my encryption\n
Usage: `decrypt <encrypted_message>`
""", mention_author = True)

			elif cmd == 'piglatin':
				await ctx.reply("""
Category: Security
Command: `piglatin`\n
Turn normal message to pig latin\n
Usage: `piglatin <message>`
""", mention_author = True)

			elif cmd == 'dcpl':
				await ctx.reply("""
Category: Security
Command: `dcpl`\n
Turn pig latin message to normal\n
Usage: `dcpl <piglatin_message>`
""", mention_author = True)

#Category: Normal stuff
			elif cmd == 'sup':
				await ctx.reply("""
Category: Normal stuff
Command: `sup`\n
Say hello to @BRUHbot#3034
Usage: `sup`
""", mention_author = True)

			elif cmd == 'givefood':
				await ctx.reply("""
Category: Normal stuff
Command: `givefood`\n
@BRUHbot#3034 will give you food, is it good ? idk\n
Usage: `givefood <food>`
""", mention_author = True)

			elif cmd == 'pfp':
				await ctx.reply("""
Category: Normal stuff
Command: `pfp`\n
Display the specified member profile picture. If member is not specified, your profile picture will be displayed\n
Usage: `pfp <member>`
""", mention_author = True)

			elif cmd == 'latency':
				await ctx.reply("""
Category: Normal stuff
Command: `latency`\n
Display @BRUHbot#3034 ping\n
Usage: `latency`
""", mention_author = True)

			elif cmd == 'luckcheck':
				await ctx.reply("""
Category: Normal stuff
Command: `luckcheck`\n
Check your luck\n
Usage: `luckcheck`
""", mention_author = True)

			elif cmd == 'nocontext' or cmd == 'outofcontext':
				await ctx.reply("""
Category: Normal stuff
Command: `nocontext`
Aliases: `nocontext, outofcontext`\n
I have no idea what this is\n
Usage: `any_mentioned_aliases`
""", mention_author = True)

			elif cmd == 'ask':
				await ctx.reply("""
Category: Normal stuff
Command: `ask`\n
Ask @BRUHbot#3034 a question, idk if the answer make sense tho\n
Usage: `ask <question>`
""", mention_author = True)

			elif cmd == 'gdlevelrate' or cmd == 'levelrate':
				await ctx.reply("""
Category: Normal stuff
Command: `gdlevelrate`
Aliases: `gdlevelrate, levelrate`\n
Rate you Geometry Dash level\n
Usage: `any_mentioned_aliasea <level_id>`
""", mention_author = True)

			elif cmd == 'aboutwhale':
				await ctx.reply("""
Category: Normal stuff
Command: `aboutwhale`\n
Tell you whale facts, very important for school\n
Usage: `aboutwhale`
""", mention_author = True)

#Category: Media
			elif cmd == 'smile':
				await ctx.reply("""
Category: Media
Command: `smile`\n
Give you a smiling doggo gif\n
Usage: `smile`
""", mention_author = True)

			elif cmd == 'mrkrabsbruh':
				await ctx.reply("""
Category: Media
Command: `mrkrabsnruh`\n
Just a gif of mr krabs that i decided to put here\n
Usage: `mrkrabsbruh`
""", mention_author = True)

			elif cmd == 'shrimp' or cmd == 'SHRIIIIIIIIIMP':
				await ctx.reply("""
Category: Media
Command: `shrimp`
Aliases: `shrimp, SHRIIIIIIIIIMP`\n
shrimp\n
Usage: `any_mentioned_aliases`
""", mention_author = True)

			elif cmd == 'dababy':
				await ctx.reply("""
Category: Media
Command: `dababy`\n
Just DaBaby being DaBaby\n
Usage: `dababy`
""", mention_author = True)

			elif cmd == 'latityintro':
				await ctx.reply("""
Category: Media
Command: `latityintro`\n
ElectroBOOM LATITY, my favorite intro of all time\n
Usage: `latityintro`
""", mention_author = True)

			elif cmd == 'thelord' or cmd == 'mindifipraisethelord':
				await ctx.reply("""
Category: Media
Command: `thelord`
Aliases: `thelord, mindifipraisethelord`\n
Mind if i praise te lord ?\n
Usage: `any_mentioned_aliases`
""", mention_author = True)

			elif cmd == 'chickennugget':
				await ctx.reply("""
Category: Media
Command: `chickennugget`\n
Do you like chicken nugget ? because i do :)\n
Usage: `chickennugget`
""", mention_author = True)

			elif cmd == 'phishe':
				await ctx.reply("""
Category: Media
Command: `phishe`\n
This is phishe\n
Usage: `phishe`
""", mention_author = True)

			elif cmd == 'cat':
				await ctx.reply("""
Category: Media
Command: `cat`\n
Some cat gif\n
Usage: `cat`
""", mention_author = True)

			elif cmd == 'hampter':
				await ctx.reply("""
Category: Media
Command: `hampter`\n
Some hampter gif, so cute :3\n
Usage: `hampter`
""", mention_author = True)

			elif cmd == 'kittyreview':
				await ctx.reply("""
Category: Media
Command: `kittyreview`\n
All kitty reviews report is here, take a look\n
Usage: `kittyreview`
""", mention_author = True)

			elif cmd == 'cursedimg':
				await ctx.reply("""
Category: Media
Command: `cursedimg`\n
Very cursed image\n
Usage: `cursedimg`
""", mention_author = True)

#Category: amogus
			elif cmd == 'sus':
				await ctx.reply("""
Category: amogus
Command: `sus`\n
you are sus\n
Usage: `sus`
""", mention_author = True)

			elif cmd == 'kill':
				await ctx.reply("""
Category: amogus
Command: `kill`\n
amogus kill\n
Usage: `kill`
""", mention_author = True)

			elif cmd == 'daily':
				await ctx.reply("""
Category: Currency
Command: `daily`\n
Claim your daily zenny\n
Usage: `daily`
""", mention_author = True)

			elif cmd == 'balance' or cmd == 'bal':
				await ctx.reply("""
Category: Currency
Command: `balance`
Aliases: `balance, bal`\n
Check how much money you have\n
Usage: `any_mentioned_aliases`
""", mention_author = True)

			elif cmd == 'quest':
				await ctx.reply("""
Category: Currency
Commans: `quest`\n
The chief will give you a quest to kill a monster, go complete the quest to earn reward\n
Usage: `quest`
""", mention_author = True)

			else:
				await ctx.reply('No description found for that command', mention_author = True)

def setup(bot):

	bot.add_cog(Help(bot))
