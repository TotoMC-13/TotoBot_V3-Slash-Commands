# DISCORD IMPORTS
import discord
from discord.ext import commands

# AIOHTTP
import aiohttp

# OS AND PATHLIB IMPORTS
import os
from dotenv import load_dotenv
from pathlib import Path


class client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=".",
            intents=discord.Intents.all(),
            application_id=os.getenv("BOT_ID"),
        )
        self.synced = False
        self.intents.members = True

    async def setup_hook(self) -> None:
        self.session = aiohttp.ClientSession()

        target_dir = Path.cwd() / "cogs"

        for cog in target_dir.rglob("*.py"):
            await self.load_extension(f"cogs.{cog.parent.name}.{cog.stem}")

        await cltree.sync(guild=discord.Object(770698123915165747))
        await cltree.sync(guild=discord.Object(333585269502640138))

        self.synced = True

    async def on_ready(self):
        await self.wait_until_ready()
        print(f"Logged in as {self.user}")


aclient = client()
cltree = aclient.tree

load_dotenv()

if __name__ == "__main__":
    aclient.run(os.getenv("TOKEN"))
