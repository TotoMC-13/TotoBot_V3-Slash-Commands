# DISCORD IMPORTS
import discord
from discord import app_commands
from discord.ext import commands
from decorators.is_owner import is_owner

# RANDOM IMPORTS
import random
import asyncio


class shake(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @is_owner()
    @app_commands.command(name="sacudir", description="Mueve al usuario de un chat de voz a otro 5 veces para que reaccione.")
    async def shake(self, interaction: discord.Interaction, user: discord.Member):
        
        if user.voice.channel:
            await interaction.response.send_message(f"Sacudiendo a {user.mention}...", ephemeral=True)

            original_channel = user.voice.channel

            index = 0

            target_channel = random.choice(interaction.guild.voice_channels)

            while user.voice.channel.id == target_channel:
                target_channel = random.choice(interaction.guild.voice_channels)
            else:
                while index < 5:
                    index += 1
                    await user.move_to(target_channel)
                    await asyncio.sleep(0.3)
                    await user.move_to(original_channel)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(
        shake(client),
        guilds=[
            discord.Object(id=770698123915165747),
            discord.Object(id=864993787835056138),
        ],
    )
    print("Module shake.py was loaded succesfully.")
