#DISCORD
import discord
from discord.ext import commands

class bienvenidas(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()    
    async def on_member_join(self, member):
        if member.guild.id == 333585269502640138:
            channel = self.client.get_channel(333585269502640138)
            em = discord.Embed(title=f"Hola {member}!", 
            description=f"Bienvenido/a a la **Comunidad Hispania de SS13**", 
            color=discord.Colour.red())
            em.add_field(name=f"Cosas que te recomendamos hacer:", 
            value=f"""
                \n\n ➭ Pasate por <#528252827672510495> para saber las normas basicas del servidor. 
                \n\n ➭ En <#795535799088971786> podras asignarte los roles que quieras. 
                \n\n ➭ Si tienes alguna pregunta no dudes en pasar por <#408667066867122176> o pregunta en <#408664655725330432>. 
                \n\nEnlaces útiles: [Nuestra wiki](http://hispaniastation.net/)""")
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/626176190721556481/726555014423904337/logo.png")
            em.set_image(url="https://cdn.discordapp.com/attachments/528284892417753089/852926541746798592/follaojos.png")
            await channel.send(embed = em)
            await channel.send(member.mention)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 333585269502640138:
            channel = self.client.get_channel(333585269502640138)
            member_count = len(member.guild.members)
            em = discord.Embed(title=f"{member} abandonó el servidor.", 
            description=f"""Usuarios en el servidor: `{member_count}`""", 
            color=discord.Colour.red())
            await channel.send(embed = em)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(
        bienvenidas(client)
    )
    print(f"Module bienvenidas.py was loaded succesfully.")