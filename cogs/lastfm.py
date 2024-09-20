import discord
from discord.ext import commands
import pylast

class LastFmCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.network = pylast.LastFMNetwork(api_key='752487533e48433c1d7c47f4f2f06d2d', api_secret='21570ca711d59e3cb803b956f6baf4eb')

    @commands.command(name='toptracks')
    async def top_tracks(self, ctx, *, artist_name: str):
        # Specify the channel ID where the command is allowed
        allowed_channel_id = 1169841725024522311  # Replace with your channel ID

        if ctx.channel.id != allowed_channel_id:
            await ctx.send("This command can only be used in a specific channel.")
            return

        
        try:
            artist = self.network.get_artist(artist_name)
            top_tracks = artist.get_top_tracks(limit=3)

            embed = discord.Embed(
                title=f"Top Tracks for {artist_name}",
                color=discord.Color.blue()
            )

            for track in top_tracks:
                embed.add_field(
                    name=track.item.title,
                    value=f"Listen [here]({track.item.get_url()})",  # Use get_url() method
                    inline=False
                )

            await ctx.send(embed=embed)

        except pylast.WSError as e:
            await ctx.send("Error connecting to Last.fm API.")
            print(f"Last.fm API error: {e}")

        except Exception as e:
            await ctx.send("An error occurred while fetching data.")
            print(f"General error: {str(e)}")

async def setup(bot):
    await bot.add_cog(LastFmCog(bot))
