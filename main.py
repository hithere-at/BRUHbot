import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name='my commands "/"'))

def bestPeople(ctx):
	return ctx.author.id == 812570189182533642

@bot.event
async def on_ready():
	print('Online!')

@bot.slash_command(guild_ids=[900247064439574589, 937910852684763146])
@commands.check(bestPeople)
async def open(ctx, files):

	bot.load_extension(f'cogs.{files}')

@bot.slash_command(guild_ids=[900247064439574589, 937910852684763146])
@commands.check(bestPeople)
async def close(ctx, files):

	bot.unload_extension(f'cogs.{files}')

@bot.slash_command(guild_ids=[900247064439574589, 937910852684763146])
@commands.check(bestPeople)
async def reload(ctx, files):

	bot.reload_extension(f'cogs.{files}')

@bot.slash_command(guild_ids=[900247064439574589, 937910852684763146])
@commands.check(bestPeople)
async def changestatus(ctx, bot_status, *, reason):

	if bot_status == 'idle':
		await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.listening, name = f'{reason}'))

	elif bot_status == 'online':
		await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.listening, name = f'{reason}'))

	elif bot_status == 'dnd':
		await bot.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.listening, name = f'{reason}'))

@bot.slash_command(guild_ids=[900247064439574589, 937910852684763146])
@commands.check(bestPeople)
async def test(ctx):
		await ctx.respond("Hello")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f'cogs.{filename[:-3]}')
		print(filename, "loaded")

bot.run(f'{os.getenv("BOT_TOKEN")}')
