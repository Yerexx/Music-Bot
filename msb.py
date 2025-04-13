import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import discord.opus

from token_config import BOT_TOKEN

if not discord.opus.is_loaded():
    print("Opus is not loaded. Attempting to load...")
    discord.opus.load_opus('/opt/homebrew/lib/libopus.dylib')  
    if discord.opus.is_loaded():
        print("Opus loaded successfully!")
    else:
        print("Failed to load Opus.")


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


voice_clients = {}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def start(ctx, channel_id: int):
    channel = bot.get_channel(channel_id)
    if channel and isinstance(channel, discord.VoiceChannel):
        voice_client = await channel.connect()
        voice_clients[ctx.guild.id] = voice_client
        await ctx.send(f"Joined {channel.name} and ready to play music!")
    else:
        await ctx.send("Invalid channel ID or the channel is not a voice channel.")

@bot.command()
async def play(ctx, url: str):
    guild_id = ctx.guild.id
    if guild_id in voice_clients:
        voice_client = voice_clients[guild_id]
        
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['url']
            voice_client.play(discord.FFmpegPCMAudio(url2))
        await ctx.send(f"Now playing: {info['title']}")
    else:
        await ctx.send("Bot is not connected to a voice channel. Use !start first.")

@bot.command()
async def volume(ctx, volume: int):
    guild_id = ctx.guild.id
    if guild_id in voice_clients:
        voice_client = voice_clients[guild_id]
        if 0 <= volume <= 100:
            voice_client.source.volume = volume / 100
            await ctx.send(f"Volume set to {volume}%.")
        else:
            await ctx.send("Volume must be between 0 and 100.")
    else:
        await ctx.send("Bot is not connected to a voice channel. Use !start first.")


if __name__ == '__main__':
    bot.run(BOT_TOKEN)