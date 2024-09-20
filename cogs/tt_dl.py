import discord
from discord.ext import commands
import yt_dlp
import os

class TikTokCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dl(self, ctx, url: str):
        try:
            # Set options for yt-dlp to download without watermark
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'tiktok_video.mp4',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',  # Ensure the output format is MP4
                }],
                'noplaylist': True,  # Ensure it doesn't try to download playlists
            }
            
            # Download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # Send the video as a reply to the user
            await ctx.send(f"{ctx.author.mention}, here is your TikTok video:", file=discord.File("tiktok_video.mp4"))
            os.remove("tiktok_video.mp4")  # Clean up the file after sending

        except Exception as e:
            await ctx.send(f"{ctx.author.mention}, an error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(TikTokCog(bot))
