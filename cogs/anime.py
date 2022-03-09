import re
import discord
import aiohttp
import asyncio
from discord.ext import commands
from bs4 import BeautifulSoup as bs
from discord.commands import slash_command, Option, SlashCommandGroup

# okay, i'll stop using random var names

soup_base = "https://gogoanime.fi"

async def get_req_res(url: str) -> str:

	async with aiohttp.ClientSession() as eat:
		async with eat.get(url) as my_meat:
			if my_meat.status == 200: return await my_meat.text()
			else: return f"fk u, no scraping {my_meat.status}"

class Anime(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	ur_eyes = SlashCommandGroup("anime", "Tools to check and search anime")

	@ur_eyes.command(description="Search anime and get the results")
	async def search(self, ctx, *, query: Option(str, "Keywords to be searched")):

		await ctx.defer()

		good_query = []

		for z in query.split():
			good_query.append(z.strip(" 	\n"))

		pretty = ""
		counter = 0
		keyword = "-".join(good_query)
		print(f'"{keyword}"')
		req_res = await get_req_res(f"{soup_base}/search.html?keyword={keyword}")

		if req_res == '' or req_res == 'fk u. no scraping': return await ctx.respond("An error has occured. try again later")

		to_scrape = bs(req_res, "html.parser")
		raw_res = to_scrape.find("ul", {"class": "items"}).parent.find_all("a")
		raw_release_res = to_scrape.find("ul", {"class": "items"}).parent.find_all("p", {"class": "released"})
		release_sres = []

		for y in raw_release_res:
			release_sres.append(y.string.strip(" 	\n"))

		for x in range(1, len(raw_res), 2):
			counter += 1
			pretty += f"[{counter}] `{raw_res[x].get('href').replace('/category/', '')}` | {release_sres[counter-1].replace('Released: ', '')}\n"

		try:
			await ctx.respond(pretty)

		except discord.errors.HTTPException:
			await ctx.respond("No results found")

	@ur_eyes.command(description="See anime description")
	async def describe(self, ctx, anime_id: str):

		await ctx.defer()

		res = ""
		anime_id = anime_id.strip(" 	\n").replace(" ", "")
		req_res = await get_req_res(f"{soup_base}/category/{anime_id}")
		raw_nav_data = bs(req_res, "html.parser")
		check = raw_nav_data.find("h1")

		if check is None or check.string == "404": return await ctx.respond("No resuts found: 404")

		infos = raw_nav_data.find_all("p", {"class": "type"})

		title = check.string
		type = infos[0].find("a").get("title")
		episode = raw_nav_data.find("ul", {"id": "episode_page"}).find("a").string
		genres = infos[2].find_all("a")
		status = infos[4].find("a").string
		other_names = infos[5].find("span").next_sibling
		synopsis = infos[1].find("span").next_sibling

		res += f"Title: {title}"
		res += f"\nEpisode: {episode.replace('0', '1')}"
		res += f"\nType: {type}\nGenre: "
		for x in genres: res += x.string
		res += f"\nStatus: {status}"
		res += f"\nOther names: {other_names}"
		res += f"\nSynopsis: {synopsis}"

		await ctx.respond(res)

def setup(bot):
	bot.add_cog(Anime(bot))