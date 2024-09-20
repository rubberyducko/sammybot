import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help_command(self, ctx):
        embed = discord.Embed(title="Help", color=discord.Color.blue())

        embed.add_field(
            name="📥 Download TikTok",
            value="Usage: `sam dl <url>`\nDownload TikToks without a watermark.",
            inline=False
        )

        # Add a blank field for spacing
        embed.add_field(name="\u200b", value="\u200b", inline=False)

        embed.add_field(
            name="📝 Quote",
            value="Usage: `sam quote`\nQuote a replied message with the user's profile picture.",
            inline=False
        )

        # Add a blank field for spacing
        embed.add_field(name="\u200b", value="\u200b", inline=False)

        embed.add_field(
            name="📊 Weekly Music",
            value="Usage: `sam weekly albums` or `sam weekly tracks`\nGet the top tracks of the week, optionally by tag.",
            inline=False
        )

        # Add a blank field for spacing
        embed.add_field(name="\u200b", value="\u200b", inline=False)

        embed.add_field(
            name="🔄 Reload Commands",
            value="Usage: `sam reload <cog_name>`\nReload a specific cog.",
            inline=False
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
