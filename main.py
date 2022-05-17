#DISCORD IMPORTS
import discord
from discord.ext import commands

#AIOHTTP
import aiohttp

#OS AND PATHLIB IMPORTS
import os
from dotenv import load_dotenv
from pathlib import Path

class client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='.',
            intents = discord.Intents.default(),
            application_id = 772489968823828490)
        self.synced = False
        self.intents.members = True
    
    async def setup_hook(self) -> None:
        self.session = aiohttp.ClientSession()

        target_dir = Path.cwd() / "cogs"

        for cog in target_dir.rglob("*.py"):
            await self.load_extension(f"cogs.{cog.parent.name}.{cog.stem}")

        await cltree.sync()
        self.synced = True

    async def on_ready(self):
        await self.wait_until_ready()
        print(f"Logged in as {self.user}")

aclient = client()
cltree = aclient.tree

load_dotenv()
aclient.run(os.getenv("TOKEN"))            