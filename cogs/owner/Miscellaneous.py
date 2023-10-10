# DISCORD IMPORTS
import discord
from discord import app_commands
from discord.ext import commands
import asyncio
from decorators.is_owner import *

# TIME IMPORTS
import time

class Miscellaneous(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
    
    @app_commands.command(name="habla", description="¡ESTA VIVO!")
    @is_owner()
    async def habla(self, interaction: discord.Interaction, channel: discord.TextChannel, message: str):
        await interaction.response.defer(ephemeral=True)
        await channel.send(content=message)
        await interaction.edit_original_response(content=f"Mensaje enviado a {channel.mention}: \nContenido: {message}")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(
        Miscellaneous(client),
        guilds=[
            discord.Object(id=864993787835056138),
            discord.Object(id=770698123915165747),
        ],
    )
    print("Module Miscellaneous.py was loaded succesfully.")
