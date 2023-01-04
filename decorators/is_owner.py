# DISCORD IMPORTS
import discord
from discord import app_commands


def is_owner():
    def predicate(interaction: discord.Interaction) -> bool:
        return interaction.user.id == 394138910508449792

    return app_commands.check(predicate)
