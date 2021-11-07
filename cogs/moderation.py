import discord
from discord.ext import commands
from discord.utils import get

class Moderation(commands.Cog):


	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def selfrole(self, ctx, *, role: str):

		try:
			pain = get(ctx.author.guild.roles, name = role)

			if pain:
				await ctx.author.add_roles(pain)
				await ctx.reply('role successfully added to you', mention_author = True)

			else:
				await ctx.reply('no role found', mention_author = True)

		except discord.Forbidden:
			await ctx.reply("i dont have permissions to give you the role or manage roles permission", mention_author = True)

	@selfrole.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('you forgot to fill the arguments, dont you ?', mention_author = True)

	@commands.command()
	@commands.has_permissions(manage_roles = True)
	async def giverole(self, ctx, member: discord.Member, *, role: str):

		try:
			more_pain = get(member.guild.roles, name = role)

			if more_pain:
				await member.add_roles(more_pain)
				await ctx.reply(f'role successfully added to {member}', mention_author = True)

			else:
				await ctx.reply('role not found. type it correctly', mention_author = True)

		except discord.Forbidden:
			await ctx.reply('i dont have permission to manage roles. also are you trying to give role to someone that is higher than the bot role ?', mention_author = True)

	@giverole.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MemberNotFound):
			await ctx.reply('i cant find a member with that name', mention_author = True)

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('you forgot to fill all the required arguments, dont you ?', mention_author = True)

		if isinstance(error, commands.MissingPermissions):
			await ctx.reply('you dont have permission to manage roles', mention_author = True)

	@commands.command()
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx, member: discord.Member, *, why: str = None):

		try:
			if why == None:
				why = 'being bad'

			await member.kick(reason = why)
			await ctx.reply('{member.name} kicked for {why}', mention_author = True)

		except discord.Forbidden:
			await ctx.reply('i dont have the permission to kick someone. also are you trying to kick someone higher than my role because that is not possible', mention_author = True)

	@kick.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MemberNotFound):
			await ctx.reply('i cant find the member', mention_author = True)

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('fill the required arguments', mention_author = True)

		if isinstance(error, commands.MissingPermissions):
			await ctx.reply('you dont have permission to kick someone', mention_author = True)

	@commands.command()
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx, member: discord.Member, *, this_is_painful: str = None):

		try:
			if this_is_painful == None:
				this_is_painful = 'being bad, *very bad*'

			await member.ban()
			await ctx.reply(f'{member} kicked for {this_is_painful}', mention_author = True)

		except discord.Forbidden:
			await ctx.reply('i dont have permission to ban someone or banning someone higher than the bot', mention_author = True)

	@ban.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MemberNotFound):
			await ctx.reply('i cant find the member', mention_author = True)

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('not enough arguments', mention_author = True)

	@commands.command(aliases = ['purge'])
	@commands.has_permissions(manage_messages = True)
	async def delete(self, ctx, half_life_3: int):

		await ctx.message.delete()
		await ctx.channel.purge(limit = half_life_3)

	@delete.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('limit is not specified', mention_author = True)

		if isinstance(error, commands.BadArgument):
			await ctx.reply('ever see a limit with words ? no ? then use numbers', mention_author = True)

def setup(bot):

	bot.add_cog(Moderation(bot))

