import discord
from discord.ext import commands
import pylast

class LastFMCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = "752487533e48433c1d7c47f4f2f06d2d"  # Replace with your Last.fm API key
        self.api_secret = "21570ca711d59e3cb803b956f6baf4eb"  # Replace with your Last.fm API secret
        self.network = pylast.LastFMNetwork(api_key=self.api_key, api_secret=self.api_secret)

    @commands.command(name='weekly')
    async def weekly(self, ctx):
        try:
            # Fetch the weekly chart list
            chart = self.network.get_weekly_chart_list()

            # Prepare the response
            response = "📊 **Weekly Chart List**:\n\n"
            for track in chart[:10]:  # Get top 10 tracks
                response += f"🎵 {track.title} by {track.artist}\n"

            await ctx.send(response)

        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(LastFMCog(bot))
