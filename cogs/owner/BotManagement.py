# DISCORD IMPORTS
import discord
from discord import app_commands
from discord.ext import commands
from decorators.is_owner import *

# PATHLIB IMPORTS
from pathlib import Path


class BotManagement(commands.GroupCog, name="cogs"):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        self.ignored_cogs = ["owner.BotManagement"]
        super().__init__()

    @is_owner()
    @app_commands.command(name="unload", description="Unloads a cog.")
    async def unload(self, interaction: discord.Interaction, extension: str):
        await interaction.response.defer()

        await self.client.unload_extension(f"cogs.{extension}")
        await self.client.tree.sync(guilds=[
            discord.Object(id=770698123915165747),
            discord.Object(id=333585269502640138)
        ],)
        self.ignored_cogs.append(str(extension))

        embed = discord.Embed(
            title="Unload",
            description=f"{extension} has been unloaded succesfully.",
            color=discord.Color.green(),
        )
        await interaction.edit_original_response(embed=embed)

    @is_owner()
    @app_commands.command(name="load", description="Loads a cog.")
    async def load(self, interaction: discord.Interaction, extension: str):
        await interaction.response.defer()

        print(extension)
        print(self.ignored_cogs[1])
        await self.client.load_extension(f"cogs.{extension}")
        await self.client.tree.sync(guilds=[
            discord.Object(id=770698123915165747),
            discord.Object(id=333585269502640138)
        ],)
        self.ignored_cogs.remove(str(extension))

        embed = discord.Embed(
            title="Load",
            description=f"{extension} has been loaded succesfully.",
            color=discord.Color.green(),
        )
        await interaction.edit_original_response(embed=embed)

    @is_owner()
    @app_commands.command(name="reload", description="Reload the selected cog.")
    async def reload(self, interaction: discord.Interaction, extension: str):
        await interaction.response.defer()

        await self.client.reload_extension(f"cogs.{extension}")
        await self.client.tree.sync(guilds=[
            discord.Object(id=770698123915165747),
            discord.Object(id=333585269502640138)
        ],)

        embed = discord.Embed(
            title="Reload",
            description=f"{extension} was successfully reloaded",
            color=discord.Colour.green(),
        )
        await interaction.edit_original_response(embed=embed)

    @is_owner()
    @app_commands.command(name="reload_all", description="Reloads all cogs.")
    async def reload_all(self, interaction: discord.Interaction):
        await interaction.response.defer()
        cogs = []
        target_dir = Path.cwd() / "cogs"

        for cog in target_dir.rglob("*.py"):
            cog_name = f"cogs.{cog.parent.name}.{cog.stem}"
            if cog_name not in self.ignored_cogs:
                await self.client.reload_extension(cog_name)
                cogs.append(cog_name)

        loaded_cogs = ", ".join(cogs)
        unloaded_cogs = ", ".join(self.ignored_cogs) if self.ignored_cogs else "None"

        embed = discord.Embed(
            title="Reload",
            description="All extensions have been reloaded.",
            color=discord.Colour.green(),
        )
        embed.add_field(name="Loaded: ", value=loaded_cogs, inline=False)
        embed.add_field(name="Ignored: ", value=unloaded_cogs, inline=False)
        await interaction.edit_original_response(embed=embed)

    @app_commands.command(
        name="list", description="Lists all cogs, both loaded and unloaded."
    )
    async def list_all(self, interaction: discord.Interaction):
        await interaction.response.defer()

        unloaded_cogs = []

        embed = discord.Embed(
            title="Reload",
            description=f"All extensions have been reloaded.",
            color=discord.Colour.green(),
        )
        embed.add_field(
            name="Loaded: ",
            value=", ".join([cog[5:] for cog in self.client.extensions]),
            inline=False,
        )

        target_dir = Path.cwd() / "cogs"
        for cog in target_dir.rglob("*.py"):
            if f"cogs.{cog.parent.name}.{cog.stem}" not in self.client.extensions:
                unloaded_cogs.append(f"{cog.parent.name}.{cog.stem}")

        embed.add_field(
            name="Ignored: ",
            value=", ".join(unloaded_cogs) if unloaded_cogs else "All cogs are loaded.",
            inline=False,
        )
        await interaction.edit_original_response(embed=embed)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(
        BotManagement(client),
        guilds=[
            discord.Object(id=333585269502640138),
            discord.Object(id=770698123915165747)
        ],
    )
    print("Module BotManagement.py was loaded succesfully.")
