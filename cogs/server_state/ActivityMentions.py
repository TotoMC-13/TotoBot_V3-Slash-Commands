# DISCORD IMPORTS
import discord
from discord.ext import commands, tasks

# ASYNCIO IMPORTS
import asyncio

# OS IMPORTS
import os

# OTHER IMPORTS
import time
from functions.status import get_status


class ActivityMentions(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        self.initialize_loop.start()

    mention_sent = False

    @tasks.loop(seconds=1, count=1)
    async def initialize_loop(self):
        await self.client.wait_until_ready()

        server_1 = os.getenv("SERVER_1")
        channel_id_server_1 = os.getenv("CHANNEL_ID_SERVER_1")

        self.mencion.start(server_1, channel_id_server_1)
        print("Main loop from menciones.py is now ON.")

        
    @tasks.loop(seconds=1800)
    async def mencion(self, server_1: str, channel_id_server_1: str):

        mention_sent = False

        mentions_interval = 1800
        timeout = 1790
        timeout_start = time.time()

        players_number = get_status(server_1, True)

        if players_number and int(players_number) >= int(
            os.getenv("MINIMUM_PLAYERS_FOR_MENTIONS")
        ):
            if mention_sent == False:
                role_id = int(os.getenv("ACTIVITY_ROLE_ID"))
                channel = await self.client.fetch_channel(int(channel_id_server_1))
                em = discord.Embed(
                    title=f"{server_1}",
                    description=f"Hay **{players_number}** jugadores en el servidor. \n¡Animate a entrar!",
                    color=discord.Colour.green(),
                )
                em.add_field(
                    name="\u200b", value=f"Actualizado <t:{round(time.time())}:R>."
                )
                message = await channel.send(f"<@{role_id}>", embed=em)
                mention_sent = True
                await message.delete(delay=mentions_interval)
                while time.time() < timeout_start + timeout:
                    try:
                        await asyncio.sleep(240)
                        players_number = await self.get_status(server_1)
                        em.description = f"Hay **{players_number}** jugadores en el servidor. \n¡Animate a entrar!"
                        em.set_field_at(
                            0,
                            name="\u200b",
                            value=f"Actualizado <t:{round(time.time())}:R>.",
                        )
                        await message.edit(embed=em)
                    except:
                        pass


async def setup(client: commands.Bot) -> None:
    await client.add_cog(ActivityMentions(client), guilds=[discord.Object(770698123915165747), discord.Object(333585269502640138)])
    print("Module ActivityMentions.py was loaded succesfully.")
