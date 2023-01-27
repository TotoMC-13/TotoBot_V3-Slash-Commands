# DISCORD IMPORTS
import discord
from discord import app_commands
from discord.ext import commands
import asyncio

# TIME IMPORTS
import time

# MC STATUS IMPORTS
from mcstatus import JavaServer


class Minecraft(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(
        name="mc_server", description="Muestra el estado del servidor de minecraft."
    )
    async def mc_server(self, interaction: discord.Interaction):
        await interaction.response.defer()

        server = None
        
        try:
            server = JavaServer.lookup("penesinietro.aternos.me")
            status = server.status()
        except:
            em = discord.Embed(title="Servidor Pene Sinietro", description="Estado del servidor OFFLINE", color=discord.Color.red())
            em.add_field(name="\u200b", value=f"Eliminando <t:{round(time.time() + 30)}:R>")

        if "offline" in status.description:  
            em = discord.Embed(title="Servidor Pene Sinietro", description="Estado del servidor OFFLINE", color=discord.Color.red())
            em.add_field(name="\u200b", value=f"Eliminando <t:{round(time.time() + 30)}:R>")
        elif server:
            status = await server.async_status()

            players_names = [player.name for player in status.players.sample]

            em = discord.Embed(title="Servidor Pene Sinietro", description="Estado del servidor ONLINE", color=discord.Color.green())
            em.add_field(name="Número de jugadores conectados:", value=f"`{status.players.online} jugadores en el servidor`")
            em.add_field(name="Jugadores conectados:", value=f"`{', '.join(players_names)}`")
            em.add_field(name="Latencia:", value=f"`{round(status.latency)} ms`")
            em.add_field(name="\u200b", value=f"Eliminando <t:{round(time.time() + 30)}:R>")
                
        await interaction.edit_original_response(embed=em)
        await asyncio.sleep(30)
        await interaction.delete_original_response()

async def setup(client: commands.Bot) -> None:
    await client.add_cog(
        Minecraft(client),
        guilds=[
            discord.Object(id=864993787835056138),
            discord.Object(id=770698123915165747),
        ],
    )
    print("Module Minecraft.py was loaded succesfully.")
