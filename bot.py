import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='sam ', intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load_cogs()
    # Replace 'YOUR_DISCORD_BOT_TOKEN' with your bot's token
    await bot.start('YOUR_DISCORD_BOT_TOKEN')

# Run the main function to start the bot
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
