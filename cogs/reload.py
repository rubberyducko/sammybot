import discord
from discord.ext import commands

class ReloadCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reload')
    @commands.has_permissions(administrator=True)  # Optional: restrict to admins
    async def reload(self, ctx, *, cog: str):
        """Reloads a cog."""
        try:
            self.bot.unload_extension(f'cogs.{cog}')
            self.bot.load_extension(f'cogs.{cog}')
            await ctx.send(f'Cog **{cog}** has been reloaded successfully.')
        except Exception as e:
            await ctx.send(f'Failed to reload cog **{cog}**. Error: {str(e)}')

async def setup(bot):
    await bot.add_cog(ReloadCog(bot))
