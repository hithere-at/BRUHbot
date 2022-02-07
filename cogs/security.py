import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import os
import dns.resolver
import pymongo
import secrets

def gen(rep: int, chars: str) -> str:
	res = ""

	for _ in range(rep):
		res += secrets.choice(chars)

	return res

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

client = pymongo.MongoClient(f'{os.getenv("MONGODB_URI")}')
db = client["money"]
stuff = db["zen"]

class security(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@slash_command(description="Generate a new password with specified length")
	async def genpass(self, ctx, length: Option(int, "How long the password will be?")):

		await ctx.author.send(f'Here is your password: {secrets.token_urlsafe(length)}')
		await ctx.respond('Password has been sent') # idk why but slash command need to be ended with "ctx.respond", otherwise it will say interaction failed

	@slash_command(description="Obfuscate a message until its not readable")
	@commands.max_concurrency(1, commands.BucketType.user, wait=True)
	async def obfs(self, ctx, member: Option(discord.Member, "Message for who?"), *, message: Option(str, "The content of the message")):

		await ctx.defer()

		letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`~!@#$%^&*()[]-+=:;\"\'{}<>|_?/,.	 "
		encr = {x: gen(3, "!@#$%^&*;:=+-?/<>") for x in letters}
		key = gen(7, "abcdefghijklmnopqrstuvwxyz1234567890")
		res = [x.replace(x, encr[x]) for x in message]
		user_doc = stuff.count_documents({"_id": str(member.id)})

		if user_doc == 0:
			stuff.insert_one({"_id": str(member.id), "key": key, "en_msg": "".join(res), "de_msg": message, "value": 0})

		else:
			stuff.update_one({"_id": str(member.id)}, {"$set": {"key": key, "en_msg": "".join(res), "de_msg": message}})

		await ctx.author.send("-------------------")
		await ctx.author.send("Obfuscated message:")
		await ctx.author.send(f'`{"".join(res)}`')
		await ctx.author.send("Key:")
		await ctx.author.send(f'`{key}`')
		await ctx.author.send("Send the message and key to someone that you specified when writing the obfs command (optional, but reccomended to send the 2 things)")
		await ctx.respond("Message has been obfuscated")

	async def get_key(ctx: discord.AutocompleteContext):
		user_acc = stuff.find_one({"_id": str(ctx.interaction.user.id)}, limit=1)
		return [user_acc.get("key")]

	@slash_command(description="Deobfuscate message from non-readable to readable message")
	@commands.max_concurrency(1, commands.BucketType.user, wait=True)
	async def deobfs(self, ctx, key: Option(str, "Key", autocomplete=get_key), message: Option(str, "Obfuscated message content")):

		await ctx.defer()

		bruh = []
		counter = 0
		author_cdocs = stuff.count_documents({"_id": str(ctx.author.id)}, limit=1)

		if author_cdocs == 0:
			await ctx.respond("You dont even have your name written in the database")

		author_doc = stuff.find_one({"_id": str(ctx.author.id)}, limit=1)

		try:

			# Check if key and message matched with the argument
			# Key section
			if key == author_doc["key"]:
				bruh.append("Key: Passed")
				counter += 1

			else:
				bruh.append("Key: Failed")

			# Message section (obfuscated)
			if message == author_doc["en_msg"]:
				bruh.append("Mesage: Passed")
				counter += 1

			else:
				bruh.append("Message: Failed")

			# if the program passed all the key and message check
			if counter == 2:

				real_message = author_doc["de_msg"]
				stuff.update_one({"_id": str(ctx.author.id)}, {"$unset": {"en_msg": "", "key": "", "de_msg": ""}})

				await ctx.author.send("-------------------------")
				await ctx.author.send("Latest decrypted message:")
				await ctx.author.send(de_msg)
				await ctx.respond("Message has been deobfuscated")

			# else, say what check that fails
			else:
				await ctx.respond("\n".join(bruh))

		except KeyError:
			await ctx.respond('this message is not for you. go away')

	@slash_command(description="Transfrom normal message to pig latin")
	async def piglatin(self, ctx, *, message: Option(str, "Normal message")):

		xdnt = message.split()
		stuff = " ".join(x[1:] + x[0] + 'ay' for x in xdnt)

		await ctx.respond(f'`{stuff}`')

	@slash_command(description="Transform pig latin message to normal")
	async def dcpl(self, ctx, *, message: Option(str, "Pig latin message")):

		pognt = message.replace('ay', '').split()
		stuff = ' '.join(x[-1] + x[:-1] for x in pognt)

		await ctx.respond(f'`{stuff}`')

def setup(bot):

	bot.add_cog(security(bot))
