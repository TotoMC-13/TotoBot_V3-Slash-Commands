# DISCORD IMPORTS
import discord
from discord import app_commands
from discord.ext import commands

# MONGODB IMPORTS
from functions.mongo_functions import add_money, get_balance, subtract_money, get_top


class Economy(commands.GroupCog, name="dinero"):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(
        name="ver",
        description="Muestra el saldo en el banco. Por defecto muestra el saldo de quien use el comando.",
    )
    async def ver(
        self, interaction: discord.Interaction, target_user: discord.Member = None
    ):
        await interaction.response.defer()
        target_user = target_user if target_user else interaction.user

        balance = await get_balance(target_user)

        em = discord.Embed(
            title=f"Cuenta de {target_user}",
            description=f"Fondos disponibles: <:hispasoles:922903735418630174>{balance}",
            color=discord.Colour.gold(),
        )
        em.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/626176190721556481/726555014423904337/logo.png"
        )
        await interaction.edit_original_message(embed=em)

    @app_commands.command(
        name="agregar",
        description="Permite agregar dinero a la cuenta del usuario seleccionado.",
    )
    async def agregar(
        self, interaction: discord.Interaction, target_user: discord.Member, amount: int
    ):
        await interaction.response.defer()
        old_balance = await add_money(target_user, amount)

        em = discord.Embed(
            title="Transacción",
            description=f"**Autor:** {interaction.user.mention}",
            color=discord.Colour.green(),
        )
        em.add_field(
            name=f"**{interaction.guild.name} <:flechas:922902500925927514> {target_user}**",
            value=f"**Monto agregado:** <:hispasoles:922903735418630174>{amount} \n**Saldo:** <:hispasoles:922903735418630174>{old_balance if old_balance else 0} <:flechas:922902500925927514> **Saldo:** <:hispasoles:922903735418630174>{old_balance + amount if old_balance else amount}",
        )
        em.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/626176190721556481/726555014423904337/logo.png"
        )
        await interaction.edit_original_message(embed=em)

    @app_commands.command(
        name="quitar",
        description="Permite quitar dinero de la cuenta del usuario seleccionado.",
    )
    async def quitar(
        self, interaction: discord.Interaction, target_user: discord.Member, amount: int
    ):
        await interaction.response.defer()

        try:
            old_balance = await subtract_money(target_user, amount)

            em = discord.Embed(
                title="Transacción",
                description=f"**Autor:** {interaction.user.mention}",
                color=discord.Colour.green(),
            )
            em.add_field(
                name=f"**{target_user.name} <:flechas:922902500925927514> {interaction.guild.name}**",
                value=f"**Monto quitado:** <:hispasoles:922903735418630174>{amount} \n**Saldo:** <:hispasoles:922903735418630174>{old_balance} <:flechas:922902500925927514> **Saldo:** <:hispasoles:922903735418630174>{old_balance - amount}",
            )
            em.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/626176190721556481/726555014423904337/logo.png"
            )
            await interaction.edit_original_message(embed=em)
        except Exception as e:
            if str(e) == "Not enough funds":
                old_balance = await get_balance(target_user)

                em = discord.Embed(
                    title="ERROR",
                    description="Fondos insuficientes.",
                    color=discord.Colour.red(),
                )
                em.add_field(
                    name=f"**El usuario {target_user.name} no tiene suficientes fondos disponibles en su cuenta.**",
                    value=f"**Saldo actual:** <:hispasoles:922903735418630174>{old_balance} \n**Saldo requerido:** <:hispasoles:922903735418630174>{amount} (Se necesitan <:hispasoles:922903735418630174>{amount - old_balance })",
                )
                em.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/626176190721556481/726555014423904337/logo.png"
                )
                await interaction.edit_original_message(embed=em)
            else:
                raise Exception(e)

    @app_commands.command(
        name="top",
        description="Muestra el top de los 5 usuarios con mas hispasoles en el servidor.",
    )
    async def top(self, interaction: discord.Interaction):
        await interaction.response.defer()

        top = await get_top()

        em = discord.Embed(title=f"Tabla de posiciones: ", description=f"__Top 5 judios de hispania__", color=discord.Colour.gold())
        
        for rank, user in enumerate(top, 1):
            username = await self.client.fetch_user(user["_id"])
            if rank == 1:
                str_rank = "Posición: "
                str_name = "Nombre: "
                str_amount = "Cantidad: "
            else:
                str_rank = "\u200b"
                str_name = "\u200b"
                str_amount = "\u200b"
            
            if rank == 1:
                em.add_field(name=str_rank, value=f"**\n`{rank}`**", inline=True)
                em.add_field(name=str_name, value=f"**\n`{username}`**", inline=True)
                em.add_field(name=str_amount, value=f"**\n<:hispasoles:922903735418630174>`{user['balance']}`**", inline=True)
            else:
                em.add_field(name=str_rank, value=f"**`{rank}`**", inline=True)
                em.add_field(name=str_name, value=f"**`{username}`**", inline=True)
                em.add_field(name=str_amount, value=f"**<:hispasoles:922903735418630174>`{user['balance']}`**", inline=True)
        
        await interaction.edit_original_message(embed=em)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Economy(client), guild=discord.Object(770698123915165747))
    print("Module Economy.py was loaded succesfully.")
