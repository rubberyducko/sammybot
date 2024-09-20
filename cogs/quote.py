import discord
from discord.ext import commands
import io
from PIL import Image, ImageDraw, ImageFont

class QuoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='quote')
    async def quote_command(self, ctx):
        if ctx.message.reference is None:
            await ctx.send("Please reply to a message you want to quote.")
            return

        # Get the replied message
        quoted_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        user = quoted_message.author
        quoted_content = quoted_message.content

        # Create the image for the quote
        profile_picture = user.avatar_url_as(size=128)
        async with self.bot.session.get(str(profile_picture)) as resp:
            if resp.status != 200:
                return await ctx.send('Could not fetch profile picture.')

            image_data = io.BytesIO(await resp.read())

        # Create a blank image with a solid color
        img = Image.new('RGB', (400, 200), (30, 30, 30))
        draw = ImageDraw.Draw(img)

        # Load a font
        font = ImageFont.load_default()
        
        # Draw the profile picture
        profile_pic = Image.open(image_data).resize((64, 64))
        img.paste(profile_pic, (10, 10))

        # Add the quote text
        draw.text((10, 80), f"{user.name}: {quoted_content}", fill="white", font=font)

        # Save the image to a bytes buffer
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Send the image in the chat
        await ctx.send(file=discord.File(buffer, 'quote.png'))

async def setup(bot):
    await bot.add_cog(QuoteCog(bot))
