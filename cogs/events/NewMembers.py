# DISCORD
import discord
from discord.ext import commands


class NewMembers(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 333585269502640138:
            channel = self.client.get_channel(333585269502640138)
            em = discord.Embed(
                title=f"Hola {member}!",
                description=f"Bienvenido/a a la **Comunidad Hispania**",
                color=discord.Colour.red(),
            )
            em.add_field(
                name=f"Cosas que te recomendamos hacer:",
                value=f"""
                \n\n ➭ Pasate por <#528252827672510495> para saber las normas basicas del servidor. 
                \n\n ➭ En caso de que vengas a buscar alguna mesa o anunciar la propia, tu canal es <#1160344156435120189>.""",
            )
            em.add_field(
                name=f"Acerca de SS13:",
                value=f"""
                \n\n ➭ Si te interesa nuestro servidor de SS13, el canal es <#333588005824757762>.
                \n\n ➭ Si tienes dudas pasa por <#408667066867122176> o pregunta en <#408664655725330432>. 
                \n\n ➭ Utiliza </estado:1138994163740839990> para ver los jugadores conectados. 
                \n\nEnlaces útiles: [Nuestra wiki](http://hispaniastation.net/)""",
                inline=False
                )
            em.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/626176190721556481/726555014423904337/logo.png"
            )
            em.set_image(
                url="https://cdn.discordapp.com/attachments/528284892417753089/852926541746798592/follaojos.png"
            )
            await channel.send(member.mention, embed=em)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 333585269502640138:
            channel = self.client.get_channel(333585269502640138)
            member_count = len(member.guild.members)
            em = discord.Embed(
                title=f"{member} abandonó el servidor.",
                description=f"""Usuarios en el servidor: `{member_count}`""",
                color=discord.Colour.red(),
            )
            await channel.send(embed=em)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(NewMembers(client), guilds=[
            discord.Object(id=770698123915165747),
            discord.Object(id=333585269502640138)
        ],)
    print(f"Module NewMembers.py was loaded succesfully.")