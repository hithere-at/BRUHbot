import discord
import secrets
import os
import asyncio
from yt_dlp import YoutubeDL as ytdl
from youtube_search import YoutubeSearch as ytsearch
from discord.ext import commands
from discord.commands import slash_command, Option, SlashCommandGroup

ffm_opts = {"options": "-vn -ab 128k"}

async def get_ytdl_inf(ytdl_opts: dict, content: str) -> dict:
	kaede_best_girl = asyncio.get_running_loop()
	return await kaede_best_girl.run_in_executor(None, lambda: ytdl(ytdl_opts).extract_info(f'ytsearch:{content}', download=True))

async def get_ytsearch_res(query: str, max: int) -> list:
	baby_eren = asyncio.get_running_loop()
	return await baby_eren.run_in_executor(None, lambda: ytsearch(query, max_results=max).to_dict())

async def play_music(ctx, sauce: str):
	player = discord.FFmpegPCMAudio(source=sauce, **ffm_opts)
	ctx.guild.voice_client.play(player)

class Controller(discord.ui.View):

	def __init__(self):
			super().__init__(timeout=None)

	async def wait_until_finished(self, msg: str, src_file: str, inter: discord.Interaction):
		hanagaki = False
		takemichi = inter.guild.voice_client

		while hanagaki == False:
			await asyncio.sleep(1.25)
			if takemichi.is_playing() or takemichi.is_paused(): continue

			if not takemichi.is_playing():
				await self.fuck_interaction()
				os.remove(src_file)
				await inter.edit_original_message(content=msg, view=self)
				hanagaki = True

	async def fuck_interaction(self):

		for gonna_kill in self.children:
			gonna_kill.disabled = True
			gonna_kill.style = discord.ButtonStyle.grey

	@discord.ui.button(label="Stop", style=discord.ButtonStyle.red, custom_id="persistent_view:red")
	async def stop(self, button: discord.ui.Button, inter: discord.Interaction):

		if inter.guild.voice_client.is_playing():
			inter.guild.voice_client.stop()
			await self.fuck_interaction()
			await inter.response.edit_message(view=self)

	@discord.ui.button(label="Pause", style=discord.ButtonStyle.green, custom_id="persistent_view:green")
	async def pause_resume(self, button: discord.ui.Button, inter: discord.Interaction):

		if inter.guild.voice_client.is_playing():
			inter.guild.voice_client.pause()
			button.label = "Resume"
			return await inter.response.edit_message(view=self)

		elif inter.guild.voice_client.is_paused():
			inter.guild.voice_client.resume()
			button.label = "Pause"
			await inter.response.edit_message(view=self)

class Music(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@slash_command(description="Bot join channel")
	async def join(self, ctx):

		await ctx.defer()

		if ctx.author.voice is None: return await ctx.respond("You're not in a voice channel ._.")

		await ctx.respond("Joining")
		channel = ctx.author.voice.channel
		await channel.connect()
		await ctx.interaction.edit_original_message(content="Joined")

	@slash_command(description="Bot leave channel")
	async def leave(self, ctx):

		if ctx.author.voice is None: return await ctx.respond("You're not in a voice channel...")

		vcclient = ctx.guild.voice_client
		await vcclient.disconnect()
		await ctx.respond("Left")

	@slash_command(description="Play song with the specified url or query")
	async def play(self, ctx, *, content: Option(str, "Content of the URL or query")):

		await ctx.defer()

		what_a_mess = secrets.token_urlsafe(10)
		rengoku_died_lol = f"song/{what_a_mess}"

		if ctx.author.voice is None: return await ctx.respond("You're not in a voice channel ._.")

		vc = ctx.guild.voice_client

		if vc not in self.bot.voice_clients: return await ctx.respond("im not in your voice channel")

		if not vc.is_playing():
			ytdl_opts = {"format": "m4a", "noplaylist": True, "outtmpl": f"{rengoku_died_lol}-%(id)s.%(ext)s"}
			beware = await get_ytdl_inf(ytdl_opts, content)
			haha_eren_go = f"{rengoku_died_lol}-{beware['entries'][0]['id']}.m4a"
			rumbling_rumbling = beware["entries"][0]["title"]

			await play_music(ctx, haha_eren_go)

		else:
			return await ctx.respond("Already playing song")

		the_paths = Controller()

		await ctx.respond(f"Now playing **{rumbling_rumbling}**", view=the_paths)
		await the_paths.wait_until_finished(f"Finished playing **{rumbling_rumbling}**", haha_eren_go, ctx.interaction)

	@slash_command(description="Search video on YouTube and get the URL")
	async def ytsearch(self, ctx, max_result: Option(int, "Max result of the search result"), *, query: Option(str, "Keywords to be search")):

		await ctx.defer()

		zenitsu_op = f"Query: {query}\n\n"
		rumbling_ep_five = await get_ytsearch_res(query, max_result)

		for kamado, tanjiro in enumerate(rumbling_ep_five, 1):
			zenitsu_op += f"Index {kamado}:\nTitle: **{tanjiro['title']}**\nURL: <https://youtu.be/{tanjiro['id']}>\nChannel: **{tanjiro['channel']}**\n\n"

		await ctx.respond(zenitsu_op)

def setup(bot):
	bot.add_cog(Music(bot))
