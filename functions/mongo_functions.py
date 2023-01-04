# DISCORD IMPORTS
import discord

# MONGODB IMPORTS
from typing import Literal
import motor.motor_asyncio
from pymongo.write_concern import WriteConcern
import pymongo

# OS IMPORTS
import os


async def connect(db_name: str):
    """
    Creates a connection to the database, returns a client and a db object.
    """

    client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("DB_URL"))
    db = client[db_name]
    return client, db


async def get_balance(target_user: discord.Member) -> int:
    """
    Returns the selected user's balance.
    """
    client, db = await connect("totobot")
    collection = db["economia"]
    find_user = await collection.find_one({"_id": target_user.id})
    client.close()

    if find_user:
        return find_user["balance"]

    return 0


async def add_money(target_user: discord.Member, amount: int) -> int:
    """
    Adds money to an user's account. Returns previous balance.
    """
    client, db = await connect("totobot")
    collection = db["economia"]
    find_user = await collection.find_one({"_id": target_user.id})

    if not find_user:
        await collection.insert_one({"_id": target_user.id, "balance": amount})
        client.close()
    else:
        await collection.find_one_and_replace(
            {"_id": target_user.id}, {"balance": find_user["balance"] + amount}
        )
        client.close()
        return find_user["balance"]


async def subtract_money(target_user: discord.Member, amount: int) -> int:
    """
    Subtracts money from an user's account. Returns previous balance.
    """
    client, db = await connect("totobot")
    collection = db["economia"]
    find_user = await collection.find_one({"_id": target_user.id})

    if not find_user or find_user["balance"] < amount:
        client.close()
        raise Exception("Not enough funds")
    else:
        await collection.find_one_and_replace(
            {"_id": target_user.id}, {"balance": find_user["balance"] - amount}
        )
        client.close()
        return find_user["balance"]


async def get_top() -> list[str]:
    """
    Return a list of the top 5 richest users.
    """
    client, db = await connect("totobot")
    collection = db["economia"]
    top = [
        user
        async for user in collection.find().sort("balance", pymongo.DESCENDING).limit(5)
    ]

    client.close()

    return top


async def edit_skullnet_urls(interaction: discord.Interaction, skullnet_url: str):
    """
    Edits the skullnet's urls.
    """
    client, db = await connect("totobot")
    collection = db["config"]

    await collection.update_one(
        {"_id": interaction.guild.id},
        {"$set": {"_id": interaction.guild.id, "skullnet_url": skullnet_url}},
        upsert=True,
    )
    client.close()


async def get_skullnet_url(interaction: discord.Interaction) -> str:
    """
    Returns the server's skullnet url.
    """

    client, db = await connect("totobot")
    collection = db["config"]

    url = await collection.find_one({"_id": interaction.guild.id})

    client.close()
    return url["skullnet_url"] if url else None
