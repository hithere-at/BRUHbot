import discord
from discord.ext import commands
import secrets

class security(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases = ['password'])
	async def genpass(self, ctx, school: int):

		candice = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		whos_candice = ''.join(secrets.choice(candice) for _ in range(school))
		await ctx.author.send(f'Here is your password: {whos_candice}')

	@genpass.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('the length of the password ?', mention_author = True)

		if isinstance(error, commands.BadArgument):
			await ctx.reply('specify using numbers only', mention_author = True)

	@commands.command()
	async def encrypt(self, ctx, *, message: str):

		encr_letters = {"a": "^1-",
				"b": "1/^",
				"c": "%5$",
				"d": "@4$",
				"e": "0/@",
				"f": ";$:",
				"g": "=5+",
				"h": "2%4",
				"i": "35;",
				"j": "^&@",
				"k": ":=$",
				"l": "0??",
				"m": "&01",
				"n": "&^1",
				"o": "$=@",
				"p": "3@$",
				"q": "#1%",
				"r": "#8;",
				"s": "@-9",
				"t": "/~7",
				"u": "1$7",
				"v": "673",
				"w": "64$",
				"x": "#^=",
				"y": "&37",
				"z": "?/$",
				" ": "6&_",
				"1": "=98",
				"2": "$$&",
				"3": ";%5",
				"4": "$=^",
				"5": "457",
				"6": "~+$",
				"7": "&@^",
				"8": "80-",
				"9": "179",
				"0": "/84",
				",": "7^%",
				".": ":1%",
				"!": "0~1",
				"@": "^76",
				"#": "977",
				"$": "/$#",
				"%": "~!-",
				"^": "^1!",
				"&": "+^2",
				"*": "7-;",
				"(": "^#?",
				")": "4&$",
				"~": "4~5",
				"[": "^@7",
				"]": "688",
				"-": ":;0",
				"+": "2&!",
				"=": "=4^",
				":": "393",
				";": "538",
				'"': '~?:',
				"'": "^%^",
				"{": "=3^",
				"}": "32#",
				"<": ":58",
				">": ":;&",
				"_": "$08",
				"?": "0$=",
				"/": "/##",
				"	": "7^6"}
		encr_message = []
		message = message.lower()

		for x in message:
			stuff = x.replace(x, encr_letters[x])
			encr_message.append(stuff)

		await ctx.message.delete()
		await ctx.author.send('Latest encrypted message from you:')
		await ctx.author.send(f'`{"".join(encr_message)}`')

	@encrypt.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('Encrypt what ?', mention_author = True)

	@commands.command()
	async def decrypt(self, ctx, message: str):

		decr_letters = {"^1-": "a",
				"1/^": "b",
				"%5$": "c",
				"@4$": "d",
				"0/@": "e",
				";$:": "f",
				"=5+": "g",
				"2%4": "h",
				"35;": "i",
				"^&@": "j",
				":=$": "k",
				"0??": "l",
				"&01": "m",
				"&^1": "n",
				"$=@": "o",
				"3@$": "p",
				"#1%": "q",
				"#8;": "r",
				"@-9": "s",
				"/~7": "t",
				"1$7": "u",
				"673": "v",
				"64$": "w",
				"#^=": "x",
				"&37": "y",
				"?/%": "z",
				"6&_": " ",
				"=98": "1",
				"$$&": "2",
				";%5": "3",
				"$=^": "4",
				"457": "5",
				"~+$": "6",
				"&@^": "7",
				"80-": "8",
				"179": "9",
				"/84": "0",
				"7^%": ",",
				":1%": ".",
				"0~1": "!",
				"^76": "@",
				"977": "#",
				"/$#": "$",
				"~!-": "%",
				"^1!": "^",
				"+^2": "&",
				"7-;": "*",
				"^#?": "(",
				"4&$": ")",
				"4-5": "~",
				"^@7": "[",
				"688": "]",
				":;0": "-",
				"2$!": "+",
				"=4^": "=",
				"393": ":",
				"538": ";",
				'~?:': '"',
				"^%^": "'",
				"=3^": "{",
				"32#": "}",
				":58": "<",
				":;&": ">",
				"$08": "_",
				"0$=": "?",
				"/##": "/",
				"7^6": "	"}
		decr_message = []
		message = message.lower()
		msg_iter = iter(message)

		for y in msg_iter:
			bruh = f'{y + next(msg_iter) + next(msg_iter)}'
			stuff = bruh.replace(bruh, decr_letters[bruh])
			decr_message.append(stuff)

		await ctx.message.delete()
		await ctx.author.send('Latest decrypted message from you:')
		await ctx.author.send(f'`{"".join(decr_message)}`')

	@decrypt.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('Decrypt what ?', mention_author = True)

	@commands.command()
	async def piglatin(self, ctx, *, message: str):

		xdnt = message.split()
		stuff = " ".join(x[1:] + x[0] + 'ay' for x in xdnt)

		await ctx.reply(f'`{stuff}`', mention_author = True)

	@piglatin.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('where is the message ?', mention_author = True)

	@commands.command()
	async def dcpl(self, ctx, *, message: str):

		pognt = message.replace('ay', '').split()
		stuff = ' '.join(x[-1] + x[:-1] for x in pognt)

		await ctx.reply(f'`{stuff}`', mention_author = True)

	@dcpl.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('where is the message ?', mention_author = True)

def setup(bot):

	bot.add_cog(security(bot))
