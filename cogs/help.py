import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class Help(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@slash_command(description="List all the bot commands")
	async def help(self, ctx):

		help_embed = discord.Embed(title='BRUHbot all commands', description="This command will show all BRUHbot commands and what does it do", color=0x14D93B)
		help_embed.set_author(name='BRUHbot', icon_url='https://images-ext-2.discordapp.net/external/0OavdISaaL7vL2nD4sL6VgEz_ow6i42Pdo_jWdHfcYQ/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/745294860839420034/4f4fa33ae47e49a5f7aca65d92bcaf75.webp')
		help_embed.add_field(name='Category: Moderation', value='`ban, kick, purge, selfrole, giverole`',  inline=False)
		help_embed.add_field(name='Category: Security', value='`obfs, deobfs, piglatin, genpass, dcpl`')
		help_embed.add_field(name='Category: Normal Stuff', value='`sup, givefood, pfp, latency, luckcheck, nocontext, ask, gdlevelrate, aboutwhale, mts, feedback`')
		help_embed.add_field(name='Category: Media', value='`smile, mrkrabsbruh, shrimp, dababy, latityintro, thelord, chickennugget, phishe, cat, hampter, kittyreview, cursedimg, fumo`')
		help_embed.add_field(name='Category: amogus (pls dont try this)', value='`sus, kill`')
		help_embed.add_field(name='Category: Economy', value='`daily, balance, quest, share, shop`')
		help_embed.add_field(name='Category: Game', value='`rps, guessnum`')
		help_embed.add_field(name='Category: Music', value='`queue, play, stop, pause, resume, ytsearch`')
		help_embed.set_footer(text='Im sleepy...')
		await ctx.respond(embed=help_embed)

def setup(bot):
	bot.add_cog(Help(bot))