import discord
import requests
import os
from discord.ext import commands

# Bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Load Keyword.io API Key
KEYWORD_IO_API_KEY = "your_keyword_io_api_key"

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command(name="keywords")
async def fetch_keywords(ctx, *, query: str):
    """Fetch keywords for a given query."""
    await ctx.send(f"🔍 Searching for keywords related to: `{query}`...")
    url = f"https://api.keyword.io/v1/keywords?query={query}&apiKey={KEYWORD_IO_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        keywords = data.get("keywords", [])
        if keywords:
            keyword_list = "\n".join([f"- {k['keyword']} (Volume: {k['volume']})" for k in keywords[:10]])
            await ctx.send(f"📈 **Top Keywords for `{query}`**:\n{keyword_list}")
        else:
            await ctx.send("⚠️ No keywords found. Try a different query.")
    else:
        await ctx.send("❌ Error fetching keywords. Please try again later.")

@bot.command(name="seo")
async def seo_tips(ctx):
    """Provide general SEO tips."""
    tips = (
        "📌 **SEO Tips for Better Rankings**:\n"
        "1. Use long-tail keywords for better targeting.\n"
        "2. Ensure your content answers user intent.\n"
        "3. Optimize your meta titles and descriptions.\n"
        "4. Include keywords in your headings (H1, H2, etc.).\n"
        "5. Use internal and external links wisely.\n"
        "6. Maintain a high content readability score."
    )
    await ctx.send(tips)

# Run the bot
bot.run("your_discord_bot_token")
