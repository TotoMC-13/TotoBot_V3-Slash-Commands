#DISCORD IMPORTS
import discord
from discord.ext import commands, tasks

#ASYNCIO IMPORTS
import asyncio

#OS IMPORTS
import os
from dotenv import load_dotenv

#OTHER IMPORTS
import time
from functions.status import get_status

class menciones(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        self.mencion.start()

    @tasks.loop(minutes=30)
    async def mencion(self):
        await self.client.wait_until_ready()
        print("Main loop from menciones.py is now ON.")
        
        server_1 = os.getenv("SERVER_1")
        channel_id_server_1 = os.getenv("CHANNEL_ID_SERVER_1")

        timeout = 1790
        timeout_start = time.time()

        players_number = get_status(server_1, True)

        if int(players_number) >= 5:
            channel = await self.client.fetch_channel(int(channel_id_server_1))
            em = discord.Embed(title=f"{server_1}", description=f"Hay **{players_number}** jugadores en el servidor. \n¡Animate a entrar!", color = discord.Colour.green())
            em.add_field(name="\u200b", value=f"Actualizado <t:{round(time.time())}:R>.")
            message = await channel.send("<@394138910508449792>", embed = em)
            await message.delete(delay=1800)
            while time.time() < timeout_start + timeout:
                try:
                    await asyncio.sleep(240)
                    players_number = await self.get_status(server_1)
                    em.description = f"Hay **{players_number}** jugadores en el servidor. \n¡Animate a entrar!"
                    em.set_field_at(0, name="\u200b", value=f"Actualizado <t:{round(time.time())}:R>.")
                    await message.edit(embed = em)
                    print("ACTUALIZADO PICHÓN")
                except:
                    pass

async def setup(client: commands.Bot) -> None:
    await client.add_cog(
        menciones(client)
    )
    print("Module menciones.py was loaded succesfully.")
