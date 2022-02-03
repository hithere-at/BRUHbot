import discord
from discord.ext import commands
from discord.utils import get
from discord.commands import slash_command, Option

class Moderation(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@slash_command(description="Give yourself a role")
	async def selfrole(self, ctx, *, role_name: Option(str, "The name of the role")):

		try:
			pain = get(ctx.author.guild.roles, name=role_name)

			if pain:
				await ctx.author.add_roles(pain)
				await ctx.respond('role successfully added to you')

			else:
				await ctx.respond('no such role found')

		except discord.Forbidden:
			await ctx.respond("i dont have permissions to give you the role or manage roles permission")

	@slash_command(description="Give someone a role")
	@commands.has_permissions(manage_roles=True)
	async def giverole(self, ctx, member: Option(discord.Member, "Who?"), *, role_name: Option(str, "The name of the role")):

		try:
			more_pain = get(member.guild.roles, name=role_name)

			if more_pain:
				await member.add_roles(more_pain)
				await ctx.respond(f'role successfully added to {member}')

			else:
				await ctx.respond('role not found. type it correctly')

		except discord.Forbidden:
			await ctx.respond('i dont have permission to manage roles. also are you trying to give role to someone that is higher than the bot role ?')

	@giverole.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingPermissions):
			await ctx.respond('you dont have permission to manage roles')

	@slash_command(description="Kick a bad member")
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: Option(discord.Member, "Who?"), *, reason: Option(str, "Why?") = None):

		why = reason or "being bad"

		try:
			await member.kick(reason=why)
			await ctx.respond('{member.name} kicked for {reason}')

		except discord.Forbidden:
			await ctx.respond('i dont have the permission to kick someone. also are you trying to kick someone higher than my role because that is not possible')

	@kick.error
	async def on_command_error(self, ctx, error):

		if isinstance(error, commands.MissingPermissions):
			await ctx.respond('you dont have permission to kick someone')

	@slash_command(description="Ban a very bad member")
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: Option(discord.Member, "Who?"), *, reason: Option(str, "Why?") = None):

		try:
			why = reason or "being bad, *very bad*"

			await member.ban()
			await ctx.respond(f'{member.name} kicked for {why}')

		except discord.Forbidden:
			await ctx.respond('i dont have permission to ban someone or banning someone higher than the bot')

	@slash_command(description="Purge message with specified amount")
	@commands.has_permissions(manage_messages=True)
	async def purge(self, ctx, amount: Option(int, "How many messages?")):

		await ctx.channel.purge(limit=amount)
		await ctx.respond("Purge successful", ephemeral=True)

def setup(bot):

	bot.add_cog(Moderation(bot))