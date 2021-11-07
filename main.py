import os
import discord
import a
import requests
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix = '%', help_command = None, status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.listening, name = 'my commands "%"'))

def bestPeople(ctx):
	return ctx.author.id == 812570189182533642

@bot.event
async def on_ready():

	reload_cogs.start()
	print('Online!')

@bot.event
async def on_command_error(ctx, error):

	if isinstance(error, commands.CommandNotFound):
		await ctx.reply('Bro. wth are you trying to type ? Also the prefix is "%"', mention_author=True)

@bot.command(hidden=True)
@commands.check(bestPeople)
async def open(ctx, files):

	bot.load_extension(f'cogs.{files}')

@bot.command(hidden=True)
@commands.check(bestPeople)
async def close(ctx, files):

	bot.unload_extension(f'cogs.{files}')

@bot.command(hidden=True)
@commands.check(bestPeople)
async def reload(ctx, files):

	bot.reload_extension(f'cogs.{files}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(seconds = 60)
async def reload_cogs():

	cog_list = ['media', 'help', 'moderation', 'normal_stuff', 'security', 'top_secret']

	for x in cog_list:
		bot.reload_extension(f'cogs.{x}')

@bot.command(hidden=True)
@commands.check(bestPeople)
async def changestatus(ctx, botStatus, *, reason):

	if botStatus == 'idle':
		await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.listening, name = f'{reason}'))

	if botStatus == 'online':
		await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.listening, name = f'{reason}'))

	if botStatus == 'dnd':
		await bot.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.listening, name = f'{reason}'))

a.keep_alive()
bot.run(f'{os.getenv("BOT_TOKEN")}')
