# DISCORD IMPORTS
import discord
from discord import app_commands
from discord.ext import commands

# ASYNCIO IMPORTS
import asyncio

# OS IMPORTS
import os
from dotenv import load_dotenv

# OTHER IMPORTS
import time
import re
from functions.status import get_status


class Status(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="estado", description="Muestra el estado del servidor.")
    async def status(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)

        servers = os.getenv("SERVERS_NAMES").split(",")
        ips_servers = os.getenv("SERVERS_IPS").split(",")

        embed_list = []

        for index, server_name in enumerate(servers):
            print(server_name)
            players_names, players_number, private_number, current_map = get_status(server_name)

            if players_number is None:
                em = discord.Embed(
                    title=f"{server_name}",
                    description="Estado del servidor: OFFLINE",
                    color=discord.Colour.red(),
                )
                em.add_field(
                    name="\u200b", value=f"Eliminando <t:{round(time.time() + 30)}:R>"
                )
                embed_list.append(em)
            else:
                if players_number == 0:
                    em = discord.Embed(
                        title=f"{server_name}",
                        description="Estado del servidor: ONLINE",
                        color=discord.Colour.gold(),
                    )
                    em.add_field(
                        name="Número de jugadores conectados: ",
                        value=f"`{players_number} jugadores en el servidor`",
                    )
                    em.add_field(
                        name="Jugadores conectados: ",
                        value="`No hay jugadores conectados`",
                    )
                    em.add_field(name="Mapa actual: ", value=f"`{current_map}`")
                    em.add_field(name="¡Entra al servidor!", value=f"<{ips_servers[index]}>")
                    em.add_field(
                        name="\u200b",
                        value=f"Eliminando <t:{round(time.time() + 30)}:R>",
                    )
                    embed_list.append(em)
                elif private_number == 0:
                    em = discord.Embed(
                        title=f"{server_name}",
                        description="Estado del servidor: ONLINE",
                        color=discord.Colour.green(),
                    )
                    em.add_field(
                        name=f"Número de jugadores conectados: ",
                        value=f"`{players_number} jugadores en el servidor`",
                    )
                    em.add_field(
                        name=f"Jugadores conectados: ", value=f"`{players_names}`"
                    )
                    em.add_field(name="Mapa actual: ", value=f"`{current_map}`")
                    em.add_field(name="¡Entra al servidor!", value=f"<{ips_servers[index]}>")
                    em.add_field(
                        name="\u200b",
                        value=f"Eliminando <t:{round(time.time() + 30)}:R>",
                    )
                    embed_list.append(em)
                elif len(players_names) == 0:
                    em = discord.Embed(
                        title=f"{server_name}",
                        description="Estado del servidor: ONLINE",
                        color=discord.Colour.green(),
                    )
                    em.add_field(
                        name=f"Número de jugadores conectados:",
                        value=f" `{players_number} jugadores en el servidor`",
                    )
                    em.add_field(
                        name=f"Jugadores conectados: ",
                        value=f"`{private_number} private`",
                    )
                    em.add_field(name="Mapa actual: ", value=f"`{current_map}`")
                    em.add_field(name="¡Entra al servidor!", value=f"<{ips_servers[index]}>")
                    em.add_field(
                        name="\u200b",
                        value=f"Eliminando <t:{round(time.time() + 30)}:R>",
                    )
                    embed_list.append(em)
                else:
                    em = discord.Embed(
                        title=f"{server_name}",
                        description="Estado del servidor: ONLINE",
                        color=discord.Colour.green(),
                    )
                    em.add_field(
                        name=f"Número de jugadores conectados: ",
                        value=f"`{players_number} jugadores en el servidor`",
                    )
                    em.add_field(
                        name=f"Jugadores conectados: ",
                        value=f"`{players_names}, {private_number} private`",
                    )
                    em.add_field(name="Mapa actual: ", value=f"`{current_map}`")
                    em.add_field(name="¡Entra al servidor!", value=f"<{ips_servers[index]}>")
                    em.add_field(
                        name="\u200b",
                        value=f"Eliminando <t:{round(time.time() + 30)}:R>",
                    )
                    embed_list.append(em)
        
        print(embed_list)
        await interaction.edit_original_response(embeds=embed_list)
        await asyncio.sleep(30)
        await interaction.delete_original_response()

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Status(client), guilds=[
            discord.Object(id=770698123915165747),
            discord.Object(id=333585269502640138),
            discord.Object(id=1272666538096332992)
        ],)
    print("Module Status.py was loaded succesfully.")
