# DISCORD IMPORTS
import discord
from discord import app_commands
from discord.ext import commands
import asyncio

# TIME IMPORTS
import time

# ECO STATUS IMPORTS
from functions.eco import *


class EcoStatus(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(
        name="eco", description="Muestra el estado del servidor de Eco."
    )
    async def eco(self, interaction: discord.Interaction):
        await interaction.response.defer()
        
        player_count, day, server_time, meteor_eta = await get_eco_status()

        if not player_count:
            em = discord.Embed(title="Hispania ECO", description="Estado del servidor: OFFLINE", color=discord.Colour.red())
            em.add_field(name="\u200b", value=f"Eliminando <t:{round(time.time() + 30)}:R>")
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/770698123915165750/1096851481174483095/logo.png")
        else:
            em = discord.Embed(title="Hispania ECO", description="Estado del servidor: ONLINE", url="http://209.222.97.90:3001/",color=discord.Colour.blue())
            em.add_field(name="Jugadores online:", value=f"`{player_count}`")
            em.add_field(name="Dia:", value=f"`{day}`")
            em.add_field(name="Hora:", value=f"`{server_time}`")
            em.add_field(name="ETA Impacto Meteorito:", value=f"`{meteor_eta}`")
            em.add_field(name="Información del Servidor:", value=f"[Sitio web](http://209.222.97.90:3001/)")
            em.add_field(name="¡Unete al servidor!:", value=f"<eco://connect/d1c2278f-dd07-47b4-a2f8-543cc62b71a1>")
            em.add_field(name="\u200b", value=f"Eliminando <t:{round(time.time() + 30)}:R>")
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/770698123915165750/1096851481174483095/logo.png")

        await interaction.edit_original_response(embed=em)
        await asyncio.sleep(30)
        await interaction.delete_original_response()

async def setup(client: commands.Bot) -> None:
    await client.add_cog(
        EcoStatus(client),
        guilds=[
            discord.Object(id=770698123915165747),
            discord.Object(id=333585269502640138)
        ],
    )
    print("Module EcoStatus.py was loaded succesfully.")
