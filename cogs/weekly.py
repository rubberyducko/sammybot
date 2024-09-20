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
    async def weekly(self, ctx, category: str):
        try:
            # Determine which type of data to fetch
            if category.lower() == 'tracks':
                top_items = self.network.get_top_tracks(limit=5)
                title = "📊 Top Tracks of the Week"
            elif category.lower() == 'artists':
                top_items = self.network.get_top_artists(limit=5)
                title = "📊 Top Artists of the Week"
            else:
                await ctx.send("Please specify a valid category: `tracks` or `artists`.")
                return

            # Create an embed
            embed = discord.Embed(title=title, color=discord.Color.blue())

            for item in top_items:
                playcount = item.item.get_playcount()  # Access the playcount for the item
                if category.lower() == 'tracks':
                    embed.add_field(
                        name=f"🎵 {item.item.title}",
                        value=f"by {item.item.artist.name} | 🎧 {playcount} listens",
                        inline=False
                    )
                elif category.lower() == 'artists':
                    embed.add_field(
                        name=f"🎤 {item.item.name}",
                        value=f"🎧 {playcount} listens",
                        inline=False
                    )
                embed.add_field(name='\u200b', value='\u200b', inline=False)  # Add empty space

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(LastFMCog(bot))
