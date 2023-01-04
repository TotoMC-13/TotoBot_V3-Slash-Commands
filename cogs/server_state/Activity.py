# DISCORD IMPORTS
import discord
from discord import app_commands
from discord.ext import commands

# ASYNCIO IMPORTS
import asyncio

# TIME IMPORTS
import time

# WEB SCRAPING IMPORTS
import urllib.request
from urllib.error import HTTPError
import ssl

# MONGODB IMPORTS
from functions.mongo_functions import edit_skullnet_urls, get_skullnet_url


class Activity(commands.GroupCog, name="actividad"):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    ssl._create_default_https_context = ssl._create_unverified_context

    @app_commands.command(
        name="diaria",
        description="Permite ver un grafico con la actividad diaria del servidor.",
    )
    async def actividad_diaria(self, interaction: discord.Interaction):
        await interaction.response.defer()

        ss13_url = await get_skullnet_url(interaction=interaction)

        if not ss13_url:
            await interaction.edit_original_response(
                content="Es necesario configurar el URL antes de utilizar este comando. Para configurarlo utiliza el comando `/actividad editar_url`, para mas información sobre como hacerlo utiliza `/actividad ayuda_url`. Por favor utiliza `/actividad ayuda_url`"
            )
            return

        try:
            await asyncio.to_thread(urllib.request.urlretrieve, ss13_url + "/daily", "grafico.jpg")
        except HTTPError:
            await interaction.edit_original_response(
                content="Hubo un problerma al intentar obtener los gráficos, es probable que el enlace de la configuración ya no sea válido o el sitio web no funcione. Por favor utiliza `/actividad ayuda_url`"
            )
            return

        file = discord.File("./grafico.jpg")

        em = discord.Embed(
            title="[ES]Hispania - Paracode",
            description="Jugadores en el servidor en las últimas 24hs",
            color=discord.Colour.red(),
        )
        em.add_field(name="\u200b", value=f"Eliminando <t:{round(time.time() + 30)}:R>")
        em.set_image(url="attachment://grafico.jpg")

        await interaction.edit_original_response(attachments=[file], embed=em)
        await asyncio.sleep(30)
        await interaction.delete_original_response()

    @app_commands.command(
        name="semanal",
        description="Permite ver un grafico con la actividad semanal del servidor.",
    )
    async def actividad_semanal(self, interaction: discord.Interaction):
        await interaction.response.defer()

        ss13_url = await get_skullnet_url(interaction=interaction)

        if not ss13_url:
            await interaction.edit_original_response(
                content="Es necesario configurar el URL antes de utilizar este comando. Para configurarlo utiliza el comando `/actividad editar_url`, para mas información sobre como hacerlo utiliza `/actividad ayuda_url`."
            )
            return

        try:
            await asyncio.to_thread(urllib.request.urlretrieve, ss13_url + "/weekly", "grafico.jpg")
        except HTTPError:
            await interaction.edit_original_response(
                content="Hubo un problerma al intentar obtener los gráficos, es probable que el enlace de la configuración ya no sea válido o el sitio web no funcione."
            )
            return

        file = discord.File("./grafico.jpg")

        em = discord.Embed(
            title="[ES]Hispania - Paracode",
            description="Jugadores en el servidor en los últimos 7 días.",
            color=discord.Colour.red(),
        )
        em.add_field(name="\u200b", value=f"Eliminando <t:{round(time.time() + 30)}:R>")
        em.set_image(url="attachment://grafico.jpg")

        await interaction.edit_original_response(attachments=[file], embed=em)
        await asyncio.sleep(30)
        await interaction.delete_original_response()

    @app_commands.command(
        name="editar_url",
        description="Permite editar la url de la cual el bot obtiene el gráfico.",
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def editar_url_grafico(self, interaction: discord.Interaction, url: str):
        await interaction.response.defer()

        if not url.startswith("https://ss13stats.skullnet.me/"):
            await interaction.edit_original_response(
                content="El enlace ingresado no parece ser correcto, debe ser un enlace proveniente de https://ss13stats.skullnet.me/. \n\nPara obtener el URL del gráfico ingresa a https://ss13stats.skullnet.me/, busca el servidor correspondiente, dale click para acceder a los gráficos y copia el URL. \n\nPara ver este mensaje nuevamente utiliza el comando `/actividad ayuda_url`"
            )
            return

        await edit_skullnet_urls(interaction=interaction, skullnet_url=url)

        await interaction.edit_original_response(content="URL configurado exitosamente.")

    @app_commands.command(
        name="ayuda_url",
        description="Cómo obtener el url del los gráficos.",
    )
    async def ayuda_url(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Para obtener el URL del gráfico ingresa a https://ss13stats.skullnet.me/, busca el servidor correspondiente, dale click para acceder a los gráficos y copia el URL. Luego edita la configuración con el comando `/actividad editar_url`"
        )


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Activity(client), guild=discord.Object(333585269502640138))
    print("Module Activity.py was loaded succesfully.")
