import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help_command(self, ctx):
        embed = discord.Embed(title="Help", color=discord.Color.blue())
        
        embed.add_field(
            name="Quote",
            value="Use `sam quote @user` to quote a replied message with a profile picture.",
            inline=False
        )

        embed.add_field(name="\u200b", value="\u200b", inline=False)  # Blank field for spacing
        
        embed.add_field(
            name="Albums",
            value="Use `sam albums` to get the top 3 albums with Spotify links.",
            inline=False
        )

        embed.add_field(name="\u200b", value="\u200b", inline=False)  # Blank field for spacing

        embed.add_field(
            name="Reload",
            value="Use `sam reload <cog_name>` to reload a specified cog (admin only).",
            inline=False
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
