import discord
from discord.ext import commands
import io
import requests
from PIL import Image, ImageDraw, ImageFont

class QuoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def draw_text_with_wrapping(self, draw, text, font, position, max_width):
        """Draws text on an image with word wrapping."""
        lines = []
        words = text.split()
        current_line = ""

        for word in words:
            # Check if adding the new word would exceed the max width
            test_line = f"{current_line} {word}".strip()
            text_length = draw.textlength(test_line, font=font)

            if text_length <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        # Add the last line
        if current_line:
            lines.append(current_line)

        # Draw each line on the image
        y_text = position[1]
        for line in lines:
            draw.text((position[0], y_text), line, fill="white", font=font)
            y_text += font.getbbox(line)[3] - font.getbbox(line)[1]  # Move to the next line using the height of the text

    @commands.command(name='quote')
    async def quote_command(self, ctx):
        if ctx.message.reference is None:
            await ctx.send("Please reply to a message you want to quote.")
            return

        try:
            # Get the replied message
            quoted_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            user = quoted_message.author
            quoted_content = quoted_message.content

            # Fetch the user's avatar
            profile_picture = str(user.avatar)
            response = requests.get(profile_picture)
            if response.status_code != 200:
                return await ctx.send('Could not fetch profile picture.')

            # Create the image for the quote
            img = Image.new('RGB', (600, 128), (30, 30, 30))
            draw = ImageDraw.Draw(img)

            # Load a custom font
            font_path = 'fonts/Cheeky Rabbit.ttf'  # Update this path to your font file
            font = ImageFont.truetype(font_path, 25)  # Adjust size as needed

            # Draw the profile picture
            profile_pic = Image.open(io.BytesIO(response.content)).resize((128, 128))
            img.paste(profile_pic, (0, 0))

            # Add the user name text
            draw.text((135, 10), f"{user.name} said:", fill="white", font=font)

            # Draw the quote text with wrapping
            self.draw_text_with_wrapping(draw, quoted_content, font, (135, 40), 460)  # 460 is the max width for the text

            # Save the image to a bytes buffer
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            # Send the image in the chat
            await ctx.send(file=discord.File(buffer, 'quote.png'))

        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(QuoteCog(bot))
