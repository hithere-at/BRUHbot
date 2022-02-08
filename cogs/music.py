import discord
import os
import asyncio
from yt_dlp import YoutubeDL as ytdl
from youtube_search import YoutubeSearch as ytsearch
from discord.ext import commands
from discord.commands import slash_command, Option, SlashCommandGroup

ffm_opts = {"options": "-vn -ab 128k"}
server_queue = {}

async def play_next_queue(ctx):

	try:
		del(server_queue[ctx.guild.id][0])

		if len(server_queue[ctx.guild.id]) >= 1:
			await play_music(ctx, True, server_queue[ctx.guild.id][0])

	except IndexError:
		await ctx.respond("Queue has been burned")

async def get_ytdl_inf(ytdl_opts: dict, content: str) -> dict:
	komi_best_girl = asyncio.get_running_loop()
	return await komi_best_girl.run_in_executor(None, lambda: ytdl(ytdl_opts).extract_info(f'ytsearch:{content}', download=True))

async def get_ytsearch_res(query: str, max: int) -> list:
	baby_eren = asyncio.get_running_loop()
	return await baby_eren.run_in_executor(None, lambda: ytsearch(query, max_results=max).to_dict())

async def play_music(ctx, from_queue: bool, inf: list):

	player = discord.FFmpegPCMAudio(source=inf[0], **ffm_opts)

	if from_queue is True:
		gonna_burn_to_ashes = asyncio.get_running_loop()
		ctx.guild.voice_client.play(player, after=lambda x: asyncio.run_coroutine_threadsafe(play_next_queue(ctx), gonna_burn_to_ashes))
		await ctx.respond(f"Now playing **{inf[1]}** from your queue")

	elif from_queue is False:
		ctx.guild.voice_client.play(player)
		await ctx.respond(f"Now playing **{inf[1]}**")

	os.remove(inf[0])

class Music(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	queue_stuff = SlashCommandGroup("queue", "Queueing System")

	@slash_command(description="Bot join channel")
	async def join(self, ctx):

		await ctx.defer()

		if ctx.author.voice is None: return await ctx.respond("You're not in a voice channel ._.")

		channel = ctx.author.voice.channel
		await channel.connect()
		await ctx.respond("Joined")

	@slash_command(description="Bot leave channel")
	async def leave(self, ctx):

		if ctx.author.voice is None: return await ctx.respond("You're not in a voice channel...")

		vcclient = ctx.guild.voice_client
		await vcclient.disconnect()
		await ctx.respond("Left")

	@queue_stuff.command(description="Add song to the queue")
	async def add(self, ctx, *, content: Option(str, "Contebt to be added")):

		await ctx.defer()

		rengoku_died_lol = f"song/{ctx.guild.id}-{ctx.author.id}"
		ytdl_opts = {"format": "bestaudio/best", "noplaylist": True, "outtmpl": f"{rengoku_died_lol}-%(id)s.%(ext)s", "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "opus", "preferredquality": "128"}]}

		if server_queue.get(ctx.guild.id) is None:
			server_queue[ctx.guild.id] = []

		junk = await get_ytdl_inf(ytdl_opts, content)
		hinokami = f"{rengoku_died_lol}-{junk['entries'][0]['id']}.m4a"
		kagura = junk["entries"][0]["title"]

		server_queue[ctx.guild.id].append([hinokami, kagura])

		if "https://" or "http://" in content:
			await ctx.respond(f"Song added to server queue\nQuery: **<{content}>**")

		else:
			await ctx.respond(f"Song added to server queue\nQuery: **{content}**")

	@queue_stuff.command(description="Remove song on the queue with specifed index")
	async def remove(self, ctx, index: Option(int, "The index of the queue to be removed")):

		if server_queue.get(ctx.guild.id) is None:
			await ctx.respond("this server doesnt have any queue")

		if index == 0:
			await ctx.respond("Index cannot be 0")

		if len(server_queue[ctx.guild.id]) < 1:
			await ctx.respond("the queue is empty lol")

		else:
			await ctx.respond(f"Index {index} has been deleted\nSong title: **{server_queue[ctx.guild.id][index-1][1]}**")
			del(server_queue[ctx.guild.id][index-1])

	@queue_stuff.command(description="Wipe out all queued songs")
	async def clear(self, ctx):

		if len(server_queue[ctx.guild.id]) < 1:
			return await ctx.respond("this server doesnt even have a queue")

		server_queue[ctx.guild.id].clear()
		await ctx.respond("This server queue has been cleared")

	@queue_stuff.command(description="View all queued songs")
	async def view(self, ctx):

		pretty = ""

		if server_queue.get(ctx.guild.id) is None:
			return await ctx.respond("stop. there is no queue")

		if len(server_queue[ctx.guild.id]) == 0:
			await ctx.respond("Nothing to see, because your queue is empty")

		else:

			for idx, val in enumerate(server_queue[ctx.guild.id], 1):

				if "https://" in val[1]:
					pretty += f"Index {idx}: <{val[1]}>\n"

				else:
					pretty += f"Index {idx}: **{val[1]}**\n"

			await ctx.respond(pretty)

	@queue_stuff.command(description="Play song fron the queue")
	async def play(self, ctx):

		if server_queue.get(ctx.guild.id) is None:
			return await ctx.respond("theres no queue hence no song to be played")

		await ctx.defer()

		if ctx.author.voice is None: return await ctx.respond("You're not in a voice channel ._.")

		vc = ctx.guild.voice_client

		if vc not in self.bot.voice_clients: return await ctx.respond("im not in your voice channel")

		if not vc.is_playing():
			await play_music(ctx, True, server_queue[ctx.guild.id][0])

		else:
			await ctx.respond("Already playing song")

	@slash_command(description="Play song with the specified url or query")
	async def play(self, ctx, *, content: Option(str, "Content of the URL or query")):

		await ctx.defer()

		rengoku_died_lol = f"song/{ctx.guild.id}-{ctx.author.id}"

		if ctx.author.voice is None: return await ctx.respond("You're not in a voice channel ._.")

		vc = ctx.guild.voice_client

		if vc not in self.bot.voice_clients: return await ctx.respond("im not in your voice channel")

		if not vc.is_playing():
			ytdl_opts = {"format": "m4a", "noplaylist": True, "outtmpl": f"{rengoku_died_lol}-%(id)s.%(ext)s"}
			# ytdl_opts = {"format": "bestaudio/best", "noplaylist": True, "outtmpl": f"{rengoku_died_lol}-%(id)s.%(ext)s", "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "opus", "preferredquality": "128"}]}
			beware = await get_ytdl_inf(ytdl_opts, content)
			haha_eren_go = f"{rengoku_died_lol}-{beware['entries'][0]['id']}.m4a"
			rumbling_rumbling = beware["entries"][0]["title"]
			await play_music(ctx, False, [haha_eren_go, rumbling_rumbling])

		else:
			await ctx.respond("Already playing song")

	@slash_command(description="Search video on YouTube and get the URL")
	async def ytsearch(self, ctx, max_result: Option(int, "Max result of the search result"), *, query: Option(str, "Keywords to be search")):

		await ctx.defer()

		zenitsu_op = f"Query: {query}\n\n"
		rumbling_ep_five = await get_ytsearch_res(query, max_result)

		for kamado, tanjiro in enumerate(rumbling_ep_five, 1):
			zenitsu_op += f"Index {kamado}:\nTitle: **{tanjiro['title']}**\nURL: <https://youtu.be/{tanjiro['id']}>\nChannel: **{tanjiro['channel']}**\n\n"

		await ctx.respond(zenitsu_op)

	@slash_command(description="Pause song")
	async def pause(self, ctx):

		if ctx.author.voice is None: return await ctx.respond("You're not in a voice channel ._.")

		vc = ctx.guild.voice_client

		if vc not in self.bot.voice_clients: return await ("im not in your voice channel")

		if vc.is_playing():
			vc.pause()
			await ctx.respond("Paused")

		else:
			await ctx.respond("Pausing what? There is no song playing right now xd")

	@slash_command(description="Stop playing current song (also works with queue by skipping)")
	async def stop(self, ctx):

		if ctx.author.voice is None: return await ctx.respond("You're not in a voice channel ._.")

		vc = ctx.guild.voice_client

		if vc not in self.bot.voice_clients: return await ("im not in your voice channel")

		if vc.is_playing():
			vc.stop()
			await ctx.respond("Stopped")

		else:
			await ctx.respond("There is no song to be stopped")

	@slash_command(description="Resume/unpause paused song")
	async def resume(self, ctx):

		if ctx.author.voice is None: return await ctx.respond("You're not in a voice channel ._.")

		vc = ctx.guild.voice_client

		if vc not in self.bot.voice_clients: return await ("im not in your voice channel")

		if vc.is_paused():
			vc.resume()
			await ctx.respond("Resumed")

		else:
			await ctx.respond("There is no song playing or the song isnt paused")

def setup(bot):
	bot.add_cog(Music(bot))
